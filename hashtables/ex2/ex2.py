

from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    hashtable = HashTable(length)
    route = [None] * length

    # insert key,value pair
    for i in tickets:
        # Add source and destination KV pairs to hashtable
         hash_table_insert(hashtable, i.source, i.destination)
    
    #Set first item as a None value
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    index = 0
    insert = 1
    while insert < length:
        # as we iterate through, we're putting a ticket into the route,  and putting it in starting at the 'insert' index (starting at 1). At the 'insert' index, we're adding the value that's returned when we retrieve the key which matches the current index (starting at 0) from our hash table 
        route[insert] = hash_table_retrieve(hashtable, route[index])
        # increase current index and insert count until the number of inserts matches the number of indexes
        index += 1
        insert += 1
    return route
