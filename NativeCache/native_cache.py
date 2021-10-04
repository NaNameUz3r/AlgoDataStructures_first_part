class NativeCache:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def seek_empty_slot(self, key):
        key_index = self.hash_function(key)
        for item in range(self.size - 1):
            if self.slots[key_index] is None:
                return key_index
            elif self.check_steps(key_index, None):
                return key_index
        return None

    def hash_function(self, value):
        key_index = 0
        value_string = str(value)
        for i in range(len(value_string)):
            if ord(value_string[i]) != 0:
                key_index += ord(value_string[i]) * (i + 1)
            else:
                key_index += 11 * (i + 1)
        if self.size != 0:
            key_index = key_index % self.size
        return key_index

    def check_steps(self, index_to_check, value_to_check):
        if index_to_check + self.step <= self.size - 1:
            index_to_check += self.step
            if self.slots[index_to_check] == value_to_check:
                return True
        elif index_to_check + self.step > self.size - 1:
            index_to_check = index_to_check + self.step - self.size
            if self.slots[index_to_check] == value_to_check:
                return True
        return False

    def put(self, key, value):
        target_slot = self.seek_empty_slot(key)
        if target_slot is None:
            target_slot = self.define_displace_slot()

        self.slots[target_slot] = key
        self.values[target_slot] = value
        self.hits[target_slot] = 0

    def define_displace_slot(self):
        minimal_hits = self.hits[0]
        key_for_displace = None
        for i in range(self.size):
            if self.hits[i] <= minimal_hits:
                minimal_hits = self.hits[i]
                key_for_displace = i
        return key_for_displace

    def get(self, key):
        target_slot = self.find_slot(key)
        if target_slot is not None:
            self.hits[target_slot] += 1
            return self.values[target_slot]
        else:
            return None

    def find_slot(self, value):
        slot_index = self.hash_function(value)
        if self.slots[slot_index] == value:
            return slot_index
        elif self.check_steps(slot_index, value):
            return slot_index
        return None

    def clean_cache(self):
        for i in range(self.size):
            self.slots[i] = None
            self.values[i] = None
            self.hits[i] = 0
