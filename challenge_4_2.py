from challenge_4_1 import input_range, test_criteria
from collections import Counter


def more_criteria(num):
    return 2 in Counter(str(num)).values()


if __name__ == '__main__':

    print(len([x for x in input_range if test_criteria(x) and more_criteria(x)]))
