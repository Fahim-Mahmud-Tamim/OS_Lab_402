process = [
    ("p1", 3, 3),
    ("p2", 2, 1),
    ("p3", 5, 2),
    ("p4", 0, 3),
    ("p5", 1, 2)
]

process.sort(key=lambda x: x[1])
time = 0
total_wt = 0
total_tat = 0

print("Process AT BT CT TAT WT")

for p, at, bt in process:
    if time < at:
        time = at

    time = time + bt
    ct = time

    tat = ct - at
    wt = tat - bt

    total_tat = total_tat + tat
    total_wt = total_wt + wt

    print(p, at, bt, ct, tat, wt)

n = len(process)
print("Average TAT =", total_tat / n)
print("Average WT =", total_wt / n)