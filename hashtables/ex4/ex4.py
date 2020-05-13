def has_negatives(a):

    """
    YOUR CODE HERE
    """

    positive = {}
    negative = {}
    result = []

    for num in a:
        if num > 0:
            positive[num] = -num
        if num < 0:
            negative[num] = num * -1

    for key in positive:
        if positive[key] in negative:
            result.append(key)
    return result
    


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
