gravity_assist_program = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 2, 19, 9, 23, 1, 23, 5, 27, 2, 6, 27, 31, 1, 31, 5, 35, 1, 35, 5, 39, 2, 39, 6, 43, 2, 43, 10, 47, 1, 47, 6, 51, 1, 51, 6, 55, 2, 55, 6, 59, 1, 10, 59, 63, 1, 5, 63, 67, 2, 10, 67, 71, 1, 6, 71, 75, 1, 5, 75, 79, 1, 10,
                          79, 83, 2, 83, 10, 87, 1, 87, 9, 91, 1, 91, 10, 95, 2, 6, 95, 99, 1, 5, 99, 103, 1, 103, 13, 107, 1, 107, 10, 111, 2, 9, 111, 115, 1, 115, 6, 119, 2, 13, 119, 123, 1, 123, 6, 127, 1, 5, 127, 131, 2, 6, 131, 135, 2, 6, 135, 139, 1, 139, 5, 143, 1, 143, 10, 147, 1, 147, 2, 151, 1, 151, 13, 0, 99, 2, 0, 14, 0]


def integer_prog_computer(tape):

    ops_processed = 0

    def get_next_op():
        nonlocal ops_processed
        next_op = tape[ops_processed*4:ops_processed*4+4]
        ops_processed += 1
        return next_op

    def process_op(op):
        op_code = op[0]
        if op_code == 1:
            tape[op[3]] = tape[op[1]] + tape[op[2]]
        elif op_code == 2:
            tape[op[3]] = tape[op[1]] * tape[op[2]]
        elif op_code == 99:
            return "Halting"
        else:
            print("Invalid Op Code")
            raise

    while process_op(get_next_op()) != "Halting":
        continue

    return tape


if __name__ == "__main__":
    # restore to 1202 alarm

    gravity_assist_program[1] = 12
    gravity_assist_program[2] = 2

    # run

    print(integer_prog_computer(gravity_assist_program)[0])
