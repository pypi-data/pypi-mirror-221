"""
rospy_yaml_include
------------------

This module provides a way to include yaml files in other yaml files.
"""

import os
import yaml

import rospkg


class RospyYamlInclude:
    """
    RospyYamlInclude class
    """

    def __init__(
        self, loader: type = yaml.SafeLoader, base_directory: str = None
    ) -> None:
        self.recursion_limit = 50
        self.recursion_count = 0

        self.loader = loader
        self.base_directory = base_directory

    class _RosInclude:
        """
        Mappping for !ros_include constructor
        """

        def __init__(self, package, extension) -> None:
            self.package = package
            self.extension = extension

    def _ros_include_constructor(
        self, loader: type, node: yaml.nodes.MappingNode
    ) -> dict:
        """
        _ros_include_constructor function handles !ros_include tag
        """
        rospack = rospkg.RosPack()

        file = self._RosInclude(**loader.construct_mapping(node))

        include_file = os.path.join(
            rospack.get_path(file.package),
            file.extension,
        )

        with open(include_file, encoding="utf-8") as yaml_file:
            return yaml.load(yaml_file, Loader=self.add_constructor())

    def _path_include_constructor(
        self, loader: type, node: yaml.nodes.ScalarNode
    ) -> dict:
        """
        _path_include_constructor function handles !path_include tag

        """
        self.recursion_count += 1
        if self.recursion_count > self.recursion_limit:
            raise RecursionError(
                "Maximum recursion limit reached, check for circular references"
            )

        file = loader.construct_scalar(node)

        with open(file, encoding="utf-8") as yaml_file:
            return yaml.load(yaml_file, Loader=self.add_constructor())

    def _relative_include_constructor(
        self, loader: type, node: yaml.nodes.ScalarNode
    ) -> dict:
        """
        _path_include_constructor function handles !relative_include tag

        this can be used to import a yaml relative to a base directory provided in the class init
        """

        self.recursion_count += 1
        if self.recursion_count > self.recursion_limit:
            raise RecursionError(
                "Maximum recursion limit reached, check for circular references"
            )

        if self.base_directory is None:
            raise ValueError(
                "base_directory must be provided in class init to use !relative_include"
            )

        file = loader.construct_scalar(node)

        include_file = os.path.join(
            self.base_directory,
            file,
        )

        with open(include_file, encoding="utf-8") as yaml_file:
            return yaml.load(yaml_file, Loader=self.add_constructor())

    def _dynamic_include_constructor(
        self, loader: type, node: yaml.nodes.ScalarNode
    ) -> dict:
        """
        _dynamic_include_constructor function handles !include tag

        this constructor attempts to infer the type of include based on the file extension
        """

        self.recursion_count += 1
        if self.recursion_count > self.recursion_limit:
            raise RecursionError(
                "Maximum recursion limit reached, check for circular references"
            )

        file = loader.construct_scalar(node)

        if file.startswith("/"):
            include_file = file
        else:
            if self.base_directory is None:
                raise ValueError(
                    "base_directory must be provided in class init to use relative include"
                )

            include_file = os.path.join(
                self.base_directory,
                file,
            )

        with open(include_file, encoding="utf-8") as yaml_file:
            return yaml.load(yaml_file, Loader=self.add_constructor())

    def add_constructor(self) -> type:
        """
        add constructor to yaml
        """

        loader = self.loader
        loader.add_constructor("!ros_include", self._ros_include_constructor)
        loader.add_constructor("!path_include", self._path_include_constructor)
        loader.add_constructor("!relative_include", self._relative_include_constructor)
        loader.add_constructor("!include", self._dynamic_include_constructor)

        return loader
