class Solution:
    def compress(self, chars: List[str]) -> int:

        idx,left,right= 0,0,0
        while right < len(chars):
            while chars[left]==chars[right]:
                right+=1
                if right == len(chars):
                    break
            length = right-left
            if length == 1:
                chars[idx]=chars[right-1]
                idx+=1
                left+=1
            else:
                length = list(map(str,str(length)))
                chars[idx]=chars[right-1]
                idx+=1
                for i in length:
                    chars[idx]=i
                    idx+=1
                left=right
                print(chars)
        return idx
