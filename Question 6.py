import csv
import statistics

daily_vaccinations = {}

with open('country_vaccination_stats_updated.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        country = row['country']
        daily_vaccination = row['daily_vaccinations']
        if daily_vaccination == '':
            continue
        daily_vaccination = float(daily_vaccination)
        if country not in daily_vaccinations:
            daily_vaccinations[country] = [daily_vaccination]
        else:
            daily_vaccinations[country].append(daily_vaccination)

top_3 = sorted(daily_vaccinations.items(), key=lambda x: statistics.median(x[1]), reverse=True)[:3]

print("Top-3 countries with highest median daily vaccination numbers:")
for i, (country, daily_vaccinations) in enumerate(top_3):
    print(f"{i+1}. {country}: {statistics.median(daily_vaccinations)}")
