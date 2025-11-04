class DoublyLinkedList:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.info = {}
        self.lruData = []
        self.lruPointer = 0

    def get(self, key: int) -> int:
        if key in self.info:
            return self.info[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.info[key] = value
        self.lruData.append(key)
        self.size += 1
        if self.size > self.capacity:
            lru = self.lruData[self.lruPointer]
            del self.info[lru]
            self.size -= 1
            self.lruPointer += 1
