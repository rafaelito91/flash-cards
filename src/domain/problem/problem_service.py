from src.domain.problem.problem_inquirer import obtain_problem_input_data, ask_wish_continue
from src.domain.problem.problem_repository import save, get_problems, update_problems, get_sorted_problems
from datetime import datetime
from src.domain.problem.problem_types import ProblemType


def save_problem():
    problem = obtain_problem_input_data()
    save(problem)


def save_problem_example():
    category = ProblemType.STACKS
    problem = {
        "description": "Example problem",
        "summary": "basically you need to know how to check duplicates in a the data structure XPTO",
        "created_at": datetime.utcnow().isoformat(),
        "categories": [category.value[0]]
    }
    save(problem)


def remove_last():
    problems = get_problems()
    problems.pop()
    update_problems(problems)


def list_problems():
    problems = get_sorted_problems()
    for problem in problems:
        print(problem)


def remove_by_id():
    id = input('Whats the id?\n')
    problems = get_problems()
    index = next((i for i, p in enumerate(problems) if p["id"] == id), None)
    problems.pop(index)
    update_problems(problems)


def execute_problems():
    problems = get_sorted_problems()
    if not problems:
        print('Empty problem list!')
        return

    print('\n### Training Session Starting ###\n')
    answered_count = 0
    for index, problem in enumerate(problems):
        position = index + 1
        print('Problem: ' + str(position) + '/' + str(len(problems)))
        print('Description: ' + problem['description'])
        print('Summary:' + problem['summary'])
        wish_continue = ask_wish_continue()
        if not wish_continue:
            break
        answered_count += 1

    if answered_count == len(problems):
        print('\n### Training Session Completed!! ###\n')
    else:
        print('\n### TRAINING SESSION INTERRUPTED ###\n')
        remaining_questions = len(problems) - answered_count
        print(str(remaining_questions) + ' questions remaining')


