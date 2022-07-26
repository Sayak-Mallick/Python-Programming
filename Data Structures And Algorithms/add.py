from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

def add_variables(a ,b):
    result = a+b
    return result


test = {
    'input': {
        'a': 4,
        'b': 7
    },
    'output': 11
}

tests = []
tests.append(test)

tests.append({
    'input': {
        'a': 13,
        'b': 1
    },
    'output': 14
})

tests.append({
    'input': {
        'a': 4,
        'b': 4
    },
    'output': 8
})

tests.append({
    'input': {
        'a': 3,
        'b': 127
    },
    'output': 130
})


print(evaluate_test_case(add_variables, test))
print(evaluate_test_cases(add_variables, tests))