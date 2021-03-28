class Evaluation(object):
    def __init__(self, flavors, items):
        self._flavors = flavors
        self._items = items

    def evaluate(self, f, i, j):
        lhs = self._items[i]
        rhs = self._items[j]
        op = self._flavors[f]
        question = f'Ist {lhs!r} mehr {op} als {rhs!r} [j/n]? '

        while True:
            response = input(question)
            response = response.strip().lower()
            if response == 'j':
                return i, j
            if response == 'n':
                return j, i
