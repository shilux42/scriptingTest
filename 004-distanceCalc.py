def break_num(nums):
    num = nums.split(', ')
    return num

def in_range(distance, index, limit):
    distance_list = []
    if distance >= limit:
        distance_list.append(distance)
        print(distance_list)

def num_pair(num):
    index = 0
    

    while index != 5:
        num1 = int(num[index])
        num2 = int(num[index + 1])
        distance = num2 - num1
        in_range(distance, index, 10)
        index += 1
        
with open('numeri.txt') as num_list:
     num = break_num(num_list.read())
     num_pair(num)