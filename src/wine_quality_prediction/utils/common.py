import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

from wine_quality_prediction import logger


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """Reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Retuns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_fiale:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml File: {path_to_yaml} loaded successfully!!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Create a list of directories
    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool, optional): Ignore is multiple dirs are to created. Default is False
    """
    for path in path_to_directories:
        os.mkdir(path, exist_ok = True)
        if verbose:
            logger.info(f"Created directory at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save JSON data
    Args:
        path(Path): Path to JSON file
        data(dict): Data to be saved in JSON File
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON File data
    Args:
        path(Path): Path to JSON file

    Returns:
        ConfigBox: Data as class attribute instad of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file Loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path: Path):
    """Save Binary File
    Args:
        data(Any): Data to be saved in binary
        path(Path): Path to Binary file
    """
    joblib.dump(value= data, filename= path)
    logger.info(f"Binary file Saved successfully at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load Binary File data
    Args:
        path(Path): Path to Binary file

    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file Loaded successfully from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get Size in KB
    Args:
        path(Path): Path of file

    Returns:
        str: Size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb}KB"