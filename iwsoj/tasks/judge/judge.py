import json
from typing import List

from tasks.models import Task


def judge(expected_out: str, output: str) -> bool:
    """
    :param expected_out: expected output value of the task
    :param output: output value of the task
    
    :return: **true** or **false** (if output and expected_out are equal or not) 
    """
    output = output.strip()
    return output == expected_out
