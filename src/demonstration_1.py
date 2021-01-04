"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            
// returns 1
hash_table.get("c");            
// returns -1 (not found)
hash_table.put("b", 1);         
// update the existing value
hash_table.get("b");            
// returns 1
hash_table.remove("b");         
// remove the mapping for 2
hash_table.get("b");            
// returns -1 (not found)
```
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash_fn(key,length):
        return id(key) % length

class MyHashTable:
    def __init__(self,capacity, hash_fn = hash_fn):
        # Your code here
        # init our storage with some positive number of empty slots
        storage = [None] * capacity
        # Some function that takes a key and spits out an integer 
        # we can maka sure that the output is in bounds of our storage by using % 
        hash_fn = hash_fn
    # Your code here

    
    '''
    Add the key and value in the hash table
    If the value already exists in the HashTable, update the value.
    '''
    def put(self, key, value):
        # Your code here
        # 1. Run the key through our hash function
        # 2. If the slot is empty at the specified index, set the storage[index] = (key, value)
        # 3. If the slot isnt free, overwrite it with the new key-value pair 
        # this will have the effect of updating a key that already existed in our hash table 
        index = self.hash_fn(key, len(self.storage))
        # check if this index is taken 
            # if it is taken, check the incoming key against the current key
            # if they match, overwrite 
            # if they dont 
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                self.storage[index] = (key,value) #O(1)
            else: 
                old_key, old_val = self.storage[index]
                print(f"Collision! Overwriting {old_key}: {old_val}")
        self.storage[index] = (key,value) #O(1)

    '''
    Return the value associated with the given key.
    If the key doesnt exist in the hash table, should return -1
    '''
    def get(self, key):
        # Your code here
        # 1. Run our hash function on our key 
        # 2. Check to see if the index is empty or not 
        # - If it is, return -1
        # - otherwise, return the value
        index = self.hash_fn(key, len(self.storage))

        if self.storage[index] is None:
            return -1

        return self.storage[index][1]

    '''
    Removes the key-value pair specified by the key.
    Set the spot where the key-value pair is to None.
    Doesn't return anything.    
    '''

    def remove(self, key: int) -> None:
        # Your code here
        # 1. Run our hash function on our key 
        # 2. Set self.storage[index] = None
        index = self.hash_fn(key, len(self.storage))
        
        self.storage[index] = None #O(1)
    

hash_table = MyHashTable(10)
# ht.put('cat', 'dog')
# ht.print_storage()
# ht.put('cat', 'tiger')
# ht.print_storage()
hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("a"))
print(hash_table.get("c"))
hash_table.put("b", 1)         
print(hash_table.get("b"))
hash_table.remove("b")         
print(hash_table.get("b"))
