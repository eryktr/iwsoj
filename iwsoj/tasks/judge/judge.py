import json

from tasks.models import Task
from typing import List


def judge(task: Task, output: List[str]) -> bool:
    expected_out = json.loads(task.definition)['outputLines']
    return output == expected_out
