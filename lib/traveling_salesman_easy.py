class TravelingSalesmanEasy(object):

  def getMaxProfit(self, nCities, profit, city, visits):
    totalProfits = 0
    soldItems    = []  # items which have already been sold; closed set

    for visitedCity in visits:
      soldItem         = -1
      runningMaxProfit = 0

      for item, buyingCity in enumerate(city):
        if (visitedCity == buyingCity):
          if (item in soldItems):
            continue

          if (profit[item] > runningMaxProfit):
            soldItem         = item
            runningMaxProfit = profit[item]

      if (soldItem != -1):
        soldItems.append(soldItem)
        totalProfits += runningMaxProfit

    return totalProfits

