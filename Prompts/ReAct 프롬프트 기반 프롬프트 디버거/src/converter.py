import os
import json
from enum import Enum

class FileType(Enum):
    FILE = "file"
    JSON = "json"

def load(dir : str, filename : str, file_type : FileType) -> str:
    if file_type == FileType.FILE:
        with open(f'{dir}/{filename}', 'r', encoding='utf-8') as file:
            return file.read()
    elif file_type == FileType.JSON:
        with open(f'{dir}/{filename}', 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        raise ValueError("Invalid file type")

def inject_inputValues_to_prompt(backupped : str, input_values : dict) -> str:
    for key, value in input_values.items():
        if value is None:
            raise ValueError(f'Value of {key} is None')
        backupped = backupped.replace(f'[{key}]', value)
    return backupped

def load_injected_prompt(path_to_dir : str = os.getcwd()):
    backupped = load(path_to_dir, 'origin.md', FileType.FILE)
    input_values = load(path_to_dir, 'input.json', FileType.JSON)
    injected = inject_inputValues_to_prompt(backupped, input_values)
    return injected

def load_debug_prompt(path_to_dir : str = os.getcwd(), system_prompt : str = "", mode = "react"):
    if mode == "react":
        debug_direction = load(path_to_dir, 'ReAct.md', FileType.FILE)
        prompt = debug_direction.replace("###promptposition###", system_prompt)
        return prompt
    else:
        return system_prompt