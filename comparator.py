EXCLUDED_FIELD_NAMES = (
    'message_id', 'track_file'
)


def _compare_two_lists_of_objects(list1: list, list2: list, compare_func):
    """Сравниваем два списка без учета их порядка."""
    if len(list1) != len(list2):
        return False
    for obj1 in list1:
        for obj2 in list2:
            if type(obj1) != type(obj2):
                continue
            if isinstance(obj1, dict):
                if compare_func(obj1, obj2):
                    break
            elif isinstance(obj1, list):
                if _compare_two_lists_of_objects(obj1, obj2, compare_func):
                    break
            else:
                if obj1 == obj2:
                    break
        else:
            return False
    return True


def compare_two_dicts_by_criteria(dict1: dict, dict2: dict):
    """Необходимо сравнить два словаря при этом они могут иметь в качестве значений в том числе списки
     - списки при этом при сравнении не должны учитывать порядок. Некоторые ключи словаря должны игнорироваться."""
    for key_d1, value_d1 in dict1.items():
        if key_d1 in EXCLUDED_FIELD_NAMES:
            continue
        for key_d2, value_d2 in dict2.items():
            if key_d2 in EXCLUDED_FIELD_NAMES:
                continue
            if key_d1 != key_d2:
                continue
            if type(value_d1) != type(value_d2):
                return False
            if isinstance(value_d1, dict):
                if not compare_two_dicts_by_criteria(value_d1, value_d2):
                    return False
            elif isinstance(value_d1, list):
                if not _compare_two_lists_of_objects(value_d1, value_d2, compare_two_dicts_by_criteria):
                    return False
            else:
                if not value_d1 == value_d2:
                    return False
    return True
