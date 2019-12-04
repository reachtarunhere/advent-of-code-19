from challenge_2_1 import gravity_assist_program, integer_prog_computer


def run_comp_with_inputs(noun, verb):
    tape = gravity_assist_program[:]
    tape[1], tape[2] = noun, verb
    return integer_prog_computer(tape)[0]


for noun in range(100):
    for verb in range(100):
        try:
            if run_comp_with_inputs(noun, verb) == 19690720:
                print(noun, verb)
        except:
            continue
