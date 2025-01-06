import time

currentTime = time.time() # Get current time

# Obtain the total seconds.milliseconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours - 4  for Eastern Standard Time
totalHours = (totalMinutes // 60) - 4

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is", currentHour, ":",
currentMinute, ":", currentSecond, "EST")
