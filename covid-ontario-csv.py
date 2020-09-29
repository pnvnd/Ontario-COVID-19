#!/usr/bin/python3
""" Ontario COVID-19 Statistics by Peter Nguyen """

import urllib.request
import csv
from datetime import datetime
import matplotlib.pyplot as plt

class OntarioCovid19:

    def __init__(self, master):
        # Load Data
        filename = "https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv"
        response = urllib.request.urlopen(filename)
        lines = [l.decode("utf-8") for l in response.readlines()]
        reader = csv.reader(lines)
        header_row = next(reader)

        dates, ages, outcomes = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[1], "%Y-%m-%d")
                age = row[5]
                outcome = row[8]

            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                ages.append(age)
                outcomes.append(outcome)

        Age_Group = ["<20", "20s", "30s", "40s", "50s", "60s", "70s", "80s", "90s", "UNKNOWN"]

        frequencies = []
        for age in Age_Group:
            frequency = ages.count(age)
            frequencies.append(frequency)
        print(frequencies)

        # Build the GUI

        # Plot the counts.
        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax.bar(Age_Group, frequencies, label="Confirmed Cases")
        # # ax.scatter(dates, deaths, c="red", s=2, label="Cumulative Deaths")

        # Format plot.
        plt.title("Ontario COVID-19\nConfirmed Cases by Age Group", fontsize=16)
        plt.xlabel("Age Group", fontsize=12)
        fig.autofmt_xdate()
        plt.ylabel("Count", fontsize=12)
        plt.tick_params(axis="both", which="major", labelsize=16)

        # # Add legend
        # ax.legend(loc="upper right", frameon=True)

        # Save chart
        plt.savefig("ontario_covid_ages.png")

        plt.show()

def main():
    root = plt.show()
    app = OntarioCovid19(root)
    root.mainloop()

if __name__ == "__main__": main()