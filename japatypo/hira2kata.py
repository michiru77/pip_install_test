from datetime import datetime

class get():
    def __init__(self) -> None:
        self.date = datetime.today()
        self.year = self.date.year
        self.month = self.date.month
        self.day = self.date.day

    def do(self) -> str:
        return '{} {} {}'.format(self.year, self.month, self.day)