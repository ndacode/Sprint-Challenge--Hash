def finder(files, queries):

    """
    YOUR CODE HERE
    """
    Dict = {}
    result = []
    for i in files:
        last = i.split("/")[-1]
        if last in Dict:
            Dict[last].append(i)
        else:
            Dict[last] = [i]
    for search in queries:
        if search in Dict:
            result += [found for found in Dict[search]]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
