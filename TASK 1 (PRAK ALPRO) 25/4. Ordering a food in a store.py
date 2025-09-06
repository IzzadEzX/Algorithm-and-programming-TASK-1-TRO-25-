print("============")
print("Welcome to our store")
print("============")
balance = 50000
while balance > 15000:
  print("your balance is: ", balance)
  print("MENU")
  print("1. Pizza = Rp 25000")
  print("2. Chicken smash = 15000")
  user_input = int(input("Enter your choice: "))
  match user_input:
    case 1:
      print("You have ordering pizza")
      balance -= 25000
    case 2:
      print("You have ordering chicken smash")
      balance -= 15000
    case _:
      print("invalid input")
print("Thanks for coming")
