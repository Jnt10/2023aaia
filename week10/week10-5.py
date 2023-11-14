class Solution:
    def average(self, salary: List[int]) -> float:
        # print(sum(salary))
        # 有陷阱, 程式還不對, 先寫2行, 等一下會修正
        total = sum(salary) - max(salary) - min(salary) 
        N =len(salary) - 2 #因為扣掉最大值、最小值,數目
        return total / N
        # return (sum(salary)-max(salary)-min(salary)) / (len(salary)-2)