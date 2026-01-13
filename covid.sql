# Total trials 
use covid_analysis;
select count(*) From clinical_trials;  

# country contribution 
SELECT Country, COUNT(*) AS total_trials
FROM clinical_trials
GROUP BY Country
ORDER BY total_trials DESC;

# Trial Status 

Select status, count(*) as status_count 
From clinical_trials 
Group By status 
Order By status_count DESC;

# Study type 

Select 'Study Type',count(*) as total 
from clinical_trials 
Group by 'Study Type';  
