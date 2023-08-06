# rospy_yaml_include

## Introduction

rospy_yaml_include is a package that provides a YAML loader that can include other YAML files.

It can either include a file given an absolute path, or given a ROS package name and a relative path.

rospy_yaml_include has a recursive check to prevent circular imports. 

### Usage

The following section contains code snippets showing example usage of the package.
Additionally, the tests directory contains a few examples of how to use the package. 

### Including a yaml from an absolute path
```python
from rospy_yaml_include.yaml_include import RospyYamlInclude

yml = """
    value: 
    - 10
    fields: !path_include /path/to/file.yml
    """

constructor = RospyYamlInclude()
yaml.load(yml, Loader=constructor.add_constructor())
```

Alternatively, the yaml.load command can be used within a `with open()` statement to load yaml from a file.

### Including a yaml from a ROS package
```python
from rospy_yaml_include.yaml_include import RospyYamlInclude

yml = """
    value: 
    - 10
        fields: !ros_include 
                package: rospy_yaml_include_test
                extension: test_files/circular_import_ros.yaml
    """

constructor = RospyYamlInclude()
yaml.load(yml, Loader=constructor.add_constructor())
```

Alternatively, the yaml.load command can be used within a `with open()` statement to load yaml from a file.
