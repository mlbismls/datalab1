from collections import defaultdict
from itertools import product

import matplotlib.pyplot as plt


def generate_coin_sample_space(num_flips):
    sample_space = {'Heads', 'Tails'}
    weighted_sample_space = defaultdict(int)
    sample_space_product = product(sample_space, repeat=num_flips)
    sample_space_coin = set(sample_space_product)
    for outcomes in sample_space_coin:
        total = len([outcome for outcome in outcomes
                     if outcome == 'Heads'])
        weighted_sample_space[total] += 1
    return weighted_sample_space


def get_matching_event(event_condition, generic_sample_space):
    return set([outcome for outcome in generic_sample_space
                if event_condition(outcome, 3, 8) == 0])


def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome]
                     for outcome in event)
    return event_size / sum(generic_sample_space.values())


def is_in_interval(x, minimum, maximum):
    return minimum <= x <= maximum


# weighted_sample_space = generate_coin_sample_space(10)
# prob = compute_event_probability(is_in_interval, weighted_sample_space)
#
# x= list(weighted_sample_space.keys())
# x.sort()
# sample_space_count=sum(weighted_sample_space.values())
# y= [weighted_sample_space[key]/sample_space_count  for key in x ]
# # where = [not  is_in_interval(key, 3, 7) for key in x]
# # plt.fill_between(x, y,where=where)
#
# weighted_sample_space_20 = generate_coin_sample_space(20)
# m= list(weighted_sample_space_20.keys())
# m.sort()
# sample_space_count=sum(weighted_sample_space_20.values())
# n= [weighted_sample_space_20[key]/sample_space_count  for key in m ]
#
#
# plt.plot(x, y, label='A: 10 coin-flips')
# plt.scatter(x, y)
# plt.plot(m, n, color='black', linestyle='dashdot',
#         label='B: 20 coin-flips')
# plt.scatter(m, n, color='k', marker='x')
# plt.xlabel('Head-count')
# plt.ylabel('Probability')
# plt.legend()
# plt.show()
#
# plt.show()
#
# assert sum(y) == 1


weighted_sample_space = generate_coin_sample_space(10)

x1= list(weighted_sample_space.keys())
x1.sort()
sample_space_count=sum(weighted_sample_space.values())
y= [weighted_sample_space[key]/sample_space_count*10  for key in x1 ]
x = [headcount /10 for headcount in x1]
# where = [not  is_in_interval(key, 3, 7) for key in x]
# plt.fill_between(x, y,where=where)

weighted_sample_space_20 = generate_coin_sample_space(200)
m1= list(weighted_sample_space_20.keys())
m1.sort()
sample_space_count=sum(weighted_sample_space_20.values())
n= [weighted_sample_space_20[key]/sample_space_count*200  for key in m1 ]
m = [headcount /200 for headcount in m1]

# where_10 = [not  is_in_interval(key, 3, 7) for key in x1]
# where_20 = [not  is_in_interval(key, 5, 15) for key in m1]

plt.plot(x, y, label='A: 10 coin-flips')
plt.scatter(x, y)
plt.plot(m, n, color='black', linestyle='-',
        label='B: 20 coin-flips')
plt.scatter(m, n, color='k', marker='x')
# plt.fill_between(x, y, where=where_10)
# plt.fill_between(m, n, where=where_20)
plt.xlabel('Head-count')
plt.ylabel('Probability')
plt.legend()
plt.show()

plt.show()

