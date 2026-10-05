from collections import deque


class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.rt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"P{i + 1} Arrival Time: "))
    bt = int(input(f"P{i + 1} Burst Time: "))
    processes.append(Process(f"P{i + 1}", at, bt))

processes.sort(key=lambda x: x.at)
ready_queue = deque()
time = 0
done = 0
time_quantum = 5

while done < n:
    for process in processes:
        if process.at <= time and process.rt > 0 and process not in ready_queue:
            ready_queue.append(process)

    if not ready_queue:
        time += 1
        continue

    current = ready_queue.popleft()
    run = min(time_quantum, current.rt)
    current.rt -= run
    time += run

    for process in processes:
        if process.at <= time and process.rt > 0 and process not in ready_queue and process != current:
            ready_queue.append(process)

    if current.rt == 0:
        current.ct = time
        current.tat = current.ct - current.at
        current.wt = current.tat - current.bt
        done += 1
    else:
        ready_queue.append(current)

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for proc in processes:
    print(proc.pid, proc.at, proc.bt, proc.ct, proc.tat, proc.wt, sep="\t")

print("\nAverage TAT:", sum(proc.tat for proc in processes) / n)
print("Average WT:", sum(proc.wt for proc in processes) / n)
