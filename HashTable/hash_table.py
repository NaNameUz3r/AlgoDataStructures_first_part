class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        value_bytes = bytearray(value, encoding='utf8')
        value_hash = sum(value_bytes) % self.size
        return value_hash

    def seek_slot(self, value):
        index = self.hash_fun(value)
        table_size = self.size - 1
        if table_size == 0 and self.slots[index] is None:
            return index
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            else:
                index += self.step
                while index > table_size:
                    if table_size == 0:
                        index -= 1
                    index -= table_size
                if self.slots[index] is None:
                    return index
        return None

    def put(self, value):
        index_to_put = self.seek_slot(value)
        if index_to_put is not None:
            self.slots[index_to_put] = value
            return index_to_put
        else:
            return None

    def find(self, value):
        index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] == value:
                return index
            else:
                index += self.step
                table_size = self.size - 1
                while index > table_size:
                    index -= table_size
                if self.slots[index] == value:
                    return index
        return None

