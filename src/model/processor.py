"""
Abstract base class to augment data
"""
from abc import ABC


class Processor(ABC):
    """
    Interface for a general approach to augment different artifacts
    """
    pass

    def process(self, input_file, output_file):
        """
        Augment the given file with some predefined behaviour
        """
        pass
