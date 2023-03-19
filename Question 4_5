import csv

# Find minimum daily vaccinations for each country
min_daily_vaccinations = {}
with open('country_vaccination_stats.csv', 'r') as file_in:
    reader = csv.DictReader(file_in)
    for row in reader:
        country = row['country']
        daily_vaccinations = row['daily_vaccinations']
        if daily_vaccinations == '':
            continue  # skip empty values
        daily_vaccinations = float(daily_vaccinations)
        if country not in min_daily_vaccinations or daily_vaccinations < min_daily_vaccinations[country]:
            min_daily_vaccinations[country] = daily_vaccinations

# Update empty daily vaccinations with minimum value for each country
with open('country_vaccination_stats.csv', 'r') as file_in, open('country_vaccination_stats_updated.csv', 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        country = row[0]
        daily_vaccinations = row[2]
        if daily_vaccinations == '':
            if country in min_daily_vaccinations:
                row[2] = min_daily_vaccinations[country]
            else:
                row[2] = 0
        writer.writerow(row)
