class Getatr:
    def __init__(self, *args, **kwargs):
        for i, j in enumerate(args, 1):
            setattr(self, f"arg{i}", j)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f"{self.__dict__}"


a = Getatr(1, 2, 3, kw1="qw", kw2=34)
print(a)
