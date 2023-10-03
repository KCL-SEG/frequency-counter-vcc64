"""Frequencies function."""

def frequencies(items):
    for item in items:
        frequencies = {}
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies
