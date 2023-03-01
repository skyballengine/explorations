import functools
import json


def json_print(func):
    """Adds pretty printing of JSON object"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(json.dumps(result, indent=4))
        return result

    return wrapper


@json_print
def generate_json():
    example = {"squadname": "yes", "billy": "asdrffgasd"}
    with open("example.json", "w") as outfile:
        json.dump(example, outfile)
    return example


generate_json()
