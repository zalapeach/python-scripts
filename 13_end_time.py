hours = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

hours_to_add = (minutes + duration) // 60
remaining_minutes = (minutes + duration) % 60
total_hours = (hours_to_add + hours) % 24
print("\n", total_hours, ":", remaining_minutes, sep = "")
