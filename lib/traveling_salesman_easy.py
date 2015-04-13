class TravelingSalesmanEasy(object):

  def getMaxProfit(self, nCities, profit, city, visits):
    totalProfits = 0
    soldItems    = []  # items which have already been sold 

    for visit in visits:
      for (item, itemCityId) in enumerate(city):
        if (item in soldItems):
          continue

        soldItem = 0 
        runningMaxProfit = 0

        if (itemCityId == visit) and (profit[item] > runningMaxProfit):
          soldItem = item 
          runningMaxProfit = profit[item]

      totalProfits += runningMaxProfit
      soldItems.append(soldItem)

    return totalProfits
