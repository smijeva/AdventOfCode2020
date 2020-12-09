import copy
import re


def load_instructions(file_name):
    with open(file_name) as file:
        instructions = [re.search('^(?P<name>[a-z]{3}) ?(?P<val>[+-]?[0-9]+)$', line)
                        for line in file]
        instructions = [{'name': i['name'], 'val': i['val']} for i in instructions]
        return instructions


def interpret_instructions(instructions):
    """
    Interprets instructions, begins with the first instruction, supports operations nop, jmp, acc, accumulates acc
    operations into a result
    :param instructions: a list of instructions, instruction is a dictionary of "name": instruction_name and
        "val": instruction value
    :return: a pair (acc_result, was_acyclic)
    """
    seen = set()
    pointer = 0
    acc = 0
    while True:
        seen.add(pointer)
        current_instruction = instructions[pointer]
        if current_instruction['name'] == "jmp":
            pointer += int(current_instruction['val'])
        else:
            pointer += 1

        if current_instruction['name'] == "acc":
            acc += int(current_instruction['val'])

        if pointer in seen:
            return acc, False
        if pointer == len(instructions):
            return acc, True


def part1(file_name):
    instructions = load_instructions(file_name)
    res, _ = interpret_instructions(instructions)
    print(res)
    return res


def part2(file_name):
    instructions = load_instructions(file_name)
    nop_ixes = [i for i, instr in enumerate(instructions) if instr["name"] == "nop"]
    for nop_ix in nop_ixes:
        instructions_cpy = copy.deepcopy(instructions)
        instructions_cpy[nop_ix]["name"] = "jmp"
        res, acyclic = interpret_instructions(instructions_cpy)
        if acyclic:
            print(res)
            return res

    jmp_ixes = [i for i, instr in enumerate(instructions) if instr["name"] == "jmp"]
    for jmp_ix in jmp_ixes:
        instructions_cpy = copy.deepcopy(instructions)
        instructions_cpy[jmp_ix]["name"] = "nop"
        res, acyclic = interpret_instructions(instructions_cpy)
        if acyclic:
            print(res)
            return res

    return 0


part1("input8.txt")
part2("input8.txt")


def test_part1():
    assert part1("input8_test1.txt") == 5


def test_part2():
    assert part2("input8_test1.txt") == 8
