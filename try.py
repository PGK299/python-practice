total = 925.75
while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

total += num
print(f"Total: {total:.2f}") 