class FieldDesc:
    def __init__(self, required=False):
        self.required = required

    def __repr__(self):
        return f'{self.required}'

    def bare(self):
        return self.required