import json


class Utils:
    @staticmethod
    def parseJsonList(data: list) -> list[dict]:
        return [json.loads(object) for object in data]

    @staticmethod
    def formatJsonList(data: dict) -> list[str]:
        return [json.dumps(object) for object in data]

    @staticmethod
    def getEntryFromKeyInJsonList(
        list: list[dict], key: str, value
    ) -> tuple[int, dict]:
        returned_items = []
        for index, object in enumerate(list):
            if object[key] != None and object[key] == value:
                returned_items.append((index, object))

        return returned_items

    @staticmethod
    def editEntryFromKeyInJsonList(
        list: list[dict], key: str, value, new_entry: dict
    ) -> list:
        old_entry = Utils.getEntryFromKeyInJsonList(list, key, value)

        if old_entry == []:
            list.append(new_entry)
        else:
            list[old_entry[0][0]] = new_entry

        return list

    @staticmethod
    def deleteEntryFromKeyInJsonList(list: list[dict], key: str, value) -> list:
        old_entry = Utils.getEntryFromKeyInJsonList(list, key, value)

        if old_entry != []:
            list.pop(old_entry[0][0])

        return list
    
    @staticmethod
    def standardizeListProperties(defaultDict: dict, objectList: list[dict]):
        returnList = []
        for object in objectList:
            returnList.append(Utils.standardizeDictProperties(defaultDict, object))
            
        return returnList

    @staticmethod
    def standardizeDictProperties(defaultDict: dict, objectDict: dict):
        """A recursive function that makes sure that two dictionaries have the same properties.

        ------
        Parameters
        ------
        defaultDict: `dict`
            A dictionary containing all the properties and their default values.
        objectDict: `dict`
            The dictionary that will be edited.

        Returns
        ------
        `dict`
            The object dictionary after having its properties standardized.
        """

        # cloning defaultDict as returnDict
        returnDict = dict(defaultDict)

        # for each key:
        for key in returnDict.keys():
            # for each key in returnDict

            if key in objectDict.keys():
                # the key was in our objectdict. Now we just have to set it.
                # We have to check this recursively if this is a dictionary, and set this to be the returned value from the recursive function.

                if type(objectDict[key]) == dict:
                    # this is a dictionary.
                    # Now, we have to run this recursively to make sure that all values inside the dictionary are updated
                    returnDict[key] = Utils.standardizeDictProperties(
                        returnDict[key], objectDict[key]
                    )
                else:
                    # this is not a dictionary. It's just a regular value
                    # putting this value into returnDict
                    returnDict[key] = objectDict[key]
            else:
                # the key was not in the objectDict, but it was in the defaultDict.
                # but, because the key was already added (as the default), we don't need to worry at all.
                # lower dictionaries that may be attached to this are also not a concern, seeing how it never existed on the objectDict, so the defaults are fine.
                continue

        return returnDict
