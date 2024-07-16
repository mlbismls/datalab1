from itertools import product
from collections import defaultdict

possible_rolls = [1, 2, 3, 4, 5, 6]
sample_space_product = product(possible_rolls, repeat=6)
sample_space = set(sample_space_product)

weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    total = sum(outcome)
    weighted_sample_space[total] += 1

def has_two_boys(outcome):
    return sum(outcome) == 21


def get_matching_event(event_condition, generic_sample_space):
    return set([outcome for outcome in generic_sample_space
                if event_condition(outcome,10,21)])


def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome]
                     for outcome in event)
    return event_size / sum(generic_sample_space.values())

def is_in_interval(x, minimum, maximum):
    return minimum <= x <= maximum

prob = compute_event_probability(is_in_interval,weighted_sample_space)
print(prob)

