class Ranking(object):
    def __init__(self, num_items, num_iterations):
        self._num_items = num_items
        self._num_iterations = num_iterations

    def rank(self, scores):
        w_mat = [[1 if i != j else 0
                  for i in range(self._num_items)]
                 for j in range(self._num_items)]
        for winner, loser in scores:
            w_mat[winner][loser] += 1

        ranks = [1.0 / self._num_items for _ in range(self._num_items)]
        for _ in range(self._num_iterations):
            ranks = self._update_ranks(w_mat, ranks)
        return ranks

    def _update_ranks(self, w_mat, ranks):
        update = [0.0 for _ in range(self._num_items)]
        for i in range(self._num_items):
            wi = 0.0
            ri = 0.0
            for j in range(self._num_items):
                wi += w_mat[i][j]

                x = w_mat[i][j] + w_mat[j][i]
                y = ranks[i] + ranks[j]
                ri += x / y
            update[i] = wi / ri

        total = sum(update)
        return [value / total for value in update]
