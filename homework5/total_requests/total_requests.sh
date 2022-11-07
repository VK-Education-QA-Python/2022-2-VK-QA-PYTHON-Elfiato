awk '{if ($8 ~ /.*HTTP/ && $7 ~ /\/.*/) print}' ../access.log | wc -l | awk '{printf("Total requests\n%s", $1)}' > total_requests.txt
