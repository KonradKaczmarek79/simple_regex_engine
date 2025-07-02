"""The task requires that not to use the re module for completing this project. """

def check_single_sing(regular_expression: str, text: str) -> bool:
    """
    Check if a regular expression matches a single singular string.
    :param regular_expression: The regular expression to check (dot, blank or the same character).
    :param text: The text to check.
    :return: True if the regular expression matches a single singular string, the . matches single char.
    Blank means no expression to check so return True.
    False otherwise.
    """
    points_to_check = (
        (regular_expression == text) and (len(regular_expression) == len(text)),
        (len(regular_expression) == 0),
        (regular_expression == ".")
    )
    return any(points_to_check)

try:
    regex, text_to_check = input().split("|")
except ValueError:
    pass
else:
    print(check_single_sing(regex, text_to_check))