from dataclasses import dataclass


@dataclass
class Month:
    year: int
    month: int

    def __str__(self):
        return '{self.year}-{self.month}'.format(self=self)

    def __repr__(self):
        return 'Month({self.year}, {self.month})'.format(self=self)
