def exclude_dict_empty_values(dictionary: dict):
    """
    빈 문자열 또는 None 값을 가진 key를 dict에서 제거
    """
    return {k: v for k, v in dictionary.items() if v != "" and v is not None}


def split_elements_per_unit(values: list, unit: int, remove_none=True):
    """
    주어진 리스트를 unit 갯수에 맞게 잘라 리스트로 삽입
    ie. ['a','b','c','d'] 를 unit 3을 적용 -> [['a','b','c'], ['d', None, None, None]]
    remove 옵션 적용시 None 은 제거됨.
    """
    total_length = len(values)
    extended_list = (
        values + [None] * (unit - (total_length % unit))
        if total_length % unit != 0
        else values
    )
    if remove_none:
        return [
            list(filter(bool, extended_list[i : i + unit]))
            for i in range(0, len(extended_list), unit)
        ]
    return [extended_list[i : i + unit] for i in range(0, len(extended_list), unit)]
