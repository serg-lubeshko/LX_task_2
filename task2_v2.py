import functools


@functools.total_ordering
class Version:
    dict_rep = {
        'alpha': '0',
        'beta': '1',
        'rc': '2',
        'b': '1',
        'a': '0'
    }

    def __init__(self, version):
        self.version = version
        self.digital = None
        self.sumbol = None

    def get_digital_part(self):
        digital_part = self.version
