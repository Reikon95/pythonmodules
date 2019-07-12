import codecademylib3_seaborn #ignore


from matplotlib import pyplot as plt

import random

numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()


'''
We are import pyplot from matplotlib under the alais of plt for ease of use

numbers a is just 1-12 written

numbers b is 12 numbers at random between 1 - 1000

line 12 plots a graph with each of these data groups as the axis

line 14 prits the graph.
