from src.evaluation import Evaluation
from src.flavometer import Flavometer
from src.io import Io
from src.ranking import Ranking
from src.sampling import Sampling
from src.stats import Stats


def main():
    io = Io()
    state = io.load()
    sampling = Sampling(len(state.flavors), len(state.items))
    evaluation = Evaluation(state.flavors, state.items)
    ranking = Ranking(len(state.items), 10)
    flavometer = Flavometer(sampling, evaluation, ranking)
    stats = Stats(ranking)
    for _ in range(100):
        state, f = flavometer.update(state)
        stats.log(state, f)
    io.save(state)


if __name__ == '__main__':
    main()
