from src.domain.problem.problem_inquirer import ask_wish_continue
from src.domain.problem.problem_repository import get_sorted_problems


def describe_problem(position, problem, problems):
    print('Problem: ' + str(position) + '/' + str(len(problems)))
    print('Description: ' + problem['description'])
    print('Summary:' + problem['summary'])


def execute_problems():
    problems = get_sorted_problems()
    if not problems:
        print('Empty problem list!')
        return

    print('\n### Training Session Starting ###\n')
    answered_count = 0
    for index, problem in enumerate(problems):
        position = index + 1
        describe_problem(position, problem, problems)

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
