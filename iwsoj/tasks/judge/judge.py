import json
from typing import List

from tasks.models import Task


def judge(task: Task, output: str) -> bool:
    """
    :param task: model of the select task
    :param output: output value of the task
    
    :return: **true** or **false** (if output and expected_out are equal or not) 
    """
    expected_out = task.output
    output = output.strip()
    return output == expected_out
