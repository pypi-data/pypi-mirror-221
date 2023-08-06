"""
This file contains misc utilities
"""

import re
import os

class DependencyRule:
    """
    Class to store a single dependency rule
    """

    def __init__(self, outputs, dependencies):

        self._outputs = [os.path.relpath(output) for output in outputs]
        self._dependencies = [os.path.relpath(dep) for dep in dependencies]

    @property
    def outputs(self):
        """
        Returns the list of the outputs specified in the dependency rule
        """
        return self._outputs

    @property
    def dependencies(self):
        """
        Returns the list of the dependencies specified in the dependency rule
        """
        return self._dependencies


class Depsfile:
    """
    A class to read the contents of a make depsfile and store the processed contents
    
    There seems to be close to no documentation for what goes into a standard
    depfile nor how it is escaped. This is likely to be the source of a number
    bugs early early on.
    """

    def __init__(self, filepath):
        self._filepath = filepath
        self._rules = []
        self._read_file()

    @property
    def filepath(self):
        """
        Returns the filepath of the depsfile
        """
        return self._filepath

    @property
    def rules(self):
        """
        Returns the list of rules in the deps file. There is normally only one rule.
        Each rules is a DependencyRule object
        """
        return self._rules

    def _read_file(self):
        with open(self._filepath, 'r', encoding="utf-8") as depsfile:
            contents = depsfile.read()
        #Remove line continuations
        contents = re.sub(r"\\\n", " ", contents)
        # Replace tabs with a single space
        contents = re.sub(r"\t", " ", contents)
        # remove repeat spaces
        contents = re.sub(r" {2,}", " ", contents)
        self._store_rules(contents)


    def _store_rules(self, contents):

        #split into rules removing leading and trailing whitespace
        text_rules = [rule.strip() for rule in contents.split('\n')]
        #remove any empty rules
        text_rules = [rule for rule in text_rules if len(rule)>0]

        for text_rule in text_rules:
            self._process_and_save_rule(text_rule)


    def _process_and_save_rule(self, rule_text):
        # get list of non-scaped spaces
        spaces = [match.start() for match in re.finditer(r"(?<!\\) ", rule_text)]
        # Split at the spaces to get all items in the rule
        items = [rule_text[i[0]+1:i[1]] for i in zip([-1]+spaces, spaces+[len(rule_text)])]
        # Removing escaped spaces. Hard to know what other characters should be escaped
        # Somethings online seem to imply that # should be escaped but impirically this
        # is not the case for OpenSCAD. Strangely : is not escaped by OpenSCAD which
        # could cause problems
        items = [re.sub(r"\\ ", " ", item) for item in items]
        outputs = []
        deps = []
        colon_delimeter_found = False
        for item in items:
            if colon_delimeter_found:
                deps.append(item)
            else:
                if item.endswith(":"):
                    colon_delimeter_found = True
                    outputs.append(item[:-1])
                else:
                    outputs.append(item)
        self._rules.append(DependencyRule(outputs, deps))

def add_directory_if_needed(filepath):
    directory = os.path.dirname(filepath)
    if not directory == "":
        if not os.path.exists(directory):
            os.makedirs(directory)