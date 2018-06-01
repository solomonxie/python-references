"""
Randomly selects k items from a stream of items of unknown or large size.
Each item in the stream has an equal probability of being included in the sample.
"""

import random


def reservoir_sampling(stream, k):
    res = []
    for i, item in enumerate(stream):
        if i < k:
            res.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                res[j] = item
    return res
