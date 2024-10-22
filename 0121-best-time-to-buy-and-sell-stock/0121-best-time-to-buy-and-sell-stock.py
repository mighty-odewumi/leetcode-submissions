class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """
    Iterate through array and get min value
    From that index of min, compare each to get max value
    Return max value - min to get profit
    """

    """
    totalMin = 0
    totalMax = 0
    index = 0
    storeMin = {}
    storeMax = {}

    for i in range(len(prices)):
      if (i == 0):
        totalMin = prices[i]
        index = i
        storeMin[totalMin] = index
      else:
        totalMin = min(totalMin, prices[i])
        if (totalMin == prices[i]):
          index = i
          storeMin[totalMin] = i

    print("totalMin", totalMin)
    print("storeMin", storeMin)

    newPrices = prices[index:]
    for j in range(len(newPrices)):
      if (j == 0):
        totalMax = newPrices[j]
        index = j
        storeMax[totalMax] = index
      else:
        totalMax = max(totalMax, newPrices[j])
        if (totalMax == newPrices[j]):
          index = j
          storeMax[totalMax] = index
    print("Total Max", totalMax)
    print("StoreMax", storeMax)

    return totalMax - totalMin
    """

    cheapest = 0
    maxProfit = 0

    for i in range(len(prices)):
        if i == 0: 
            maxProfit = 0
            cheapest = prices[i]
        
        if prices[i] < cheapest:
            cheapest = prices[i]
        
        else:
            currentProfit = prices[i] - cheapest
            maxProfit = max(maxProfit, currentProfit)
    return maxProfit
