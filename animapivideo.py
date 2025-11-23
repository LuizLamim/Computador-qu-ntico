import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True