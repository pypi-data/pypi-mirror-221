# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Emeralds
# Author: Jason Drawdy
# Version: 0.0.1
# Date: 07/21/23
# #########################################################################
# Description:
# Contains all classes and functions for creating a complete pip package.
# #########################################################################
from setuptools import setup, find_packages
import datetime
import zipfile
import hashlib
import shutil
import codecs
import os

class InstallHelper:
    """A encapsulation object containing all necessary components for creating a pip package."""
    def __init__(self: "InstallHelper") -> None:
        self.package = "emeralds"
        self.author = "Jason Drawdy"
        self.email = "<40871836+jasondrawdy@users.noreply.github.com>"
        self.version = '0.0.1'
        self.description = 'A testing package for learning PyPi.'
        self.long_description = self._get_project_readme()

    def _get_project_readme(self: "InstallHelper"):
        """Returns the current README documentation or a default description."""
        default_data = 'Cool package for testing!'
        current_path = os.path.abspath(os.path.dirname(__file__))
        readme_file = os.path.join(current_path, "README.md")
        if os.path.exists(readme_file):
            with codecs.open(readme_file, encoding="utf-8") as file:
                return file.read()
        return default_data 

    def prepare_for_packaging(self: "InstallHelper"):
        """Temporarily modifies the current project structure for more accurate packaging."""
        os.rename('src', self.package)

    def restore_original_structure(self: "InstallHelper"):
        """Creates the original file and directory structure before the creation of any packages."""
        os.rename(self.package, 'src')
    
    def create_project_package(self: "InstallHelper"):
        """Performs the actual package creation process using all provided `setup()` function information."""
        setup(
            name=self.package,
            version=self.version,
            author=self.author,
            author_email=self.email,
            description=self.description,
            long_description_content_type="text/markdown",
            long_description=self.long_description,
            packages=find_packages(),
            extras_require={'dev': ['twine', 'sphinx', 'sphinx-rtd-theme', 'sphinx-autoapi']},
            keywords=['emeralds', 'test', 'package'],
            classifiers=[
                "Development Status :: 1 - Planning",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11",
                "Operating System :: OS Independent",
            ]
        )

packager = InstallHelper()
packager.prepare_for_packaging()
packager.create_project_package()
packager.restore_original_structure()