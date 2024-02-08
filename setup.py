# Code for Local Package Setup.
# It will look for constructor file (__init__.py) every folder and install it 
# as my local package.

import setuptools

# Read README.md file to show it 
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Specify the Package Version.
__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Romyo282"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "midoom282@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)