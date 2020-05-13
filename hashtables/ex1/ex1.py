

from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        weight = weights[i]
        diff = limit - weight
        compared = hash_table_retrieve(ht, diff)
        if compared is not None:
            return (i,met)
        hash_table_insert(ht,weight,i)

    return None
   
