from typing import List
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np
import warnings 

warnings.filterwarnings("ignore")
class ResourceOwner:
    _data = []
    reads = 0
    writes = 0

    def __init__(self, sample_size: int = 20):
        self._data = np.random.randint(0, 10000, sample_size)
        self.len = len(self._data)
    
    def plot(self):
        plt.bar(range(len(self._data)), self._data)
        plt.show()

    def get(self, positon: int) -> int:
        self.reads += 1
        return self._data[positon]

    def set(self, position: int, value: int):
        self._data[position] = value
        self.writes += 1

    def get_snapshot(self) -> List[int]:
        return self._data

    def animate(self, sort):
        fig, ax = plt.subplots()
        plt.title("Sorting Visualizer")
        generator = sort(self)
        bar_rects = ax.bar(range(len(self._data)), self._data)
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        
        iteration = [0]
        def update_fig(_data, rects, iteration):
            for rect, val in zip(rects, _data):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text("GRAPH UPDATES: {} reads: {} writes: {}".format(iteration, self.reads, self.writes))
        anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator, interval=1, repeat=False)
        plt.show()
        
    def logSummary(self):
        print("Reads: {} Writes: {}".format(self.reads, self.writes))
        print("Total: {}".format(self.reads + self.writes))