import csv

total_vaccinations = 0

with open('country_vaccination_stats_updated.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['date'] == '1/6/2021':
            daily_vaccinations = row['daily_vaccinations']
            if daily_vaccinations != '':
                total_vaccinations += float(daily_vaccinations)

print(f'Total vaccinations on 1/6/2021: {total_vaccinations}')
