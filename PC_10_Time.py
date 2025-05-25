import time

t = time.strftime('%H:%M:%S')  # Get current time as string (Hour:Minute:Second)
print(t)                       # Print the current time

hr = int(time.strftime('%H'))  # Get current hour as an integer (0-23)

# Check the time of day and print corresponding greeting
if hr >= 6 and hr < 12:
    print("Good Morning")      # Between 6 AM and before 12 PM
elif hr >= 12 and hr <= 18:
    print("Good Afternoon")    # Between 12 PM and 6 PM (inclusive)
elif hr > 18 and hr <= 24:
    print("Good Night")        # Between after 6 PM and midnight
