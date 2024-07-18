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


weighted_sample_space = generate_coin_sample_space(10)
prob = compute_event_probability(is_in_interval, weighted_sample_space)

x= list(weighted_sample_space.keys())
sample_space_count=sum(weighted_sample_space.values())
y= [weighted_sample_space[key]/sample_space_count  for key in x ]
plt.scatter(x, y)
plt.show()
