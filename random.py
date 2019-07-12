import random

random_list = []

for i in range(101):
  random_list.append(random.randint(1, 101))
print(random_list)
randomer_number = random.choice(random_list)


print(randomer_number)

'''
you import the random module, and there are multiple functions for this
the one in line 6 generates a random int between 1 and 100 (inclusive, exclusive)
Then line 8 generates a random int out of that list

'''
