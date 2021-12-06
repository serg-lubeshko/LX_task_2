import functools


@functools.total_ordering
class Version:
    """
    1.1.0-alpha       >>>      1.1. 0.0
    1.2.0-alpha.1     >>>      1.2. 0.0.1
    1.0.1b            >>>      1.0. 1.1
    1.0.10-alpha.beta >>>      1.0.10.0.1
    1.0.0-rc.1        >>>      1.0. 0.2.1
    0.3.0b            >>>      0.3. 0.1
    0.3.0b4           >>>      0.3. 0.1.4???????

    @functools.total_ordering
    Given a class defining one or more rich comparison ordering methods, this class decorator supplies the rest.
    This simplifies the effort involved in specifying all of the possible rich comparison operations:
    The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). In addition, the class should supply
    an __eq__() method

    """

    def __init__(self, version):
        self.version = version

    def split_num_with_letter(self, value):
        dict_rep = {
            'alpha': '0',
            'beta': '1',
            'rc': '2',
            'b': '1',
            'a': '0'
        }
        split_value = list(value)
        for index, item in enumerate(split_value):
            if item in dict_rep:
                split_value[index] = dict_rep[item]
        return split_value

    def replace_version(self):
        dict_rep = {
            'alpha': '0',
            'beta': '1',
            'rc': '2',
            'b': '1',
            'a': '0'
        }
        versions_replace_split = self.version.replace("-", ".").strip().split('.')
        print(versions_replace_split)

        len_vesion_new = len(versions_replace_split)
        for num in range(len_vesion_new):
            if versions_replace_split[num] in dict_rep:
                versions_replace_split[num] = dict_rep[versions_replace_split[num]]
            elif not versions_replace_split[num].isdigit():
                a = self.split_num_with_letter(versions_replace_split.pop(num))
                versions_replace_split.extend(a)
                print(a)
        print(versions_replace_split)

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        # if not self._is_valid_operand(other):
        #     return NotImplemented
        print(' __eq__ called')
        return self.version == other.version

def main():
    to_test = [
        # ("1.0.0", "2.0.0"),
        # ("1.0.0", "1.42.0"),
        # ("1.2.0", "1.2.42"),
        # ("1.1.0-alpha", "1.2.0-alpha.1"),
        # ("1.0.1b", "1.0.10-alpha.beta"),
        # ("1.0.0-rc.1", "1.0.0"),
    ]

    # for version_1, version_2 in to_test:
    #     assert Version(version_1) < Version(version_2), "le failed"
    #     assert Version(version_2) > Version(version_1), "ge failed"
    #     assert Version(version_2) != Version(version_1), "neq failed"
    # a = Version("1.1.0-alpha")
    # b = Version("1.0.0-rc.1 ")
    # c = Version("1.0.10-alpha.beta ")
    d = Version("1.0.0-rc.1")
    dd = Version("1.0.0-rc.2")
    print(d==dd)
    # print(a.replace_version())
    # print(b.replace_version())
    # print(c.replace_version())
    print(d.replace_version())


if __name__ == "__main__":
    main()
