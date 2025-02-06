import random
#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.randset = set()

    def insert(self, val: int) -> bool:
        if val not in self.randset:
            self.randset.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.randset:
            return False
        else:
            self.randset.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.randset))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

