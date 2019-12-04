import os

from docker.errors import ContainerError

from submissions.status import Status
from submissions.language import Language
from tasks.judge.judge import judge
from runner.runner import soSorryYouLose


def validate_code(source_code, language_name, task):
    """
    :param source_code: the code which is a solution of the task by a user
    :param language_name: the name of the programming language of the task
    :param task: selected task by a user

    :return: `Status <../html/submissions.html#submissions-status-module>`_
    """
    language = Language.from_string(language_name)
    lang_suffix = "." + language.get_suffix()

    try:
        code_file = create_tmp_file("sourceCode" + lang_suffix, source_code)
        input_public_file = create_tmp_file("input0.txt", task.input_public)
        input_hidden_file = create_tmp_file("tnput1.txt", task.input_hidden)
        output = soSorryYouLose(code_file, input_public_file, input_hidden_file)
    except MemoryError:
        return Status.MLE,
    except TimeoutError:
        return Status.TLE,
    except ContainerError as err:
        return Status.CE, err.stderr.decode("utf-8")
    finally:
        os.remove(code_file)
        os.remove(input_public_file)
        os.remove(input_hidden_file)

    out = output.split("__SPLIT_PLACEHOLDER__\n")
    ok = judge(task.output_public, out[0])
    if not ok:
        return Status.WA, \
               "on test:\n" + \
               task.input_public + \
               "\nExpected output:\n" + \
               task.output_public + \
               "\ngot:\n" + \
               out[0]

    ok = judge(task.output_hidden, out[1])
    if ok:
        return Status.OK,
    else:
        return Status.WA, "on hidden tests"


def create_tmp_file(name, input):
    """
    :param name: name of the file or input 
    :param input: content of the file or input

    :return: the path to created temporary file
    """
    tmp_dir = os.path.join(os.getcwd(), "tmp")
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    path = os.path.join(tmp_dir, name)
    code_file = open(path, "w")
    code_file.write(input)
    code_file.close()
    return path
