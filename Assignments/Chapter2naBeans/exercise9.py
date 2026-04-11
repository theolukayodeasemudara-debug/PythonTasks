total_seconds = int(input("Enter number of seconds: "))

# Calculate hours
hours = total_seconds // 3600
# Calc minutes
minutes = (total_seconds % 3600) // 60
# Calc secs
seconds = total_seconds % 60

# Output the result
print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
