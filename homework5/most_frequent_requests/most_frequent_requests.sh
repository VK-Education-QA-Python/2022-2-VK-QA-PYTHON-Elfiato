echo Most frequent requests > most_frequent_requests.txt; awk '{var = "http://almhuette-raith.at/"; if ($7 ~ var".*") print(substr($7, length(var))); else print($7)}' ../access.log | sort | uniq -c | sort -nr | head -n 10 | awk '{printf("%s\n%s\n", $2, $1)}' >> most_frequent_requests.txt
