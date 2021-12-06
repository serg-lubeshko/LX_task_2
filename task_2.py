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
    dict_rep = {
        'alpha': '0',
        'beta': '1',
        'rc': '2',
        'b': '1',
        'a': '0'
    }

    def __init__(self, version):
        self.version = self.replace_version(version)
        # self.digital = None

    def split_num_with_letter(self, value):

        split_value = list(value)
        for index, item in enumerate(split_value):
            if item in Version.dict_rep:
                split_value[index] = Version.dict_rep[item]
        return split_value

    def replace_version(self, version):
        # dict_rep = {
        #     'alpha': '0',
        #     'beta': '1',
        #     'rc': '2',
        #     'b': '1',
        #     'a': '0'
        # }
        versions_replace_split = version.replace("-", ".").strip().split('.')
        # print(versions_replace_split)

        len_vesion_new = len(versions_replace_split)
        for num in range(len_vesion_new):
            if versions_replace_split[num] in Version.dict_rep:
                versions_replace_split[num] = Version.dict_rep[versions_replace_split[num]]
            elif not versions_replace_split[num].isdigit():

                a = self.split_num_with_letter(versions_replace_split.pop(num))
                versions_replace_split.extend(a)

                print(a)
        c=[int(i) for i in versions_replace_split]
        return c
    # def __ge__(self, other):
    #     print(self.version, '----', other.version)
    #     if self.version > other.version:
    #         return True
    #     else:
    #         return False

    def __lt__(self, other):
        print(' __lt__ called')
        print(self.version, '----', other.version)
        if self.version < other.version:
            return True
        else:
            return False
        # len_self_version = self.version
        # len_other_version = other.version
        # len_version = min(len_self_version, len_other_version)
        # for i in range(len_version):
        #     if self.version[i] < self.version[i]

    def __eq__(self, other):
        # if not self._is_valid_operand(other):
        #     return NotImplemented
        print(' __eq__ called')
        print(self.version, '----', other.version)
        return self.version == other.version


def main():
    to_test = [
        # ("1.0.0", "2.0.0"),
        # ("1.0.0", "1.42.0"),
        # ("1.2.0", "1.2.42"),
        # ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        # ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"
    # a = Version("1.1.0-alpha")
    # b = Version("1.0.0-rc.1 ")
    # c = Version("1.0.10-alpha.beta ")
    # d = Version("1.0.0-rc.1")
    # dd = Version("1.0.0-rc.2")
    # print(d != dd)
    # print(a.replace_version())
    # print(b.replace_version())
    # print(c.replace_version())


if __name__ == "__main__":
    main()
