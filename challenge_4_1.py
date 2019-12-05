input_range = range(240298, 784957)


def test_criteria(num):

    digits = list(str(num))

    def no_decrease(): return digits == sorted(digits)

    def not_all_unique(): return len(set(digits)) != len(digits)

    return no_decrease() and not_all_unique()


if __name__ == '__main__':

    print(test_criteria(111111))

    print(len([x for x in input_range if test_criteria(x)]))
