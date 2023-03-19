SELECT country, 
       COALESCE(daily_vaccinations, 0) AS daily_vaccinations 
FROM 
    (SELECT country, 
            percentile_cont(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS daily_vaccinations 
     FROM country_vaccination_stats 
     WHERE daily_vaccinations IS NOT NULL 
     GROUP BY country) AS t;
