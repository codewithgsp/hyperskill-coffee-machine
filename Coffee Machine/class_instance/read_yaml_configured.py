# To read the YAML file format from the onfiuration
import yaml
import os
path = "C:\\Users\\MASTEREB\\IdeaProjects\\Coffee Machine\\Coffee Machine\\class_instance\\"
config_file_name = "config.yaml"


def read_config_file(config_file):
    with open(os.path.join(path, config_file)) as file:
        list_ = yaml.load(file, Loader=yaml.FullLoader)
        print(list_)


read_config_file(config_file_name)
