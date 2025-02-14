import yaml

def read_config(file_path="config/config.yaml"):
    """Read configuration from config.yaml"""
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config
