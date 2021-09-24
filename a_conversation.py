import random
from dr_jekyll import jekyll
from mr_hyde import hyde

def say_something_to_me(someone):
    for elem in someone:
        print(elem[int(random.random()*10)], end= " ")
    print()

for i in range(2, int(random.random()*10+2)):
    print("jekyll:", end="  ")
    say_something_to_me(jekyll)
    print("hyde:", end="  ")
    say_something_to_me(hyde)