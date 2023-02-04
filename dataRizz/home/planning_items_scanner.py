import pandas as pd
from graphing import makeGraph

def main(highlight=None):
  plannedDeliveries = pd.read_csv("data/FY21_Planning_Items.csv")
  distributions = []
  completedDeliveries = pd.read_csv("data/FY21_LFM_Order_Items.csv")
  for index, row in completedDeliveries.iterrows():
      distributions.append(str(row["Distribution Date"]))

  def getTotalDeliveries(company):
    totalDeliveries = 0
    for index, row in plannedDeliveries.iterrows():
      if row["Producer Code"] == company:
        totalDeliveries += 1
    return totalDeliveries

  def withinWeek(week, distribution):
    week = week.split(" ")
    week = week[0].split("/")
    week = week[2] + week[0] + week[1]
    distribution = distribution.split(" ")
    distribution = distribution[0].split("/")
    distribution = distribution[2] + distribution[0] + distribution[1]
    if int(week) - 7 <= int(distribution) <= int(week):
      return True
    return False

  def getFailedDeliveries(company):
    failedDeliveries = 0
    for index, row in plannedDeliveries.iterrows():
      if row["Producer Code"] == company:
        for distribution in distributions:
          if withinWeek(str(row["Delivery Week"]), distribution):
            failedDeliveries += 1
            break
    return failedDeliveries

  def getProbabilityACompanyWillFailDelivery(company):
    totalDeliveries = getTotalDeliveries(company)
    failedDeliveries = getFailedDeliveries(company)
    return failedDeliveries / totalDeliveries * 100
    
  companies = []
  for index, row in plannedDeliveries.iterrows():
    if row["Producer Code"] not in companies:
      if type(row["Producer Code"]) == str: #stops it from adding nan
        companies.append(row["Producer Code"])

  company_probabilities = []
  for company in companies:
    company_probabilities.append(100 - getProbabilityACompanyWillFailDelivery(company))
    
  results = pd.DataFrame({"Company": companies, "Probability": company_probabilities})

  makeGraph("Company", companies, "Probability", company_probabilities, title="Probability of Success of a Delivery by Company", 
            x_descriptor="Company", y_descriptor="Probability of Success (%)", highlight=results.index[results["Company"] == highlight].tolist()[0])