class Version:
    """
    1.1.0-alpha       >>>      1.1. 0.0
    1.2.0-alpha.1     >>>      1.2. 0.0.1
    1.0.1b            >>>      1.0. 1.1
    1.0.10-alpha.beta >>>      1.0.10.0.1
    1.0.0-rc.1        >>>      1.0. 0.2.1
    0.3.0b            >>>      0.3. 0.1
    0.3.0b4           >>>      0.3. 0.1.4???????
    """
    def __init__(self, version):
        self.version = version

    def replace_version(self):
        dict_rep = {
            'alpha':'0',
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
            # elif versions_replace_split[num]
        print(versions_replace_split)
            


def main():
    to_test = [
        # ("1.0.0", "2.0.0"),
        # ("1.0.0", "1.42.0"),
        # ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        # ("1.0.1b", "1.0.10-alpha.beta"),
        # ("1.0.0-rc.1", "1.0.0"),
    ]

    # for version_1, version_2 in to_test:
    #     assert Version(version_1) < Version(version_2), "le failed"
    #     assert Version(version_2) > Version(version_1), "ge failed"
    #     assert Version(version_2) != Version(version_1), "neq failed"
    a= Version("1.1.0-alpha")
    b= Version("1.0.0-rc.1 ")
    c= Version("1.0.10-alpha.beta ")
    d= Version("1.0.1b")
    print(a.replace_version())
    print(b.replace_version())
    print(c.replace_version())
    print(d.replace_version())

if __name__ == "__main__":
    main()
