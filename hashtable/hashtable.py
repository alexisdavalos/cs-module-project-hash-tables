class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'({self.key},{self.value}) ->'

class LinkedList:
    def __init__(self):
        self.head = None;

    def checkNext(self, node):
        if isinstance(HashTableEntry, node.next):
            return True
        else:
            return False

    def __repr__(self):
        nodes = []
        cur = self.head
        if cur == None:
            nodes.append(cur)
        elif cur.next == None:
            nodes.append(cur)
        else:
            while cur:
                nodes.append(cur)
                cur = cur.next
        return f'[LinkedList] -> {[node for node in nodes]}\n'
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
        self.storage = [LinkedList() for i in range(capacity)] 
        self.items = 0
        

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
        for node in self.storage:
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
        # print(f'key in djb2: {key}')
       
        hash = 5381

        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        # print(f'hashed value: {hash}')
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
        # The slot in the arr
        bucket_index = self.hash_index(key)
        # checks the buckets index for key 
        new_node = HashTableEntry(key, value)
        # node/value at the index slot
        cur = self.storage[bucket_index]
        # check if slot's linked list is empty
        if cur.head == None:
            # adds new node to the linked list
            self.storage[bucket_index].head = new_node
            self.items += 1
            return

        # if the head is not None, a node exists in that linked list
        # traverese the list until we find a key and replace its value
        # otherwise add the new node to the end of the list
        else:
            # check the first element of the list
            cur = self.storage[bucket_index].head
            if cur.key == key:
                cur.value = value
                print(f'match found: {cur}')
            else:
            # traverse down the list since more elements exist
                while cur:
                    # found key so replace it's value
                    if cur.key == key:
                        # print(f'found key: {cur.key} = {key}')
                        cur.value = value
                        # print(f'updated value: {cur.value} = {value}')
                    # track previous node
                    prev = cur
                    # update current node
                    cur = cur.next
                # otherwise add new node
                prev.next = new_node
                self.items +=1
            
       
            # print(f'current node updated:{cur}')
            # print(f'current node next updated:{cur.next}')



    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index].head

        if cur.key == key:
            self.storage[index].head = self.storage[index].head.next
            self.items -= 1
            return

        while cur:
            prev = cur
            cur = cur.next
            if cur.key == key:
                prev.next = cur.next
                self.items -= 1
                return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        bucket_index = self.hash_index(key)
        cur = self.storage[bucket_index].head
        if cur == None:
            return None

        if cur.key == key:
            return cur.value

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next

        # if existing_node:
        #     if existing_node != None and existing_node.key == key:
        #         return existing_node.value
        #     else:
        #         return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        


if __name__ == "__main__":
    # ht = HashTable(10)
    # print(ht.storage)
    # print(ht.storage)
    # ht.put('second key', 'second value')
    # print(ht.storage)

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
    def assertTrue(value1, value2):
        if value1 == value2:
            return True
        else:
            return False

    ht = HashTable(8)
    print(ht.storage)

    for i in range(25):
        print(i)
        ht.put(f"key-{i}", f"val-{i}")
        

    print(ht.storage)
    return_value = ht.get("key-12")
    print(assertTrue(return_value, "val-12")
)
 

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
