age = int(input("Enter your age: "))

if age < 5:
    ticket_price = 5
elif age < 16:
    ticket_price = 10
else:
    ticket_price = 18

print(f"You'll pay ${ticket_price} for the ticket")