class Flavometer(object):
    def __init__(self, sampling, evaluation, ranking):
        self._sampling = sampling
        self._evaluation = evaluation
        self._ranking = ranking

    def update(self, state):
        from copy import deepcopy
        state = deepcopy(state)
        f = self._sampling.sample_flavor()
        ranks = self._ranking.rank(state.scores[f])
        i, j = self._sampling.sample_items(ranks)
        i, j = self._evaluation.evaluate(f, i, j)
        state.scores[f].append((i, j))
        return state, f
