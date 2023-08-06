# --------------------------------------------------
# Any
# --------------------------------------------------
class Any:
    # def hide__new__(cls, *args, **kw):
    # instance = super(Any, cls).__new__(cls, *args, **kw)
    # return instance

    def __init__(self, *args, **kw):
        init = super().__init__
        try:
            init(*args, **kw)
        except Exception:
            init()

