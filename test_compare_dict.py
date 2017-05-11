import pytest
import json
from comparator import compare_two_dicts_by_criteria

with open('test_data/one.json') as f:
    fist_json = json.load(f)

with open('test_data/two.json') as f:
    second_json = json.load(f)

with open('test_data/three.json') as f:
    third_json = json.load(f)

with open('test_data/four.json') as f:
    firth_json = json.load(f)

test_data = [
    (fist_json, second_json, True),
    (fist_json, third_json, False),
    (firth_json, third_json, True),
]


@pytest.mark.parametrize("first_dict,second_dict,same", test_data)
def test(first_dict, second_dict, same):
    result = compare_two_dicts_by_criteria(first_dict, second_dict)
    assert result == same
