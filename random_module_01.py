# --------- Pseudo - random --------

import random

# ------ 1 Random Program --------
x = random.randint(1,6)
print(x)

# ------ 2 Random Program --------
y = random.random()
print(y)

# ------ 3 Random Program --------
mylist = ['rock','paper','scissors']
z = random.choice(mylist)
print(z)

# ------ 4 Random Program --------
cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
random.shuffle(cards)
print(cards)