processes = [
    {"PID": "P1", "AT": 0, "BT": 6},
    {"PID": "P2", "AT": 1, "BT": 2},
    {"PID": "P3", "AT": 2, "BT": 3},
    {"PID": "P4", "AT": 3, "BT": 1},
    {"PID": "P5", "AT": 4, "BT": 2}
]

time = 0
completed = []
total_wt = 0

for p in processes:
    p["RT"] = p["BT"]


def find_shortest(ready):
    shortest = ready[0]
    for p in ready:
        if p["RT"] < shortest["RT"]:
            shortest = p
    return shortest


while len(completed) < len(processes):
    ready = []
    for p in processes:
        if p["AT"] <= time and p not in completed and p["RT"] > 0:
            ready.append(p)

    if not ready:
        time += 1
        continue

    p = find_shortest(ready)
    p["RT"] -= 1
    time += 1

    if p["RT"] == 0:
        p["CT"] = time
        p["TAT"] = p["CT"] - p["AT"]
        p["WT"] = p["TAT"] - p["BT"]

        total_wt += p["WT"]
        completed.append(p)

print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in completed:
    print(p["PID"], "\t", p["AT"], "\t", p["BT"], "\t", p["CT"], "\t", p["TAT"], "\t", p["WT"])

average_wt = total_wt / len(processes)
print("\nAverage Waiting Time =", average_wt)
