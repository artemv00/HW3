import math


def minimum(arr: list):
    if arr:
        min_num = arr[0]
        for i in arr:
            if i < min_num:
                min_num = i
    else:
        min_num = None

    return min_num


def maximum(arr: list):
    if arr:
        max_num = arr[0]
        for i in arr:
            if i > max_num:
                max_num = i
    else:
        max_num = None

    return max_num


def addition(arr: list):
    if arr:
        addition_num = 0
        for i in arr:
            addition_num += i
    else:
        addition_num = None

    return addition_num


def multiplication(arr: list):
    if arr:
        multiplication_num = 1
        for i in arr:
            try:
                multiplication_num *= i
            except OverflowError:
                multiplication_num = math.inf
    else:
        multiplication_num = None

    return multiplication_num


def file_reader(file: str):

    a_list = []

    with open(file, 'r') as f:
        for line in f:
            a_list = line.split()
            a_list = list(map(int, a_list))
    return a_list


def body(file):

    a_file = file_reader(file=file)

    minn = minimum(a_file)
    maxx = maximum(a_file)
    addit = addition(a_file)
    mult = multiplication(a_file)

    return {'minn': minn, 'maxx': maxx, 'addit': addit, 'mult': mult}


filename = 'numbers.txt'

output = body(file=filename)

print(
    'Minimal:', output['minn'],
    '\nMaximal:', output['maxx'],
    '\nAdding:', output['addit'],
    '\nMultiplication:', output['mult']
)
