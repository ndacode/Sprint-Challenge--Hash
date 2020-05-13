def intersection(arrays):

    """
    YOUR CODE HERE
    """
    arrays = sorted(arrays, key=lambda x: len(x))
    intersects = []
    Dict = {}
    for i in arrays[0]:
        Dict[i] = 1
    for List in arrays[1:]:
        for indx in List:
            if indx in Dict:
                Dict[indx] += 1
    intersects = [found for found in Dict if Dict[found] == len(arrays)]

    return intersects


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
