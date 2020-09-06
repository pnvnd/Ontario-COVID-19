import csv
import urllib.request
from datetime import datetime
import matplotlib.pyplot as plt

filename = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv"
response = urllib.request.urlopen(filename)
lines = [l.decode("utf-8") for l in response.readlines()]

reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

# for index, column_header in enumerate(header_row):
    # print(index, column_header)

# Get dates and high temperatures from this file.
dates, cases, deaths = [], [], []
for row in reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")

    if row[4] == "":
        case = 0
    else:
        case = int(row[4])

    if row[6] =="":
        death = 0
    else:
        death = int(row[6])
    
    dates.append(current_date)
    cases.append(case)
    deaths.append(death)

# print(deaths)

# Plot the high temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(dates, cases, c=cases, cmap=plt.cm.Blues, s=10)
ax.scatter(dates, deaths, c=deaths, cmap=plt.cm.Reds, s=10)

# Format plot.
plt.title("Ontario COVID-19 Cases and Deaths", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Count", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
