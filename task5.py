#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

population = float(input("Please enter the population\n"))
rate_of_growth = float(input("Please enter the rate of growth in decimal form: "))
numberofdays = float(input("Please enter the number of days:  "))
daysoutofayear = numberofdays/365
one = 1
future_population = (population) * (one + rate_of_growth)**(daysoutofayear)
rfp=round(future_population,0)
print(f"There will be {rfp} people after 12 days")