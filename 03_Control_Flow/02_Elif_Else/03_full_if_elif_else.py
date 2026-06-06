"""
Full If-Elif-Else Structure

Putting it all together: if, multiple elif, and else.
"""

# Traffic light system
light = input("Traffic light color (red/yellow/green): ").lower()

if light == "red":
    print("STOP!")
elif light == "yellow":
    print("Slow down, prepare to stop.")
elif light == "green":
    print("Go!")
else:
    print("That's not a valid traffic light color.")

# Season based on month
month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
else:
    season = "Autumn"

print(f"Month {month} is in {season}.")
