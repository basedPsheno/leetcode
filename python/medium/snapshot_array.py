# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [{} for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.history[index][self.snap_id] = val
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.history[index]:
            return self.history[index][snap_id]
        elif len(self.history[index]) > 0:
            keys = list(self.history[index].keys())
            for vsi in reversed(keys):
                if vsi < snap_id:
                    return self.history[index][vsi]
            
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
