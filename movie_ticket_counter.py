"""Aerokicks Cinema Hall - command-line Python version."""

print("================================")
print("     AEROKICKS CINEMA HALL")
print("================================")

# Ask for a valid number of tickets.
while True:
    try:
        ticket = int(input("Enter the number of tickets you want to buy (1-10): "))
        if 1 <= ticket <= 10:
            break
        print("Please choose between 1 and 10 tickets.")
    except ValueError:
        print("Please enter a whole number.")

price = ticket * 10
print(f"You have bought {ticket} ticket(s).")
print(f"Ticket subtotal: ${price:.2f}")

# Give a 10% discount when more than 5 tickets are purchased.
if ticket > 5:
    discount = price * 0.10
    price -= discount
    print(f"You received a 10% discount of ${discount:.2f}!")

# Allow the customer to purchase multiple snacks.
food_prices = {"popcorn": 5, "soda": 3, "candy": 2}
while True:
    buy_food = input("Would you like to buy food? (yes/no): ").strip().lower()
    if buy_food == "no":
        break
    if buy_food != "yes":
        print("Please enter yes or no.")
        continue

    while True:
        food = input("Choose popcorn ($5), soda ($3), or candy ($2): ").strip().lower()
        if food in food_prices:
            price += food_prices[food]
            print(f"You bought {food} for ${food_prices[food]:.2f}.")
            print(f"Current total: ${price:.2f}")
            break
        print("Invalid food choice. Please try again.")

# Display the final bill.
print("\n================================")
print("             FINAL BILL")
print("================================")
print(f"Tickets purchased: {ticket}")
print(f"Final total: ${price:.2f}")
print("Thank you for supporting Aerokicks Cinema Hall!")
print("================================")
