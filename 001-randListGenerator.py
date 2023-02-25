from random import randint

def num_list(min, max):
    num_list = []
    
    for i in range(max):
        randomNum = randint(min, max)
        num_list.append(randomNum)
    
    return num_list


print(num_list(1, 50))

