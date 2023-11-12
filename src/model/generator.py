"""
Abstract Base Class of a Generator
"""
from abc import ABC, abstractmethod


class Generator(ABC):
    """
    Abstract Base Class of a Generator

    This can be used as interface to abstract from different generating models
    """

    def __int__(self):
        self.type = "abstract"

    @abstractmethod
    def generate(self, output_file_path):
        """
        Generates an artefact and returns it
        """
        pass
