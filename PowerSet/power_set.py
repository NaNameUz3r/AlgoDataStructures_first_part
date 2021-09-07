class PowerSet:

    def __init__(self):
        self.set = []

    def size(self):
        return len(self.set)

    def put(self, value):
        if value not in self.set:
            self.set.append(value)

    def get(self, value):
        if value in self.set:
            return True
        return False

    def remove(self, value):
        if self.get(value):
            self.set.remove(value)
            return True
        return False

    def intersection(self, set2):
        intersected_set = PowerSet()
        for item in self.set:
            if set2.get(item):
                intersected_set.put(item)
        return intersected_set

    def union(self, set2):
        union_set = PowerSet()
        for item in self.set:
            union_set.put(item)

        for item in set2.set:
            union_set.put(item)
        return union_set

    def difference(self, set2):
        diff_set = PowerSet()

        for item in self.set:
            if not set2.get(item):
                diff_set.put(item)
        for item in set2.set:
            if not self.get(item):
                diff_set.put(item)
        return diff_set

    def issubset(self, set2):
        for item in set2.set:
            if not self.get(item):
                return False
        return True
