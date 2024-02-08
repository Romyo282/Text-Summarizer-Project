# To logging all infos during runtime

import os
from pathlib import Path
import logging

# Creat Logging screan

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",  # to do (cicd) Deployment
    f"src/{project_name}/__init__.py", # constructor to use in istallation of local package
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", # where i'll write my utility
    f"src/{project_name}/logging/__init__.py", # constructor to use in logging
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", # to keep all model related parameters.
    "app.py",  
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

# To convert path to my specific OS format (windows).

for filepath in list_of_files:
    filepath = Path(filepath) 

    # this will separate the path dir and file.
    filedir, filename = os.path.split(filepath)

    # for folers creation if it's not empty.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # check if it is not exist .
    # not to replace files when i run template.
    if (not os.path.exists(filepath)) or(os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass 
            logging.info(f"Creating empty file: {filepath}") 


    else:
        logging.info(f"{filename} is already exist")        














