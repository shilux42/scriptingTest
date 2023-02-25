# Parse number separated by ', '
def break_num(nums):
    num = nums.split(', ')
    return num

# Append True of False for the distance beetwen 2 numbers
def in_range(distance, status_list, limit):
    if distance >= limit:
        status_list.append(True)
    else:
        status_list.append(False)

    return status_list

# Evalueta the average distance
def average(distance_list, index):
    average_dist = sum(distance_list) / (index + 1)
    return average_dist

def num_pair(num):
    index = 0
    status_list = []
    distance_list = []

    while index != 5:
        num1 = int(num[index])
        num2 = int(num[index + 1])
        distance = num2 - num1
        distance_list.append(distance)
        in_range(distance, status_list, 10)
        index += 1

    average_dist = average(distance_list, index)

    if False in status_list:
        print(False, '---', f'The average distance is {average_dist}')
    elif True in status_list:
        print(True, '---', f'The average distance is {average_dist}')

if __name__ == '__main__':

    with open('numeri.txt') as num_list:
         num = break_num(num_list.read())
         (num_pair(num))