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


def ask_wish_continue():
    answer = input('Continue? (y/n)\n')
    return answer.lower() == 'y'
