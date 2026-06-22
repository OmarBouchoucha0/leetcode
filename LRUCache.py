class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.info = {}

    def get(self, key: int) -> int:
        if key in self.info:
            value = self.info[key]
            del self.info[key]
            self.info[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.info:
            del self.info[key]
        elif len(self.info) >= self.capacity:
            first_key = next(iter(self.info))
            del self.info[first_key]

        self.info[key] = value
