"""
Base class for an Evaluator
"""

from abc import ABC


class Evaluator(ABC):
    """
    Base class for an Evaluator
    """

    def evaluate(self, input_file_path):
        """
        Evaluates a given artifact based on the specific detector
        """
        pass
