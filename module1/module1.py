from datetime import datetime

class Print():
    def __init__(self) -> None:
        self.date = datetime.today()
        self.year = self.date.year
        self.month = self.date.month
        self.day = self.date.day

    def do(self) -> None:
        print('{} {} {}'.format(self.year, self.month, self.day))