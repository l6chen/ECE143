import csv

filename = 'zip://./datasets/vehicle_stops_2016_datasd_original.csv'
searched_filename = 'zip://./datasets/vehicle_stops_search_details_2016_datasd.csv'
causes={"Citation":0,"Verbal Warning":0, "NULL":0, "Written Warning":0,"FI":0, "Other":0}
time_interval_stop = {"00":0,"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0}
ans={}
with open(searched_filename) as f:
    reader = list(csv.reader(f))
    line_counter=0
    for row in reader:
        if line_counter == 0:
            line_counter += 1
        else:
            ans.setdefault(row[0], [])
f.close()

with open(filename) as f:
    reader = list(csv.reader(f))
    line_counter=0
    for row in reader:
        if line_counter == 0:
            line_counter += 1
        else:
            if (row[0] in ans) and (row[6][11:13] in time_interval_stop):
                ans[row[0]].append(row[6][11:13])
f.close()

with open(filename) as f:
    reader = list(csv.reader(f))
    line_counter=0
    for row in reader:
        if line_counter == 0:
            line_counter += 1
        else:
            if (row[0] in ans) and (row[10]== "Y"):
                ans[row[0]].append("Arrested")
f.close()

with open(filename) as f:
    reader = list(csv.reader(f))
    line_counter=0
    for row in reader:
        if line_counter == 0:
            line_counter += 1
        else:
            if (row[0] in ans) and (row[11]== "Y"):
                ans[row[0]].append("Searched")
f.close()

with open(searched_filename) as f:
    reader = list(csv.reader(f))
    line_counter=0
    for row in reader:
        if line_counter == 0:
            line_counter += 1
        else:
            if (row[0] in ans) and (row[3] in causes):
                ans[row[0]].append(row[3])
f.close()

with open('zip://./datasets/TimeInterval_results_3.csv', mode='w') as create_file:
    f = csv.writer(create_file)
    f.writerow(["stop_id", "time_interval", "result"])
    for i,j in ans.items():
        if len(j) > 1:
            f.writerow([i, j[0], j[1]])
create_file.close()


