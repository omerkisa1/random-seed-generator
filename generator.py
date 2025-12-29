import time

class LaggedFibonacciRNG:
    def __init__(self, seed=None):
        self.j = 24
        self.k = 55  
        self.m = 2**64 

        if seed is None:
            seed = time.time_ns()
            
        self.state_buffer = []
        temp_state = seed
        
        for _ in range(self.k):
            temp_state = (6364136223846793005 * temp_state + 1442695040888963407) % self.m
            self.state_buffer.append(temp_state)
            
        self.index = 0
    def next(self):
        idx_j = (self.index - self.j) % self.k
        idx_k = (self.index - self.k) % self.k 
        
        new_val = (self.state_buffer[idx_j] + self.state_buffer[idx_k]) % self.m
        
        self.state_buffer[self.index] = new_val
        
        self.index = (self.index + 1) % self.k
        
        return new_val

rng = LaggedFibonacciRNG(seed=time.time_ns())
print("Üretilen ilk 5 sayı:")
for i in range(5):
    print(f"{i+1}. Sayı: {rng.next()}")