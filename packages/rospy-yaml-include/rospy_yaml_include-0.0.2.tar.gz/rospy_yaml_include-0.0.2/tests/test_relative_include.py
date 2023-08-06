import pytest
import sys
from rospy_yaml_include.yaml_include import RospyYamlInclude
import yaml
import os


class TestPathInclude:
    """
    Class containing unit tests for TestPathInclude
    """

    def test_path_include(self):
        """
        Unit test for path_include
        """
        cwd = os.getcwd()

        yml = """
            value: 
            - 10
            fields: !relative_include test_files/import.yaml
            """

        try:
            constructor = RospyYamlInclude(base_directory=cwd)
            yaml.load(yml, Loader=constructor.add_constructor())
        except RecursionError as error:
            pytest.fail(f"RecursionError: Maximum recursion limit reached: {error}")

    def test_path_circular_include(self):
        """
        Unit test for circular includes in path_include
        """
        cwd = os.getcwd()
        yml = """
            value: 
            - 10
            fields: !relative_include test_files/circular_import.yaml
            """
        try:
            constructor = RospyYamlInclude(base_directory=cwd)
            yaml.load(yml, Loader=constructor.add_constructor())
        except RecursionError as error:
            assert f"RecursionError caught: {error}"


if __name__ == "__main__":
    sys.exit(pytest.main(["--capture=no", __file__]))
