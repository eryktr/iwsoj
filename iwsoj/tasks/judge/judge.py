import json
from typing import List

from tasks.models import Task


def judge(task: Task, output: List[str]) -> bool:
    expected_out = json.loads(task.definition)['outputLines']
    return output == expected_out
