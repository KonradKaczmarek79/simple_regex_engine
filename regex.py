class RegularExpression:
    """ A class to represent a regular expression

    Attributes:
        BEGINNING: a symbol specifying the required starting character of the text
        ENDING: a symbol specifying the required ending character of the text
    """

    BEGINNING = "^"
    ENDING = "$"

    def __init__(self, pattern, text_to_check):
        self.pattern = pattern
        self.text_to_check = text_to_check


    def same_text_or_blank(self):
        return (len(self.pattern) == len(self.text_to_check)) \
            and self.pattern == self.text_to_check \
            or (len(self.pattern) == 0)


    @staticmethod
    def check_single_sign(sign_re, sign_text):

        points_to_check = (
            (sign_re == sign_text),
            (sign_re == ".")
        )

        return any(points_to_check)


    def check_beginning(self):
        if self.pattern.startswith(self.BEGINNING) and len(self.pattern) > 1:
            if check_single_sign(self.pattern[1], self.text_to_check[0]):
                self.pattern = self.pattern[2:]
                self.text_to_check = self.text_to_check[1:]


    def check_ending(self):
        if self.pattern.endswith(self.ENDING) and len(self.pattern) > 1:
            if check_single_sign(self.pattern[-2], self.text_to_check[-1]):
                self.pattern = self.pattern[:-2]
                self.text_to_check = self.text_to_check[:-1]


    def compare_with_pattern(self):
        result = []

        self.check_beginning()
        self.check_ending()

        # check if the same text or no pattern passed
        if self.same_text_or_blank():
            result.append(True)

        # check if pattern is substring of text to check
        elif len(self.pattern) < len(self.text_to_check):
            start_point = 0
            end_point = len(self.pattern)
            while end_point <= len(self.text_to_check):
                result = []
                for re_letter, txt_letter in zip(self.pattern, self.text_to_check[start_point:end_point]):
                    result.append(RegularExpression.check_single_sign(re_letter, txt_letter))
                if all(result):
                    return True

                start_point += 1
                end_point += 1
        else:
            try:
                for re_letter, txt_letter in zip(self.pattern, self.text_to_check, strict=True):
                    result.append(RegularExpression.check_single_sign(re_letter, txt_letter))
            except ValueError:
                result.append(False)
        return all(result)
