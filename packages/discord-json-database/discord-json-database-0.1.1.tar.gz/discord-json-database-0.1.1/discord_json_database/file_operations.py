from .errors import Errors
import os


class FileOperations:
    @staticmethod
    def get_data(database):
        if database.filepath is None:
            raise Errors.FilePathNotSet()

        data = None
        if not os.path.exists(database.filepath):
            FileOperations.save_data(
                database, []
            )  # Create the file if it doesn't exist

        with open(database.filepath, "r") as file:
            data = file.read()

        return data.splitlines()

    @staticmethod
    def save_data(database, data_list):
        if database.filepath is None:
            raise Errors.FilePathNotSet()

        data = "\n".join(data_list)
        with open(database.filepath, "w") as file:
            file.write(data)
