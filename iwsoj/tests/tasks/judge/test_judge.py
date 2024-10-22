from tasks.judge.judge import judge


def test_judge_ok_solution(validtask):
    print(validtask)
    output = "OutputLine[0]\nOutputLine[1]"
    assert judge(validtask.output_hidden, output)


def test_judge_wrong_solution(validtask):
    output = "fundamentally\nwrong"
    assert not judge(validtask.output_hidden, output)
