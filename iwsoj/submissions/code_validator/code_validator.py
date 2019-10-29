import os

from docker.errors import ContainerError

from submissions.status import Status
from submissions.language import Language
from tasks.judge.judge import judge
from runner.runner import soSorryYouLose


def validate_code(sourceCode, language_name, task):
    language = Language.from_string(language_name)
    lang_suffix = "." + language.get_suffix()

    try:
        code_file = create_tmp_file("sourceCode" + lang_suffix, sourceCode)
        input_file = create_tmp_file("input.txt", task.input)
        output = soSorryYouLose(code_file, input_file)
    except ContainerError as err:
        return Status.CE, err.stderr.decode("utf-8")
    finally:
        os.remove(code_file)
        os.remove(input_file)

    print('code output ' + output)
    ok = judge(task, output)
    if ok:
        return Status.OK,
    else:
        return Status.WA,

def create_tmp_file(name, input):
    tmp_dir = os.path.join(os.getcwd(), "tmp")
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    path = os.path.join(tmp_dir, name)
    code_file = open(path, "w")
    code_file.write(input)
    code_file.close()
    return path