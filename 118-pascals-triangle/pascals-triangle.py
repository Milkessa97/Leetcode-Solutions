class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1],[1,1]]
        if numRows<=2:
            return l[:numRows]
        while len(l)<numRows:
            new_arr=[1]
            for i in range(1,len(l)):
                new_arr.append(l[-1][i]+l[-1][i-1])
            new_arr.append(1)
            l.append(new_arr)
        return(l)
