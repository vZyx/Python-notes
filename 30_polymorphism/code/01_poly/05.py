

class GraphAlgorithm:
    def __init__(self):
        self.algorithms_steps = [self.step1_general,
                                 self.step2_abstract,
                                 self.step3_general]

    def run(self):
        return ''.join([step() for step in self.algorithms_steps])

    def step1_general(self):
        return 'G1'

    def step3_general(self):
        return 'G3'

class Dijkstra(GraphAlgorithm):
    def __init__(self):
        super().__init__()

    def step2_abstract(self):
        return 'APQ'

print(Dijkstra().run())