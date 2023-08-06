class ObjectView:
    def __init__(self, **entries):
        self.__dict__.update(entries)
