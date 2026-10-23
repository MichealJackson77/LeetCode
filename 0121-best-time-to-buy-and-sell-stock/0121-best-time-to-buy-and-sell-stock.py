class Solution:
    def maxProfit(self, price: list[int]) -> int:
        buy=price[0]
        profit=0
        for i in range(1,len(price)):
            if buy>price[i]:
                buy=price[i]
            elif price[i]-buy>profit:
                profit=price[i]-buy 
        return profit       

        