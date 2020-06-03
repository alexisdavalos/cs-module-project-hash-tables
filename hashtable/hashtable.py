class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.index = None

    def __repr__(self):
        return f'({self.key}:{self.value})'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [None] * capacity

    def __repr__(self):
        return f'({self.capacity}:{self.bucket})'

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # Formula for load factor = num of pairs/num of buckets
        pairs = 0
        for node in self.buckets:
            while node!= None and node.next!= None:
                pairs+=1
        
        load_factor = pairs//self.capacity
        return load_factor
        

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        print(f'key in djb2: {key}')
        if isinstance(key, str):
            hash = len(key)
        else:
            hash = key

        byte_array = str.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        print(f'hashed value: {hash}')
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        # print(f'hash key: {key}')
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # print(f'given key: {key}')
        bucket_index = self.hash_index(key)
        print(f'bucket index: {bucket_index}')
        new_node = HashTableEntry(key, value)
        # checks the buckets index for key 
        existing_node = self.buckets[bucket_index]
        while existing_node != None:
            # check if given key matches node key
            if existing_node.key == key:
                # if they match, update the value
                self.buckets[bucket_index].value = value
                return
            # no key found
            else:
                # replace None w/ new node
                self.buckets[bucket_index] = new_node
                return

        if existing_node == None:
            self.buckets[bucket_index] = new_node
            return new_node


       


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        for bucket in self.buckets:
            if bucket == None:
                return None
            elif bucket.key == key:
                return bucket.value
            else:
                return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        


if __name__ == "__main__":
    ht = HashTable(8)
    print(ht.buckets)
    ht.put('first key', 'first value')
    print(ht.buckets)
    ht.put('second key', 'second value')
    print(ht.buckets)
    key = ht.get('first key')
    print(f'get key: {key}')
    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")
    # print(ht.buckets)
    print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
