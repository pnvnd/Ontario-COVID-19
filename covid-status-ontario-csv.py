import urllib.request
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv"
response = urllib.request.urlopen(filename)
lines = [l.decode("utf-8") for l in response.readlines()]
reader = csv.reader(lines)
header_row = next(reader)

# Get dates, case and death counts from CSV file.
dates, casesOnt, deaths = [], [], []
for row in reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")

    if row[4] == "":
        caseOnt = 0
    else:
        caseOnt = float(row[4])

    if row[6] =="":
        death = 0
    else:
        death = float(row[6])
    
    dates.append(current_date)
    casesOnt.append(caseOnt)
    deaths.append(death)

# Plot the counts.
plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.scatter(dates, casesOnt, c="blue", s=2, label="Confirmed Cases")
ax.scatter(dates, deaths, c="red", s=2, label="Cumulative Deaths")

# Format plot.
plt.title("Ontario COVID-19\nActive Confirmed Cases and Cumulative Deaths", fontsize=16)
plt.xlabel("Date", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Count", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=16)
ax.set_ylim(bottom=0)

# Add legend
ax.legend(loc="upper left", frameon=True)

# Fix trimming issue with output chart
plt.tight_layout()

# Save chart to file
plt.savefig("covid_cases_deaths.png", dpi=150)

plt.show()
