import sys
class jar:
    def __init__ (self,capacity=12):
        self.capacity = 12
        self.size = 0
        if self.capacity < 0:
            raise ValueError ("Capacity must be a non-negative integer")
    def __str__(self):
        return f"🍪" * self.size
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceeds capacity")
        self.size += n
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self.size -= n
            for v in self.size:
                print("nom" * v
    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size
