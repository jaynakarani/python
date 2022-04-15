import statistics

number = list(map(int,input().split()))


max_number = max(number)
min_number = min(number)
mean_number = round(statistics.mean(number),2)
standard_deviation = round(statistics.stdev(number),2)
variance_number = round(statistics.variance(number),2)

print(max_number, min_number, mean_number, standard_deviation, variance_number)