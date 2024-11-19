# Fonctions
# cut_upper_aera : [-inf; +inf] -> [-limit; +limit]
# cut_lower_aera : [-inf; +inf] -> [-inf; -limit] U 0 U [+limit; +inf]

from math import exp


class max_accel():
    def __init__(self, max_pas) :
        self.max_pas = max_pas
        self.old_val = 0
        
    def __call__(self, value):
        if abs(value - self.old_val) < self.max_pas :
            self.old_val = value
        elif value > self.old_val :
            self.old_val += self.max_pas
        else :
            self.old_val -= self.max_pas
        return self.old_val

def map(value, in_min, in_max, out_min, out_max):
    return (value-in_min) * (out_max-out_min) / (in_max-in_min) + out_min

def scale(value, level):
    return value * level

def cut_upper_aera(value, maxi) :
    return min(max(value, -maxi), maxi)

def cut_lower_aera(value, mini) :
    if mini > value > -mini :
        return 0
    return value

def rm_dead_aeras(value, maxi, mini) :
    value = cut_lower_aera(value, mini)
    if value != 0 :
        value = value - mini if value > 0 else value + mini
    value = value * maxi / (maxi-mini)
    value = cut_upper_aera(value, maxi)
    return value

def exp_factor(value, factor):
    signe = 1 - 2*(value < 0)
    value = signe * (exp(abs(value)*factor)-1.0) / (exp(factor)-1.0)
    return value

# A revoir
def square_to_circle(x, y):
    norme = (x**2 + y**2) ** 0.5
    if norme :
        if(abs(x) > abs(y)) :
            gain = abs(x) / norme
        else :
            gain = abs(y) / norme
        x *= gain
        y *= gain
    return x, y

# A revoir
def square_to_losange(x, y):
    if x or y :
        if(abs(x) > abs(y)) :
            gain = (abs(x) + abs(y)) / abs(x)
        else :
            gain = (abs(x) + abs(y)) / abs(y)
        x /= gain
        y /= gain
    return x, y

# A revoir
def cut_norme(x, y, u=1):
    n = (x**2 + y**2) ** 0.5
    if n > u :
        x = x * u / n
        y = y * u / n
    return x, y

