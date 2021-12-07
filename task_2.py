import functools
import string


@functools.total_ordering
class Version:
    dict_replace = {
        'alpha': '0',
        'beta': '1',
        'rc': '2',
        'b': '1',
        'a': '0'
    }

    def __init__(self, version):
        self.version = version
        self.version_digit, self.version_letter = self.divide_version_digit_letter(version)

    @staticmethod
    def numeric_replace_part_digit_letter(value: list[str]) -> list[int]:
        """ The letter part replaces to digital. Return List integer  """

        len_value = len(value)
        for num in range(len_value):
            if value[num] in Version.dict_replace:
                value[num] = Version.dict_replace[value[num]]
        return [int(number) for number in value]

    def divide_version_digit_letter(self, version):
        """ Divide version into numeric and alphabetic parts """

        symbol = string.ascii_lowercase + string.ascii_uppercase + "-"
        part_digit = None
        part_letter = None
        if not version.replace(".", '').strip().isdigit():
            for element in version:
                if element in symbol:
                    index = version.find(element)
                    part_digit = (version[0: index]).strip().split('.')
                    part_letter = (version[index:].lstrip('-')).strip().split('.')
                    break
        else:
            part_digit = version.split('.')
            part_letter = [0]

        numeric_digit = self.numeric_replace_part_digit_letter(part_digit)
        numeric_letter = self.numeric_replace_part_digit_letter(part_letter)
        return numeric_digit, numeric_letter

    def __eq__(self, other):
        if self.version_digit == other.version_digit:
            if self.version_letter == other.version_letter:
                return True
        return False

    def __lt__(self, other):
        if self.version_letter < other.version_letter:
            if self.version_letter < other.version_letter:
                return True
            else:
                return False
        else:
            return self.version_digit < other.version_digit


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), f"le failed {version_1}"
        assert Version(version_2) > Version(version_1), f"ge failed {version_1}"
        assert Version(version_2) != Version(version_1), f"neq failed {version_1}"

    print(Version('1.1.3') < Version('2.2.3'))
    print(Version('1.3.0') > Version('0.3.0'))
    print(Version('0.3.0b') < Version('1.2.42'))
    print(Version('1.3.42') == Version('42.3.1'))


if __name__ == "__main__":
    main()
