"""
Tools for manipulating and using ExSourceFiles.
"""
from os import path
import json
import subprocess
from copy import deepcopy
from tempfile import gettempdir
import logging
import hashlib
import argparse
import yaml
from jsonschema import validate

from exsource_tools import utils

logging.basicConfig()
LOGGER = logging.getLogger('exsource')
LOGGER.setLevel(logging.INFO)

SOURCE_PATH = path.dirname(__file__)
SCHEMA_PATH = path.join(SOURCE_PATH, "schemas")

UNSTAGED = 0
PENDING = 1
SKIPPED = 2
PROCESSED = 3

CONTINUE = 10
SKIP = 11
DELAY = 12
UNCHANGED = 13

def _exsource_file_format(filepath, mode="read"):
    """
    Return the format of an exsource file based on filename.

    This will error if the file type is not supported
    """
    if filepath.lower().endswith('.yml') or filepath.lower().endswith('.yaml'):
        file_format = "YAML"
    elif filepath.lower().endswith('.json'):
        file_format = "JSON"
    else:
        raise ValueError(f"Couldn't {mode} '{filepath}'. "
                         "Only YAML and JSON exsource files are supported.")
    return file_format

def load_exsource_file(filepath):
    """
    Load an exsource file from the inupt filepath. An ExSource object is returned
    """
    file_format = _exsource_file_format(filepath, "read")
    with open(filepath, 'r', encoding="utf-8") as file_obj:
        file_content = file_obj.read()
        if file_format == "JSON":
            input_data = json.loads(file_content)
        else:
            #only other option is YAML
            input_data = yaml.safe_load(file_content)
    return ExSource(input_data)

class ExSource:
    """
    Class that stores and validates ExSource data.
    """

    def __init__(self, exsource_data):
        self._store(exsource_data)

    def validate(self, data):
        """
        Validate data against schema
        """
        validate(instance=data, schema=self.load_schema())

    def _store(self, data):
        """
        Store data if valid
        """
        self.validate(data)
        self._extra_data = deepcopy(data)
        self._exports = {key: ExSourceExport(data['exports'][key]) for key in data['exports']}
        del self._extra_data['exports']
        all_output_filenames = [file_obj.filepath for file_obj in self.all_output_files]
        if len(set(all_output_filenames)) != len(all_output_filenames):
            LOGGER.warning("Warning: Multiple exports define the creation of the same input file.")

    def dump(self):
        """
        Return the ExSource data as a python dictionary. This can then be dumped to file.
        """
        data = deepcopy(self._extra_data)
        data['exports'] = {key: self._exports[key].dump() for key in self._exports}
        # Check still valid, as the data may have been updated directly.
        self.validate(data)
        return data

    def save(self, filepath):
        """
        Save ExSource data to file.
        """
        file_format = _exsource_file_format(filepath, "write")
        with open(filepath, 'w', encoding="utf-8") as file_obj:
            if file_format == "JSON":
                json.dump(self.dump(), file_obj, sort_keys=True, indent=4)
            else:
                #only other option is YAML
                file_obj.write(yaml.dump(self.dump()))

    def set_data(self, data):
        """
        Set data from dictionary
        """
        self._store(data)

    def load_schema(self):
        """
        Return the exsource schema.
        """
        schema_file = path.join(SCHEMA_PATH, "exsource.schema.json")
        with open(schema_file, 'r', encoding="utf-8") as file_obj:
            schema = json.loads(file_obj.read())
        return schema

    @property
    def exports(self):
        """
        Return the list of ExSourceExport objects
        """
        return self._exports

    @property
    def all_output_files(self):
        """
        A list of output files for every export combined
        """
        output_files = []
        for _, export in self.exports.items():
            output_files += export.output_files
        return output_files

    @property
    def all_input_files(self):
        """
        A list of input files for every export combined
        """
        input_files = []
        for _, export in self.exports.items():
            input_files += export.input_files
        return input_files

    def export_for(self, filepath):
        """
        Return the export that generates the file specified as `filepath`.
        The return is a ExSourceExport object
        """
        for _, export in self.exports.items():
            if filepath in export.output_files:
                return export
        return None


class ExSourceExport:
    """
    A class to hold the data for an exsource export
    """
    # This is mostly seriealisation and de serialisation
    # There must be a better way than this?:
    # - Keeping everything in a dictionary is rubbish.
    # - Writing a marshmallow schema for a json schema seems silly
    # - Marshmallow-jsonschema goes the wrong way

    def __init__(self, data):
        self._extra_data = deepcopy(data)
        self._output_files = [ExSourceFile(file_data) for file_data in data['output-files']]
        del self._extra_data['output-files']
        self._source_files = [ExSourceFile(file_data) for file_data in data['source-files']]
        del self._extra_data['source-files']
        self._application = data['application']
        del self._extra_data['application']

        self._name = None
        self._description = None
        self._parameters = None
        self._app_options = None
        self._dependencies = None
        self._dependencies_exhaustive = None

        self._load_optional_properties(data)

    def _load_optional_properties(self, data):
        if 'name' in data:
            self._name = data['name']
            del self._extra_data['name']
        if 'description' in data:
            self._description = data['description']
            del self._extra_data['description']
        if 'parameters' in data:
            self._parameters = data['parameters']
            del self._extra_data['parameters']
        if 'app-options' in data:
            self._app_options = data['app-options']
            del self._extra_data['app-options']
        if 'dependencies' in data:
            self._dependencies = [ExSourceFile(file_data) for file_data in data['dependencies']]
            del self._extra_data['dependencies']
        if 'dependencies-exhaustive' in data:
            self._dependencies_exhaustive = data['dependencies-exhaustive']
            del self._extra_data['dependencies-exhaustive']

    def unchanged_from(self, previous):
        """
        Return true if this export is unchanged from a previous run. This will check the file
        hashes on disk.
        """

        if not isinstance(previous, ExSourceExport):
            return False
        if self.application != previous.application:
            return False
        if self.parameters != previous.parameters:
            return False
        if set(self.app_options) != set(previous.app_options):
            return False
        source_unchanged = self._source_files_unchanged(previous)
        output_unchanged = self._output_files_unchanged(previous)
        deps_unchanged = self._dependencies_unchanged(previous)

        return source_unchanged and output_unchanged and deps_unchanged

    def _source_files_unchanged(self, previous):
        if len(self.source_files) != len(previous.source_files):
            return False
        for source_file, previous_source_file in zip(self.source_files, previous.source_files):
            if source_file.filepath != previous_source_file:
                return False
            if not previous_source_file.unchanged_on_disk:
                return False
        return True

    def _output_files_unchanged(self, previous):
        if len(self.output_files) != len(previous.output_files):
            return False
        for output_file, previous_output_file in zip(self.output_files, previous.output_files):
            if output_file.filepath != previous_output_file:
                return False
            if not previous_output_file.unchanged_on_disk:
                return False
        return True

    def _dependencies_unchanged(self, previous):
        for dep in previous.dependencies:
            if not dep.unchanged_on_disk:
                return False
        return True


    def __getitem__(self, key):
        return dict.__getitem__(self._extra_data, key)

    def dump(self):
        """
        Return the data for this export as a python dictionary.
        """
        data = deepcopy(self._extra_data)
        data['output-files'] = [file_obj.dump() for file_obj in self._output_files]
        data['source-files'] = [file_obj.dump() for file_obj in self._source_files]
        data['application'] = self._application
        if self._name is not None:
            data['name'] = self._name
        if self._description is not None:
            data['description'] = self._description
        if self._parameters is not None:
            data['parameters'] = self._parameters
        if self._app_options is not None:
            data['app-options'] = self._app_options
        if self._dependencies is not None:
            data['dependencies'] = [file_obj.dump() for file_obj in self._dependencies]
        if self._dependencies_exhaustive is not None:
            data['dependencies-exhaustive'] = self._dependencies_exhaustive
        return data

    @property
    def output_files(self):
        """
        Return the list of output files
        """
        return self._output_files

    @property
    def source_files(self):
        """
        Return the list of source files
        """
        return self._source_files

    @property
    def application(self):
        """
        Return the application used to perform the export
        """
        return self._application

    @property
    def name(self):
        """
        Return the name of the export
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the export name. This is the human freindly name.
        """
        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Name must be a string")
        self._name = value

    @property
    def description(self):
        """
        Return the description of the export
        """
        return self._description

    @description.setter
    def description(self, value):
        """
        Set the export description. This is the human freindly description.
        """
        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Description must be a string")
        self._description = value

    @property
    def parameters(self):
        """
        Return the parameters to be used for export
        """
        if self._parameters is None:
            return {}
        return self._parameters

    @property
    def app_options(self):
        """
        Return the application commandline options to be used for export
        """
        if self._app_options is None:
            return []
        return self._app_options

    @property
    def dependencies(self):
        """
        Return the list of dependencies
        """
        if self._dependencies is None:
            return []
        return self._dependencies

    @property
    def dependencies_exhaustive(self):
        """
        Return whether the dependencies list is exhaustive
        """
        if self._dependencies_exhaustive is None:
            return False
        return self._dependencies_exhaustive

    def add_dependency(self, filepath, store_hash=False):
        """
        Add a dependency to this export
        """
        if self._dependencies is None:
            self._dependencies = []
        self._dependencies.append(ExSourceFile(filepath))
        if store_hash:
            self._dependencies[-1].store_hash()

    def mark_dependencies_exhaustive(self):
        """
        Mark that the dependency list is now exhaustive
        """
        self._dependencies_exhaustive = True


class ExSourceFile:
    """
    Class to store the information for a file. This could just be the filepath
    but can also contain the MD5 hash.
    """

    def __init__(self, data):
        if isinstance(data, str):
            self._filepath = data
            self._md5 = None
            self._extra_data = {}
        elif isinstance(data, dict):
            self._extra_data = deepcopy(data)
            self._filepath = data['filepath']
            del self._extra_data['filepath']
            self._md5 = data['md5']
            del self._extra_data['md5']
        else:
            raise TypeError("Expecting a dictionary or a string")

    def __eq__(self, other):
        if isinstance(other, str):
            return self.filepath == other
        if isinstance(other, ExSourceFile):
            if self.md5 is None or self.md5 == other.md5:
                if self.filepath == other.filepath:
                    return True
            return False
        super().__eq__(other)

    def __repr__(self):
        return self._filepath

    def dump(self):
        """
        Return the data for this file as a python dictionary.
        """
        if self._extra_data == {} and self._md5 is None:
            return self._filepath

        data = deepcopy(self._extra_data)
        data['filepath'] = self._filepath
        data['md5'] = self._md5
        return data

    def store_hash(self):
        """
        Store the hash for this file if it exists
        """
        if self.exists:
            self._md5 = self.get_hash_on_disk()

    def get_hash_on_disk(self):
        """
        Return the hash for this file if it exists
        """
        if not self.exists:
            return None
        hash_md5 = hashlib.md5()
        with open(self._filepath, "rb") as file_obj:
            for chunk in iter(lambda: file_obj.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @property
    def exists(self):
        """
        Return whether this file exists on disk
        """
        return path.isfile(self._filepath)

    @property
    def filepath(self):
        """
        Return the filepath of this file
        """
        return self._filepath

    @property
    def md5(self):
        """
        Return the md5 sum of this file. This will be none if the file
        hasn't been hashed. To hash the file use store_hash.
        """
        return self._md5

    @property
    def unchanged_on_disk(self):
        """
        Return false if the file has changed on disk
        """
        if self._md5 is None:
            #Can't know if changed, so assumed to have changed
            return False
        if not self.exists:
            return False
        return self.get_hash_on_disk() == self._md5


def make_parser():
    """
    Create the argument parser for the exsource-make command
    """
    description = "Process exsource file to create inputs."
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)
    def_help = "Path to ExSource definition file. Default is exsource-def.yml or exsource-def.json"
    parser.add_argument("-d", "--exsource-def", help=def_help)
    out_help = "Path to ExSource output file. Default is exsource-out.yml or exsource-out.json"
    parser.add_argument("-o", "--exsource-out", help=out_help)
    headless_help = ("Set this flag on machines without an X server running. Commands "
                     "requring X will be run with xvfb. Ensure xvfb is installed.")
    parser.add_argument("-H", "--headless", action='store_true', help=headless_help)
    return parser

def find_def_file():
    """
    Find the exsource definition file in the current directory.
    """
    default_names = ["exsource-def.yml", "exsource-def.yaml", "exsource-def.json"]
    for def_name in default_names:
        if path.isfile(def_name):
            return def_name
    return None

def find_out_file():
    """
    Find the exsource output file in the current directory.
    """
    default_names = ["exsource-out.yml", "exsource-out.yaml", "exsource-out.json"]
    for def_name in default_names:
        if path.isfile(def_name):
            return def_name
    return None

def make():
    """
    This is the function run by the entrypoint exsource-make
    """
    parser = make_parser()
    args = parser.parse_args()

    def_filepath = args.exsource_def
    if def_filepath is None:
        def_filepath = find_def_file()
    if def_filepath is None:
        #If still is None then error
        raise RuntimeError("Couldn't find ExSource definition file.")
    def_file = load_exsource_file(def_filepath)

    out_filepath = args.exsource_out
    if out_filepath is None:
        out_filepath = find_out_file()

    out_file = None
    if out_filepath is not None and path.exists(out_filepath):
        out_file = load_exsource_file(out_filepath)

    processor = ExSourceProcessor(def_file, out_file, out_filepath, args.headless)
    processor.make()

class ExSourceProcessor:
    """
    This class processes the data in the exsource file to create all the ouputs.
    Currently it only works for certain OpenSCAD and FreeCAD exports
    """

    def __init__(self,
                 exsource_def,
                 previous_exsource=None,
                 exsource_out_path=None,
                 headless=False):

        self.headless = headless
        self._exsource = deepcopy(exsource_def)
        self._exsource_prev = previous_exsource
        self._exsource_out_path = exsource_out_path
        self._all_output_files = {output.filepath: UNSTAGED for output in self._exsource.all_output_files}

    def make(self):
        """
        Process all exsource exports (if possible)
        """
        self._all_output_files = {output.filepath: PENDING for output in self._exsource.all_output_files}
        iteration = 0
        unprocessed_exports = self._exsource.exports
        while len(unprocessed_exports) > 0:
            #TODO: make less simplistic
            iteration += 1
            if iteration > len(self._exsource.exports):
                raise RuntimeError("Circular dependencies in exsource file")

            unprocessed_exports = self._process_exports(unprocessed_exports)

        outpath = self._exsource_out_path
        if outpath is None:
            outpath = 'exsource-out.yml'
        self._exsource.save(outpath)

    def _process_exports(self, exports_to_process):
        unprocessed_exports = {}

        for export_id, export in exports_to_process.items():
            LOGGER.info("Processing export: %s", export_id)
            app = export.application

            dep_action = self._check_dependencies(export_id, export)

            if dep_action == CONTINUE:
                if app.lower() == "openscad":
                    self._process_openscad(export)
                elif app.lower() == "freecad":
                    self._process_freecad(export)
                else:
                    LOGGER.warning("Skipping %s as no methods available process files with %s",
                                   export_id,
                                   app)
                    for output in export.output_files:
                        self._all_output_files[output.filepath] = SKIPPED
            elif dep_action == SKIP:
                for output in export.output_files:
                    self._all_output_files[output.filepath] = SKIPPED
                LOGGER.warning("Skipping %s it has skipped dependencies", export_id)
            elif dep_action == DELAY:
                unprocessed_exports[export_id] = export
                LOGGER.info("Delaying %s as it has unprocessed dependencies", export_id)
            elif dep_action == UNCHANGED:
                #Move all extra information over if eveything is unchanged since last run.
                new_export = deepcopy(self._exsource_prev.exports[export_id])
                new_export.name = export.name
                new_export.description = export.description
                self._exsource.exports[export_id] = new_export

        return unprocessed_exports

    def _check_dependencies(self, export_id, export):
        """
        action to take based on dependency and source file status
        """
        # Store all hashes of all dependent files (both dependencies and source files)
        # before checking if changed
        if self._exsource_prev is not None:
            if export_id in self._exsource_prev.exports:
                prev_export = self._exsource_prev.exports[export_id]
                #Always reprocess is dependencies aren't exhaustive
                if prev_export.dependencies_exhaustive and export.unchanged_from(prev_export):
                    LOGGER.info("Export %s: is unchanged, no processing needed", export_id)
                    return UNCHANGED
        action = CONTINUE
        for dep in export.dependencies + export.source_files:
            dep.store_hash()
            if dep.filepath in self._all_output_files:
                dep_status = self._all_output_files[dep.filepath]
                if dep_status == SKIPPED:
                    return SKIP
                if dep_status == PENDING:
                    LOGGER.info("Dependent file: %s not yet processed", dep.filepath)
                    action = DELAY
                    #No return here as another dependency might require it be skipped

        return action

    def _process_openscad(self, export):
        #TODO: Tidy up
        assert len(export.output_files) == 1, "OpenSCAD expects only one output"
        output = export.output_files[0]
        assert len(export.source_files) == 1, "Openscad expects only one source file"
        source = export.source_files[0]

        require_x = True if output.filepath.lower().endswith('.png') else False


        params = []
        for parameter in export.parameters:
            if isinstance(export.parameters[parameter], (float, int)):
                par = str(export.parameters[parameter])
            elif isinstance(export.parameters[parameter], bool):
                #ensure lowercase for booleans
                par = str(export.parameters[parameter]).lower()
            elif isinstance(export.parameters[parameter], str):
                par = export.parameters[parameter]
            else:
                LOGGER.warning("Can only process string, numerical or boolean arguments "
                               "for OpenSCAD. Skipping parameter %s", parameter)
                continue
            params.append("-D")
            params.append(f"{parameter}={par}")

        executable = "openscad"

        depfilename = output.filepath + ".d"
        utils.add_directory_if_needed(output.filepath)
        openscad_file_args = ["-d", depfilename, "-o", output.filepath, source.filepath]
        openscad_args = export.app_options + params + openscad_file_args
        try:
            if self.headless and require_x:
                xrvb_args = ['xvfb-run',
                             '--auto-servernum',
                             '--server-args',
                             '-screen 0 1024x768x24']
                args = xrvb_args + [executable] + openscad_args
            else:
                args = [executable] + openscad_args
            ret = subprocess.run(args, check=True, capture_output=True)
            #print std_err as OpenSCAD uses it to print rather than std_out
            std_err = ret.stderr.decode('UTF-8')
            print(std_err)
        except subprocess.CalledProcessError as error:
            std_err = error.stderr.decode('UTF-8')
            raise RuntimeError(f"\n\nOpenSCAD failed create file: {output} with error:\n\n"
                               f"{std_err}") from error
        output.store_hash()
        depsfile = utils.Depsfile(depfilename)
        assert len(depsfile.rules) == 1, "Expecting only one rule in and openscad deps file"
        assert len(depsfile.rules[0].outputs) == 1, "Expecting only one output to be specified in the openscad depsile"
        assert depsfile.rules[0].outputs[0] == output, "depsfile output doens't match expected file"
        for dep in depsfile.rules[0].dependencies:
            if dep not in export.source_files+export.dependencies:
                export.add_dependency(dep, store_hash=True)
        export.mark_dependencies_exhaustive()
        self._all_output_files[output.filepath] = PROCESSED

    def _process_freecad(self, export):
        #TODO: Tidy up

        outputs = export.output_files
        sources = export.source_files
        assert len(sources) == 1, "FreeCAD expects only one source file"
        sourcefile = sources[0].filepath
        assert len(export.app_options) == 0, "Cannot apply options to FreeCAD"
        for parameter in export.parameters:
            LOGGER.info("Cannot process parameters for FreeCAD skipping parameter %s",
                        parameter)
            continue

        for outfile_obj in outputs:
            outfile = outfile_obj.filepath
            utils.add_directory_if_needed(outfile_obj.filepath)
            if outfile.lower().endswith('.stp') or outfile.lower().endswith('.step'):
                macro = (f"doc = FreeCAD.openDocument('{sourcefile}')\n"
                         "body = doc.getObject('Body')\n"
                         f"body.Shape.exportStep('{outfile}')\n")
            elif outfile.lower().endswith('.stl'):
                macro = ("from FreeCAD import Mesh\n"
                         f"doc = FreeCAD.openDocument('{sourcefile}')\n"
                         "body = doc.getObject('Body')\n"
                         f"Mesh.export([body], '{outfile}')\n")
            tmpdir = gettempdir()
            macropath = path.join(tmpdir, "export.FCMacro")
            with open(macropath, 'w', encoding="utf-8") as file_obj:
                file_obj.write(macro)
            subprocess.run(["freecadcmd", macropath], check=True)
            outfile_obj.store_hash()
            self._all_output_files[outfile] = PROCESSED

