from .file_operations import FileOperations
from .utils import Utils
from .errors import Errors
from .error_tests import ErrorTests


class Data:
    def __init__(self, database, id) -> None:
        """
        Initialize a Data object.

        Args:
            id (int): The ID of the entry.

        Raises:
            ValueError: If the id is not an integer.
        """
        if not isinstance(id, int):
            raise ValueError("id must be an integer.")

        self.id = id
        self.database = database

        if self.database.data_structure is None:
            raise Errors.DataStructureNotSet()
        if not ErrorTests.dataStructureHasID(self.database.data_structure):
            raise Errors.NoIdInDataStructure()

        # Get data for that id
        self.data: dict = self.__getData()

    def __getData(self):
        data = FileOperations.get_data(self.database)
        data_parsed = Utils.parseJsonList(data)

        # Standardize the Dictionary Properties
        data_parsed = Utils.standardizeListProperties(
            self.database.data_structure, data_parsed
        )

        users = Utils.getEntryFromKeyInJsonList(data_parsed, "id", self.id)
        if users != []:
            # Return the first user that has this id. Ideally, there should never be more than one.
            return users[0][1]
        else:
            # Create the user
            user_data = self.database.data_structure
            user_data["id"] = self.id

        return user_data

    def get(self, data: str):
        """
        Get any information that is stored with this entry.
        """
        if data in self.data.keys():
            return self.data[data]
        
        raise KeyError(f"Key `{data}` does not exist for this entry.")

    def set(self, data: str, value):
        """
        Set any information that is stored with this entry.
        """
        if data in self.data.keys():
            self.data[data] = value
            return value
        
        raise KeyError(f"Key `{data}` does not exist for this entry.")

    def save(self) -> None:
        """
        Save the data to the JSON file.
        """
        # Get old data
        all_data = FileOperations.get_data(self.database)
        all_data_parsed = Utils.parseJsonList(all_data)

        # Standardize the Dictionary Properties
        all_data_parsed = Utils.standardizeListProperties(
            self.database.data_structure, all_data_parsed
        )

        # Edit our entry
        new_data = Utils.editEntryFromKeyInJsonList(
            all_data_parsed, "id", self.id, self.data
        )

        # Save new data
        new_data_formatted = Utils.formatJsonList(new_data)
        FileOperations.save_data(self.database, new_data_formatted)

    def deleteDataAndSave(self) -> None:
        """
        Delete the data from the JSON file and save the changes.
        """
        # Get old data
        all_data = FileOperations.get_data(self.database)
        all_data_parsed = Utils.parseJsonList(all_data)

        # Standardize the Dictionary Properties
        all_data_parsed = Utils.standardizeListProperties(
            self.database.data_structure, all_data_parsed
        )

        # Delete our entry
        new_data = Utils.deleteEntryFromKeyInJsonList(
            all_data_parsed, "id", self.id
        )

        # Save new data
        new_data_formatted = Utils.formatJsonList(new_data)
        FileOperations.save_data(self.database, new_data_formatted)
