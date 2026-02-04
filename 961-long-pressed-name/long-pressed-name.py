class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        name_idx, typed_idx = 0,0
        while typed_idx < len(typed):
            if typed_idx < len(typed) and name[name_idx] != typed[typed_idx]:
                return False
            while typed_idx < len(typed) and name[name_idx] == typed[typed_idx]:
                name_idx += 1
                typed_idx += 1
                if name_idx == len(name):
                    while typed_idx<len(typed) and typed[typed_idx] == name[name_idx -1]:
                        typed_idx += 1
                    if typed_idx == len(typed):
                        return True
                    else:
                        return False
            while typed_idx < len(typed) and name[name_idx-1] == typed[typed_idx]:
                typed_idx += 1
            if typed_idx == len(typed) and name_idx < len(name):
                return False
        return True