class MyString(str):
    def lower(self):
        return super().lower() + "!"

    def count_words(self):
        return len(self.split())

    def replace(self, old, new, maxreplace=-1):
        upper_str = super().upper()
        return super(MyString, MyString(upper_str)).replace(old, new, maxreplace)

    def __add__(self, other):
        if isinstance(other, MyString):
            return MyString(super().__add__(" " + other))
        return NotImplemented

    def __mul__(self, times):
        if isinstance(times, int):
            return MyString((self + "-") * (times - 1) + self)
        return NotImplemented
