class Sampling(object):
    def __init__(self, num_flavors, num_items):
        self._num_flavors = num_flavors
        self._num_items = num_items

    def sample_flavor(self):
        from random import randrange
        return randrange(self._num_flavors)

    def sample_items(self, ranks):
        from random import choice, gauss, randrange
        i = randrange(1, self._num_items - 1)
        d = 1 + abs(gauss(0.0, 0.2 * self._num_items))
        j = round(i + choice((-d, d)))
        j = min(max(j, 0), self._num_items - 1)

        indexes = list(range(self._num_items))
        indexes = sorted(indexes, key=lambda k: ranks[k])
        return indexes[i], indexes[j]
