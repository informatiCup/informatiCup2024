"""
Abstract Base Class of a Generator
"""
from abc import ABC


class Generator(ABC):
    """
    Abstract Base Class of a Generator

    This can be used as interface to abstract from different generating models
    """

    def __int__(self):
        self.type = "abstract"

    def generate(self, output_file_path):
        """
        Generates an artefact and returns it
        """
        pass
