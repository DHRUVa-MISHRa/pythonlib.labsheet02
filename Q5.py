import numpy as np # type: ignore

# a) Load CSV file
temp = np.loadtxt("temperature.csv", delimiter=",")

print("Temperature Data:")
print(temp)

# b) Find hottest day
max_day = np.argmax(temp) + 1
print("\nDay with highest temperature:", max_day)
print("Highest temperature:", np.max(temp))

# c) Average temperature
avg = np.mean(temp)
print("\nAverage temperature:", avg)

# d) Save days exceeding average
above_avg = temp[temp > avg]

np.savetxt("above_average.csv", above_avg, delimiter=",")

print("\nDays with above average temperature saved to above_average.csv")