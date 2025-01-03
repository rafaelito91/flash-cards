from src.domain.problem.problem_inquirer import ask_action
from src.domain.problem.problem_repository import get_sorted_problems


def _describe_problem(position, problem, problems):
    print('Problem: ' + str(position) + '/' + str(len(problems)))
    print('Description: ' + problem['description'])
    print('Summary:' + problem['summary'])


def _conclusion_message(answered_count, problems):
    if answered_count == len(problems):
        print('\n### Training Session Completed!! ###\n')
    else:
        print('\n### TRAINING SESSION INCOMPLETE DUE TO BREAKS OR SKIPS ###\n')
        remaining_questions = len(problems) - answered_count
        print(str(remaining_questions) + ' questions remaining')


def execute_problems():
    problems = get_sorted_problems()
    if not problems:
        print('Empty problem list!')
        return

    print('\n### Training Session Starting ###\n')
    answered_count = 0
    index = 0
    while index < len(problems):
        problem = problems[index]
        position = index + 1
        _describe_problem(position, problem, problems)

        action = ask_action()
        if action == 'positive':
            answered_count += 1
            index += 1
        elif action == 'negative':
            answered_count += 1
            index += 1
        elif action == 'repeat':
            pass
        elif action == 'skip':
            index += 1
        elif action == 'break':
            break
        else:
            raise Exception(f"Problem mapping desired action: {action}")

    _conclusion_message(answered_count, problems)
