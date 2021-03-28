from src.state import State


class Io(object):
    @staticmethod
    def load():
        flavors = ['bitter', 'salzig', 'sauer', 'süß', 'umami']
        items = [
            'saurer Apfel',
            'süßer Apfel',
            'reife Banane',
            'unreife Banane',
            'Gurke',
            'Tomate']
        scores = [[] for _ in range(len(flavors))]
        return State(flavors, items, scores)

    @staticmethod
    def save(data):
        pass
