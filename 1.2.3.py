from collections import defaultdict
weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    total = sum(outcome)
    weighted_sample_space[total] += 1
# 这段代码实际上是将能够组合成固定值的样本空间的样本记录下来，也就是指能产生的total数的组合有多少钟