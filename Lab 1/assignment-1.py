# Daksh Dua
# 27 Oct 2025
# Project: Daily Calorie Tracker CLI


# --- Step 1: Introductory Message ---


import datetime


print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals, count total calories, and compare them to your daily limit.\n")


# --- Step 2: Input & Data Collection ---


meals = []
calories = []

# number of meals
num_meals = int(input("How many meals did you have today? "))

# loop runs number of meals times to take meal details
for i in range(num_meals):
    meal = input(f"Enter name of meal #{i+1}: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)


# --- Step 3: Calorie Calculations ---


total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

# total and average calories
print("\n----- CALORIE SUMMARY -----\n")
print(f"Total Calories: {total_calories}")
print(f"Average Calories per Meal: {average_calories: }")


# --- Step 4: Exceed Limit Warning System ---


if total_calories > daily_limit:
    print("Warning! : You exceeded your daily limit!")
else:
    print("Great! You are within your daily limit.")


# --- Step 5: Neatly Formatted Output ---


# column headers
print("\nMeal Name\tCalories")

# a line for separation
print("-" * 25)
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-" * 25)
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories}")


# --- Task 6: Bonus - Save to File ---


save = input("\nDo you want to save this session to a file? (yes/no): ").lower()
if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "a") as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]}: {calories[i]} calories\n")
        file.write("\n")
        file.write(f"Total: {total_calories}\n")
        file.write(f"Average: {average_calories:.2f}\n")
        file.write(f"Daily Limit: {daily_limit}\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded daily limit !!!\n")
        else:
            file.write("Status: Within daily limit. \n")
    print(f" Session appended to {filename}")
