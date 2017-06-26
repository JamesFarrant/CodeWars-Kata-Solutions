def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0])] + [sum(j for j in arr if j < 0)] if arr else []
