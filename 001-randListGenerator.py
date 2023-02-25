from random import randint

def num_list(min, max):
    num_list = []
    
    for i in range(max):
        random_num = randint(min, max)
        num_list.append(random_num)
    
    return num_list

if __name__ == '__main__':
    print(num_list(0, 49))