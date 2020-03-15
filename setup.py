# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lambda",
    version="1.0",
    author="Amy Beisel",
    author_email="amy.beisel@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/AmyBeisel/my_lambda",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)