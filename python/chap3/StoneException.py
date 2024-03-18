
class StoneException(RuntimeError):
    def __init__(self, m):
        super().__init__(m)
