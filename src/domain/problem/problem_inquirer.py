from datetime import datetime
from src.domain.problem.problem_types import ProblemType


def get_categories():
    category = ProblemType.STACKS

    return [category.value[0]]


def obtain_problem_input_data():
    description = input('Description:\n')
    summary = input('Summary:\n')
    problem = {
        "description": description,
        "summary": summary,
        "created_at": datetime.utcnow().isoformat(),
        "categories": get_categories()
    }
    return problem


def ask_action():
    options = {
        'p': ['Consider positive', 'positive'],
        'f': ['Consider failure', 'failure'],
        's': ['Skip', 'skip'],
        'b': ['Break execution', 'break']
    }
    print('What is your action?')
    for option in options:
        print(f"- ({option}) {options[option][0]}")
    answer = input('Answer:')

    if answer.lower() not in options:
        print(f"Invalid option provided ({answer.lower()}). Repeating question\n")
        return 'repeat'

    return options[answer][1]
