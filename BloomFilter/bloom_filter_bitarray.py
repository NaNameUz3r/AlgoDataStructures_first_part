class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitarray = 0
        self.first_mask = 0
        self.second_mask = 0
        for i in range(f_len):
            self.bitarray = (self.bitarray << 1) | 1

    def hash(self, str1, salt):
        hash_mask = 0
        for character in str1:
            hash_mask = (hash_mask * salt + ord(character)) % self.filter_len
        return 1 << hash_mask

    def hash1(self, str1):
        return self.hash(str1, 17)

    def hash2(self, str1):
        return self.hash(str1, 223)

    def add(self, str1):
        self.first_mask |= self.hash1(str1)
        self.second_mask |= self.hash2(str1)

    def is_value(self, str1):
        if self.first_mask & self.hash1(str1) and (
           self.second_mask & self.hash2(str1)):
            return True
        return False
