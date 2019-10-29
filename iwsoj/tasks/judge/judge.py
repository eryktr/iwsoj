import json
from typing import List

from tasks.models import Task


def judge(task: Task, output: str) -> bool:
    expected_out = task.output
    output = output.strip()
    return output == expected_out
