class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_map = [0] * self.filter_len

    def hash1(self, str1):
        hashed_index = 0
        hardcoded_random = 17
        for c in str1:
            code = ord(c)
            hashed_index = hashed_index * hardcoded_random + code
        hashed_index = hashed_index % self.filter_len
        return hashed_index

    def hash2(self, str1):
        hashed_index = 0
        hardcoded_random = 223
        for c in str1:
            code = ord(c)
            hashed_index = hashed_index * hardcoded_random + code
        hashed_index = hashed_index % self.filter_len
        return hashed_index

    def add(self, str1):
        hashed_indexes = [self.hash1, self.hash2]
        for hash_function in hashed_indexes:
            self.bit_map[hash_function(str1)] = 1

    def is_value(self, str1):
        hashed_indexes = [self.hash1, self.hash2]
        total_bits = 0
        for hash_function in hashed_indexes:
            if self.bit_map[hash_function(str1)] == 1:
                total_bits += 1
        return total_bits == len(hashed_indexes)
