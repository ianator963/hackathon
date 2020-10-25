autorefresh-get.py

#!/usr/bin/env python

import panda
crontab -e
30 8 * * * echo "python get_all_states_history.py"
#example, you can also just get the data directly from the curl
CSV_FILE="https://covidtracking.com/data/download/all-states-history.csv"

data = pandas.io.parsers.read_csv(CSV_FILE, low_memory=False)

print("TOTAL ROWS: " + str(len(data.index)))

top_50 = data.head(50)

#naive approach, top 50 is theoretically the lasat 50 states records, this is not the approach I woudl go with
#print(top_50)
top_50.to_csv("all_states_history.csv")