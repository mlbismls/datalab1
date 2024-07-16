from itertools import product

possible_children = ['Boy', 'Girl']
sample_space = product(possible_children, possible_children, possible_children, possible_children)


def has_two_boys(outcome):
    return len([child for child in outcome
                if child == 'Boy']) == 2


def get_matching_event(event_condition, generic_sample_space):
    return set([outcome for outcome in generic_sample_space
                if event_condition(outcome)])


def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome]
                     for outcome in event)
    return event_size / sum(generic_sample_space.values())


final = compute_event_probability(has_two_boys, set(sample_space))
print(final)
