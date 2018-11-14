import re
import random
from marks import marks


def analyze():
    lab_marks = 0
    module_marks = 0
    for key in marks:
        if re.match(r'(lab)', key):
            lab_marks += marks[key]
        elif re.match(r'(module)', key):
            module_marks += marks[key]
    exam_mark = 0
    if lab_marks == 40:
        exam_mark += 30
    elif 32 <= lab_marks < 40:
        exam_mark += 30 * random.uniform(0.9, 1)
    elif 24 <= lab_marks < 32:
        exam_mark += 30 * random.uniform(0.7, 1)
    else:
        exam_mark += 30 * random.uniform(0.6, 1)

    if module_marks == 20:
        exam_mark += 10
    elif 16 <= module_marks < 20:
        exam_mark += 10 * random.uniform(0.95, 1)
    elif 12 <= module_marks < 16:
        exam_mark += 10 * random.uniform(0.8, 1)
    elif 8 <= module_marks < 12:
        exam_mark += 10 * random.uniform(0.7, 1)
    else:
        exam_mark += 10 * random.uniform(0.6, 1)

    exam_mark = int(exam_mark)
    print('Expected exam mark', exam_mark)
    return exam_mark + lab_marks + module_marks


if __name__ == '__main__':
    print('Table of marks:\n'
          '0-59 - Fx\n'
          '60-64 - E\n'
          '65-74 - D\n'
          '75-84 - C\n'
          '85-94 - B\n'
          '95-100 - A\n')
    print('Predicted mark: ', analyze())
