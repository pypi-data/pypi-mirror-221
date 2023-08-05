class Errors:
    class IncorrectFileType(Exception):
        """Exception raised for errors with incorrect file type.

        Attributes:
            type: file type (ex: ".txt")
            filepath: filepath given
        """

        def __init__(self, type, filepath):
            self.type = type
            self.filepath = filepath
            super().__init__(
                f"The specified file path '{self.filepath}' must be of type '{self.type}'"
            )

    class FilePathNotSet(Exception):
        """Exception raised for when the file path is not set."""

        def __init__(self):
            super().__init__(
                f"File Path is MISSING! Use `json_database.database.set_filepath()` to set the file path, or set it when initalizing the database."
            )

    class DataStructureNotSet(Exception):
        """Exception raised for when the data structure is not set."""

        def __init__(self):
            super().__init__(
                f"Data Structure is MISSING! Use `json_database.database.set_data_structure()` to set the data structure, or set it when initalizing the database."
            )

    class NoIdInDataStructure(Exception):
        """Exception raised for when the data structure has no id."""

        def __init__(self):
            super().__init__(
                'No ID in data structure. Your data structure must contain an id. `{"id": None}`'
            )
