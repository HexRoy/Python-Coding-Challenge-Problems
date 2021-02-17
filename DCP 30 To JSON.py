# Problem
# =====================================================================================================================
# Write a function that takes in a number, string, list, or dictionary and returns its JSON encoding.
# It should also handle nulls.
# For example, given the following input:
# [None, 123, ["a", "b"], {"c":"d"}]
# You should return the following, as a string:
# '[null, 123, ["a", "b"], {"c": "d"}]'


# Solution
# =====================================================================================================================
import json


def to_json(n):
    """
    to_json: Converts list of number, string, list, or dictionary to json format
    :param n: (list) can contain number, string, list, or dictionary
    :return: (string) in json format
    """
    return json.dumps(n)


# Input
# =====================================================================================================================
print(to_json([None, 123, ["a", "b"], {"c":"d"}]))
print(type(to_json([None, 123, ["a", "b"], {"c":"d"}])))