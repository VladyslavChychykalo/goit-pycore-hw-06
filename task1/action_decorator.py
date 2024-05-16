# import sys


def action_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            print(f"Record with name '{args[1]}' not found")
            raise e
        except ValueError as e:
            # print(e)
            raise e

    return inner
