class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        
class LinkedKVPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash(inpt, max):
    inpt = ((inpt >> 16) ^ inpt) * 0x45d9f3b
    inpt = ((inpt >> 16) ^ inpt) * 0x45d9f3b
    inpt = ((inpt >> 16) ^ inpt)

    return inpt % max

def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))

    current_KVpair = hash_table.storage[index]
    last_KVpair = None

    while current_KVpair is not None and current_KVpair.key != key:
        last_KVpair = current_KVpair
        current_KVpair = last_KVpair.next

    if current_KVpair is not None:
        current_KVpair.value = value
    else:
        new_KVpair = LinkedKVPair(key, value)
        new_KVpair.next = hash_table.storage[index]
        hash_table.storage[index] = new_KVpair

def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_KVpair = hash_table.storage[index]

    while current_KVpair is not None:
        if(current_KVpair.key == key):
            return current_KVpair.value
        current_KVpair = current_KVpair.next

