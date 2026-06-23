class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            values_array = self.store[key]
            for i, (_, time) in enumerate(values_array):
                if time > timestamp:
                    self.store[key].insert(i, (value, timestamp))
                    return
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            values_array = self.store[key]
            index = len(values_array)
            for i, (_, time) in enumerate(values_array):
                if time > timestamp:
                    index = i - 1
                    break
            if index < 0:
                return ""
            if index == len(values_array):
                return values_array[-1][0]
            return values_array[index][0]
        else:
            return ""
