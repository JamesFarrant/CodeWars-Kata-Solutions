def remove_smallest(numbers):
    if len(numbers) > 0:
        mini = min(numbers)
        numbers.remove(mini)
        return numbers
    else:
        return []
