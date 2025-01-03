from src.client.data import get_data, save_data
from src.domain.problem.problem_validator import validate_problem
import uuid
from datetime import datetime


def get_problems():
    return get_data()


def get_sorted_problems():
    problems = get_problems()
    problems.sort(key=lambda x: datetime.fromisoformat(x["created_at"]), reverse=True)
    return problems


def update_problems(data):
    save_data(data)


def save(problem_object):
    validate_problem(problem_object)
    if "id" not in problem_object:
        problem_object["id"] = str(uuid.uuid4())
    data = get_problems()
    data.append(problem_object)
    update_problems(data)
