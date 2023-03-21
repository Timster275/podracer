import random
from typing import List
class DataGenerator():
    def __init__(self, sample_size):
        self.sample_size = sample_size

    def lin(self) -> List[int]:
        dt = [x for x in range(self.sample_size)]
        random.shuffle(dt)
        return dt
    
    def exp(self):
        dt = [x**2 for x in range(self.sample_size)]
        random.shuffle(dt)
        return dt
    
    def rand(self):
        dt = [random.randint(0, 10000) for x in range(self.sample_size)]
        random.shuffle(dt)
        return dt