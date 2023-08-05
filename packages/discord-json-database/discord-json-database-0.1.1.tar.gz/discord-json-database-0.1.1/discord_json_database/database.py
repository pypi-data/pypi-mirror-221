from .data import Data
from .errors import Errors
from .error_tests import ErrorTests
import os


class Database:
    def __init__(self, *args, filepath: str = None, data_structure: dict = None):
        self.filepath = None
        self.data_structure = None

        self.set_filepath(filepath)
        self.set_data_stucture(data_structure)

    def set_filepath(self, filepath: str):
        """Sets the filepath for this database. Must point to a txt file."""
        if filepath == None:
            raise Errors.FilePathNotSet()
        if not os.path.exists(os.path.dirname(filepath)):
            raise FileNotFoundError(
                f"The specified file path '{os.path.dirname(filepath)}' does not exist."
            )
        if not filepath.endswith(".txt"):
            raise Errors.IncorrectFileType(".txt", filepath)

        self.filepath = filepath

    def set_data_stucture(self, data_structure: dict):
        """Sets the filepath for this database. Must point to a txt file."""
        if data_structure == None:
            raise Errors.DataStructureNotSet()
        if not isinstance(data_structure, dict):
            raise TypeError("Data Structure must be of type `dict`")
        if not ErrorTests.dataStructureHasID(data_structure):
            raise Errors.NoIdInDataStructure()

        self.data_structure = data_structure

    def get_data(self, id: int):
        if self.data_structure is None:
            raise Errors.DataStructureNotSet()

        return Data(self, id)
