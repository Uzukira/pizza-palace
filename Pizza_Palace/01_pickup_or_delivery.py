# get input function
cost = 0

def pick_deliv(question):

    error = "Sorry, we didn't get that"

    valid = False
    while not valid:
        response = input(question)

        if response == "y":
            return "delivery"

        elif response == "n":
            return "pick up"
        else:
            print(error)
            continue

# main routine
order_type = pick_deliv("Would you like to have your order delivered? (y/n) ")

if order_type == "delivery":
    name = input("What is your name? ")
    address = input("What is your delivery address? ")
    cost += 3
    print("Your order is a delivery order for {} to {}".format(name, address))

else:
    name = input("What is your name? ")
    print("Your order is a pick up order for {}".format(name))

print("your cost is now ${} ".format(cost))
