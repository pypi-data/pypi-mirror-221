class ErrorTests:
    @staticmethod
    def dataStructureHasID(data_structure):
        if not isinstance(data_structure, dict):
            raise TypeError("Data Structure must be of type `dict`")

        try:
            data_structure["id"]
            return True
        except KeyError:
            return False
