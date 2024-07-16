from collections import defaultdict
from itertools import product


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
                if event_condition(outcome, 5, 15) == 0])


def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome]
                     for outcome in event)
    return event_size / sum(generic_sample_space.values())


def is_in_interval(x, minimum, maximum):
    return minimum <= x <= maximum


weighted_sample_space = generate_coin_sample_space(20)
prob = compute_event_probability(is_in_interval, weighted_sample_space)
print(prob)
