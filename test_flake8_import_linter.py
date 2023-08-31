import ast
from flake8_import_linter import Plugin

from unittest import TestCase


class TestFlake8ImportLinter(TestCase):

    def _expect_forbidden(self, string):
        tree = ast.parse(string)
        plugin = Plugin(tree)

        err_count = 0
        for x in plugin.run():
            err_count = 1
            self.assertTrue(x[0] == 1)
            self.assertTrue(x[1] == 0)
            self.assertTrue(x[2] == "IMP100 forbiden import")

        self.assertTrue(err_count == 1)

    def _expect_no_error(self, string):
        tree = ast.parse(string)
        plugin = Plugin(tree)

        err_count = 0
        for x in plugin.run():
            err_count = 1

        self.assertTrue(err_count == 0)

    def test_absolute_submodule_import(self):
        self._expect_forbidden("from unittest import TestCase")

    def test_absolute_full_import(self):
        self._expect_forbidden("import pytest")

    def test_absolute_import_as(self):
        self._expect_forbidden("import pytest as pt")

    def test_relative_import(self):
        self._expect_no_error("from .a import b")

    def test_no_file(self):
        self._expect_no_error("")
