
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    keys = dict.keys()
    for key in keys:
        if not isinstance(key, str):
            return False
    return all(key.islower() for key in keys) or all(key.isupper() for key in keys)

# Test cases
dict1 = {"a": "apple", "b": "banana"}
dict2 = {"a": "apple", "A": "banana", "B": "banana"}
dict3 = {"a": "apple", 8: "banana", "a": "apple"}
dict4 = {"Name": "John", "Age": "36", "City": "Houston"}
dict5 = {"STATE": "NC", "ZIP": "12345"}

print(check_dict_case(dict1))  # True
print(check_dict_case(dict2))  # False
print(check_dict_case(dict3))  # False
print(check_dict_case(dict4))  # False
print(check_dict_case(dict5))  # True
