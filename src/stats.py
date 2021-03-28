class Stats(object):
    def __init__(self, ranking):
        self._ranking = ranking

    def log(self, state, f):
        ranks = self._ranking.rank(state.scores[f])
        indexes = list(range(len(state.items)))
        indexes = sorted(indexes, key=lambda k: ranks[k])
        flavor = state.flavors[f]

        print()
        print(f'Ranking für {flavor!r} von wenig nach viel:')
        for i in indexes:
            item = state.items[i]
            rank = ranks[i]
            print(f'    {item} ({rank:.3})')
        print()
