import json

import pytest

from tasks.models import Task


@pytest.fixture()
def emptytask():
    return Task()


@pytest.fixture()
def validtask():
    t = Task()
    t.title = "Simple task"
    t.statement = "Solve me if u dare"
    t.definition = json.dumps({
        "inputLines": [
            {
                "arguments": [
                    {
                        "type": "int",
                        "value": 7
                    },
                    {
                        "type": "double",
                        "value": 3.14159
                    },
                    {
                        "type": "string",
                        "value": "noway"
                    }
                ]
            },
            {
                "arguments": [
                    {
                        "type": "int",
                        "value": 0
                    },
                    {
                        "type": "double",
                        "value": 0.0
                    },
                    {
                        "type": "string",
                        "value": "zero"
                    }
                ]
            }
        ],

        "outputLines": [
            "Output from inputLine[0]",
            "Output from inputLine[1]"
        ]
    })
    return t
