# First-Come, First-Served (FCFS) Disk Scheduling Algorithm
req_sqnce_fcfc = [0, 41, 30, 100, 62, 51, 20]
head_fcfc = 70
total_seek_fcfc = 0
current_fcfc = head_fcfc

print("--- FCFS Disk Scheduling ---")
print(f"Initial head position: {head_fcfc}")
print(f"Request sequence: {req_sqnce_fcfc}")
print("Seek operations:")
for n in req_sqnce_fcfc:
  difference = abs(current_fcfc - n)
  print(f"  {current_fcfc} -> {n} (seek: {difference})")
  total_seek_fcfc += difference
  current_fcfc = n

print(f"FCFS Total Seek Time: {total_seek_fcfc}")
print("\n" + "=" * 40 + "\n") # Separator for clarity

# Shortest Seek Time First (SSTF) Disk Scheduling Algorithm
req_sqnce_sstf = [0, 41, 30, 100, 62, 51, 20]
head_sstf = 70
total_seek_sstf = 0
current_sstf = head_sstf
remaining_sstf = req_sqnce_sstf.copy()
sequence_sstf = []

print("--- SSTF Disk Scheduling ---")
print(f"Initial head position: {head_sstf}")
print(f"Request sequence: {req_sqnce_sstf}")
print("Seek operations:")

while remaining_sstf:
  closest_request = min(remaining_sstf, key=lambda x: abs(current_sstf - x))
  difference = abs(current_sstf - closest_request)
  print(f"  {current_sstf} -> {closest_request} (seek: {difference})")
  total_seek_sstf += difference
  sequence_sstf.append(closest_request)
  current_sstf = closest_request
  remaining_sstf.remove(closest_request)

print(f"SSTF Sequence of requests: {sequence_sstf}")
print(f"SSTF Total Seek Time: {total_seek_sstf}")