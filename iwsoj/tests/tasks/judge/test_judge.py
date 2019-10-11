from tasks.judge.judge import judge


def test_judge_ok_solution(validtask):
    print(validtask)
    output = ["Output from inputLine[0]", "Output from inputLine[1]"]
    assert judge(validtask, output)


def test_judge_wrong_solution(validtask):
    output = ["fundamentally", "wrong"]
    assert not judge(validtask, output)
