import json
import twitter3


def checking(dict_keys):
    """
    This function makes a menu out of list of dictionary keys. Returns the index of the key
    :param dict_keys: list
    :return: int
    """
    print("\nHere are the main keys for your file, type the number of which one you need:\n")

    for i in range(len(dict_keys)):
        print(i, dict_keys[i])
    print(len(dict_keys), "If you want the content of all of them\n")

    num = input("Please, type the number: ")
    num = int(num)
    while (0 > num) or (num > len(dict_keys)):
        num = input("Typed the wrong number. Please type carefully again: ")
    return num


def user_friends(json_file):
    """
    This function returns the list of twitter user friends' names
    :param json_file: twitter json object
    :return: list(str, str...)
    """
    user_friends = []
    for friend in json_file["users"]:
        user_friends.append(friend["screen_name"])
    return user_friends


def read_from_file(path):
    """
    This function reads from twitter json file and returns only the needed parts of it
    :param path: str (name of the file)
    :return: json object    """
    with open(path, encoding="UTF-8") as file:
        part = json.load(file)
        friends = user_friends(part)
        options = list(part.keys())

        while True:
            num = checking(options)
            if num == len(options):
                return part
            elif num == 0:
                print("Choose the user you want to get data of: ")
                number = checking(friends)
                if number == len(friends):
                    return part

            part = part[options[num]]

            if isinstance(part, list) and len(part) > 0:
                for elem in part:
                    if elem["screen_name"] == friends[number]:
                        part = elem
                        break
            else:
                return part
            options = list(part.keys())


if __name__ == "__main__":
    twitter3.get_twitter_json()
    print(json.dumps(read_from_file("try_new.json"), indent=2))

    print("Done, my master...")