class HashTable:
    def __init__(self , size=7):
        self.data_map = [None] * size

    def _hash(self , key):
        hash_res = 0
        for letter in key :
            hash_res = (hash_res + ord(letter)*23) % (len(self.data_map))

        return hash_res
    def set_item(self , key , value):
        index = self._hash(key)

        if self.data_map[index] is None :
            self.data_map[index] =  []

        self.data_map.append([key,value])



    def get_item(self , key):
        index = self._hash(key)

        if self.data_map[index] is not None :
            for item in  self.data_map[index] :
                if item[0] == key :
                    return item[1]

        return None

    def keys(self ):
        all_keys = []

        for kvp in self.data_map :
            if kvp is not None :
                for item in kvp :
                    all_keys.append(item[0])

        return all_keys





