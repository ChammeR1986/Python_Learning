time_sec = int(input("enter time in seconds: "))

hours = time_sec // 3600
remaining_sec = time_sec % 3600

minutes = remaining_sec // 60
final_seconds = remaining_sec % 60

print (f"{hours:02}:{minutes:02}:{final_seconds:02}")
