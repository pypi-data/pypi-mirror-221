import re
import typing


def auto_group_list_by_pkeys(
    primary_key_names: tuple, list_of_dicts: typing.List[dict], use_auto_group_dict: bool = True, each_result_item_callback: typing.Callable = None
) -> dict:
    """
    It can group items separated by "__" into listed groups and separate them by selected primary-key values.
    Example: Primary key is ("a",)
    [
     {"a": 1, "b": 2, "c__a": 33, "c__b": 44},
     {"a": 1, "b": 2, "c__a": 55, "c__b": 66},
     {"a": 2, "b": 2, "c__a": 7, "c__b": 88},
     {"a": 2, "b": 2, "c__a": 77, "c__b": 99}
    ]
    ===>
    {
        '1': {'a': 1, 'b': 2, 'c': [{'a': 33, 'b': 44}, {'a': 55, 'b': 66}]},  # each_result_item_callback
        '2': {'a': 2, 'b': 2, 'c': [{'a': 7, 'b': 88}, {'a': 77, 'b': 99}]}    # each_result_item_callback
    }
    :param primary_key_names: Specify name of columns which you want to group by
    :param list_of_dicts: List of dicts. Usually SQL Select result.
    :param use_auto_group_dict: Should be used funtion auto_group_dict for each row of grouped keys into list?
    :param each_result_item_callback: Function could be called for each row result. Row instance will be passed into as function attribute.
    :return: Dict with joined repeated rows and listed dicts with group prefix stored under joined primary key.
    """
    pk_results = {}
    for item in list_of_dicts:
        primary_key = "-".join([str(item[pk_item]) for pk_item in primary_key_names])
        result = pk_results.get(primary_key, {})
        grouped_row = {}
        for key, value in item.items():
            parsed_key = re.findall(r"^([a-zA-Z0-9]+)__([^_]+.*)$", key)
            if parsed_key:
                group_key = parsed_key[0][0]
                subgroup_key = parsed_key[0][1]
                if group_key in grouped_row:
                    grouped_row[group_key][subgroup_key] = value
                else:
                    grouped_row[group_key] = {subgroup_key: value}
            else:
                if use_auto_group_dict:
                    result = auto_group_dict({key: value}, merge_with_dict=result)
                else:
                    result[key] = value
        for key, group_line in grouped_row.items():
            if use_auto_group_dict:
                group_line = auto_group_dict(group_line)

            if key in result:
                result[key].append(group_line)
            else:
                result[key] = [group_line]

        if isinstance(each_result_item_callback, typing.Callable):
            callback_result = each_result_item_callback(result)
            result = callback_result if isinstance(callback_result, dict) else result

        pk_results[primary_key] = result
    return pk_results


def auto_group_list(list_of_dicts: typing.List[dict], use_auto_group_dict: bool = True, each_result_row_callback: typing.Callable = None) -> dict:
    """
    It can group items separated by "__" into listed groups.
    Example: [
                 {"a": 1, "b": 2, "c__a": 3, "c__b": 4},
                 {"a": 1, "b": 2, "c__a": 5, "c__b": 6},
                 {"a": 1, "b": 2, "c__a": 7, "c__b": 8}
             ]
              ==>
            {"a": 1, "b": 2, "c": [
                {"a": 3, "b": 4},  # each_result_row_callback
                {"a": 5, "b": 6},  # each_result_row_callback
                {"a": 7, "b": 8}   # each_result_row_callback
              ]
            }
    :param list_of_dicts: List of dicts. Usually SQL Select result.
    :param use_auto_group_dict: Should be used funtion auto_group_dict for each row of grouped keys into list?
    :param each_result_row_callback: Function could be called for each row result. Row instance will be passed into as function attribute.
    :return: Dict with joined repeated rows and listed dicts with group prefix.
    """
    result = {}
    for item in list_of_dicts:
        grouped_row = {}
        for key, value in item.items():
            parsed_key = re.findall(r"^([a-zA-Z0-9]+)__([^_]+.*)$", key)
            if parsed_key:
                group_key = parsed_key[0][0]
                subgroup_key = parsed_key[0][1]
                if group_key in grouped_row:
                    grouped_row[group_key][subgroup_key] = value
                else:
                    grouped_row[group_key] = {subgroup_key: value}
            else:
                if use_auto_group_dict:
                    result = auto_group_dict({key: value}, merge_with_dict=result)
                else:
                    result[key] = value
        for key, group_line in grouped_row.items():
            if use_auto_group_dict:
                group_line = auto_group_dict(group_line)

            if isinstance(each_result_row_callback, typing.Callable):
                callback_result = each_result_row_callback(group_line)
                group_line = callback_result if isinstance(callback_result, dict) else group_line

            if key in result:
                result[key].append(group_line)
            else:
                result[key] = [group_line]
    return result


def auto_group_list_multi(list_of_dicts: typing.List[dict], use_auto_group_dict: bool = True, each_result_row_callback: typing.Callable = None) -> list:
    """
    It can group items separated by "__" into listed groups. It watches line change.
    If repeating key is changed, new line will of list is created.
    Example:
            [
                {"a": 1, "b": 2, "c__a": 3, "c__b": 4},
                {"a": 1, "b": 2, "c__a": 5, "c__b": 6},
                {"a": 1, "b": 2, "c__a": 7, "c__b": 8},
                {"a": 11, "b": 22, "c__a": 33, "c__b": 44},
                {"a": 11, "b": 22, "c__a": 55, "c__b": 66},
                {"a": 11, "b": 22, "c__a": 77, "c__b": 88},
            ]
            ==>
            [
                #  each_result_row_callback
                {"a": 1, "b": 2, "c":
                    [
                        {"a": 3, "b": 4},
                        {"a": 5, "b": 6},
                        {"a": 7, "b": 8}
                    ]
                },
                #  each_result_row_callback
                {"a": 22, "b": 33, "c":
                    [
                        {"a": 33, "b": 44},
                        {"a": 55, "b": 66},
                        {"a": 77, "b": 88}
                    ]
                }
            ]
    :param list_of_dicts: List of dicts. Usually SQL Select result.
    :param use_auto_group_dict: Should be used funtion auto_group_dict for each row of grouped keys into list?
    :param each_result_row_callback: Function could be called for each row result. Row instance will be passed into as function attribute.
    :return: Dict with joined repeated rows and listed dicts with group prefix.
    """
    results = []
    result_row: dict = {}
    last_row_identifier: list = None
    for item in list_of_dicts:
        row_identifier = []
        new_result_row = {}
        grouped_row = {}
        for key, value in item.items():
            parsed_key = re.findall(r"^([a-zA-Z0-9]+)__([^_]+.*)$", key)
            if parsed_key:
                group_key = parsed_key[0][0]
                subgroup_key = parsed_key[0][1]
                if group_key in grouped_row:
                    grouped_row[group_key][subgroup_key] = value
                else:
                    grouped_row[group_key] = {subgroup_key: value}
            else:
                if use_auto_group_dict:
                    new_result_row = auto_group_dict({key: value}, merge_with_dict=new_result_row)
                else:
                    new_result_row[key] = value
                row_identifier.append(value)

        if last_row_identifier != row_identifier:
            result_row = new_result_row

            if isinstance(each_result_row_callback, typing.Callable):
                callback_result = each_result_row_callback(result_row)
                result_row = callback_result if isinstance(callback_result, dict) else result_row

            results.append(result_row)
            last_row_identifier = row_identifier

        for key, group_line in grouped_row.items():
            if use_auto_group_dict:
                group_line = auto_group_dict(group_line)
            if key in result_row:
                result_row[key].append(group_line)
            else:
                result_row[key] = [group_line]

    return results


def auto_group_dict(dict_structure: dict, merge_with_dict: dict = None) -> dict:
    """
    It can group dict keys with same prefix under one dict key. Group keys are identified by group separator "___"
    Example: {
                "a": 1, "b": 2, "c___a": 3, "c___b___bb": 4, "c___b___cc": 5,
            }
            ===>
            {
                "a": 1, "b": 2, "c": {
                    "a": 3, "b": {
                        "bb": 4, "cc": 5
                    }
                }
            }
    :param dict_structure: Dict wit one level of depth. It ususaly goes from databese row select.
    :param merge_with_dict: Result will be added into this dict
    :return: Dict with posible N level structure
    """

    def set_value(_key_path, _value):
        _result = result
        key_path_len = len(_key_path)
        for index, _key in enumerate(_key_path):
            is_last = index == key_path_len - 1
            if _key not in _result:
                _result[_key] = {}
            if is_last:
                _result[_key] = _value
            _result = _result[_key]

    result = merge_with_dict if merge_with_dict else {}
    for key, value in dict_structure.items():
        key_path = key.split("___")
        if len(key_path) > 1:
            set_value(key_path, value)
        else:
            result[key] = value
    return result
