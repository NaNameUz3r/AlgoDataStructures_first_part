class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        if self.is_key(key) is False:
            if self.values.count(None) != 0:
                return self.values.index(None)
            else:
                return None

    def is_key(self, key):
        key_exists = False
        for item in range(self.size):
            if self.slots[item] == key:
                key_exists = True
                return key_exists
        return key_exists

    def put(self, key, value):
        slot_to_put = self.hash_fun(key)
        if slot_to_put is not None and self.is_key(key) is False:
            self.slots[slot_to_put] = key
            self.values[slot_to_put] = value
        else:
            return None

    def get(self, key):
        for item in range(self.size):
            if self.slots[item] == key:
                return self.values[item]
        return None