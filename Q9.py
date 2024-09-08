import math
def calculate_mean(my_list):
    i = 0
    x = 0
    for a in my_list:
        x = x + a
        i+=1
    x = x / i
    return x
def calculate_median(my_list):
    n = len(my_list)
    s_list = sorted(my_list)
    
    if n % 2 == 1:
        median = s_list[n//2]
    else:
        median_1 = s_list[n//2 - 1]
        median_2 = s_list[n//2]
        median = ((median_1 + median_2)/2)
    return median
def calculate_mode(my_list):
    counter ={}

    for item in my_list:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    max = None
    for count in counter.values():
        if max is None or count > max:
            max = count

    for key, value in counter.items():
        if value == max:
            mode = key
    return mode
def calculate_range(my_list):
    n = len(my_list)
    s_list = sorted(my_list)

    max_lim = s_list[n-1]
    min_lim = s_list[0]
    range = max_lim - min_lim

    return range
def calculate_variance(my_list):
    num = 0
    mean = calculate_mean(my_list)
    for x in my_list:
        num = num + (x-mean) ** 2
        variance = num / len(my_list)
    return variance
def calculate_std(my_list):
    variance = calculate_variance(my_list)
    std = math.sqrt(variance)
    return std

my_list = [32, 40, 40, 28, 37, 35, 33]

print("Mean: ", calculate_mean(my_list))
print("median: ", calculate_median(my_list))
print("mode: ", calculate_mode(my_list))
print("range: ", calculate_range(my_list))
print("variance: ", calculate_variance(my_list))
print("std: ", calculate_std(my_list))
