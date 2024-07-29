country = ["egypt", "france", "germany"]
num = [1, 2, 3]
x = input("Enter the country: ")

total_visits = 0

for i in range(len(country)):
    if country[i] == x:
        num_msg = f"You have visited {country[i]} {num[i]} time(s)"
        print(num_msg)
        break  # Exit the loop once the country is found

# Calculate total visits only if the input is "all"
if x == "all":
    for i in range(len(num)):
        total_visits += num[i]
    print(f"Total number of visits across all countries: {total_visits}")
