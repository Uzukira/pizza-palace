# pizza function

available_pizzas = ["0. Hawaiian $8.50 ", "1. Margarita $8.50 ", "2. Meat lovers $8.50 ", "3. Classic Cheese $8.50 ",
                    "4.Pepperoni $8.50 ", "5. Ham and Cheese $8.50 ", "6. Beef and Onion $8.50 ",
                    "7. BBQ Meat Deluxe $13.50 ", "8. Chicken Deluxe $13.50 ",
                    "9. BBQ Chicken and Bacon Deluxe $13.50 ", "10. Seafood Deluxe $13.50 ",
                    "11. Apricot Chicken Deluxe $13.50 "]

available_toppings = ["0. Cheese", "1. Ham", "2. Pineapple", "3. Tomatoes", "4. Bacon", "5. Pepperoni", "6. Jalapeno",
                      "7. BBQ Sauce", "8. Aioli Sauce", "9. Mayonnaise", "10. Onions", "11. Sausage"]

cost = 0

another = "y"

pizza1_top_list = []
pizza2_top_list = []
pizza3_top_list = []
pizza4_top_list = []
pizza5_top_list = []

pizza2_top = ""
pizza3_top = ""
pizza4_top = ""
pizza5_top = ""


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


def pizza_list(question, list_in):
    confirmation = "n"

    users_pizzas = []

    while len(users_pizzas) < 5:

        what_pizza = input(question)

        incorrect = True

        if len(users_pizzas) == 5:
            return users_pizzas

        elif what_pizza.isdigit() is True and len(users_pizzas) < 5 and confirmation == "n":
            what_pizza_int = int(what_pizza)
            if what_pizza_int < 12:
                users_pizzas.append(list_in[what_pizza_int])

                print(users_pizzas)
            else:
                print("that number is not on our list")

        elif len(users_pizzas) == 0:
            print("There are no pizzas on your list")

        else:
            while incorrect is True and len(users_pizzas) != 5:
                confirmation = input("Are you sure you are finished ordering pizzas? (y/n) ")
                if confirmation == "y":
                    return users_pizzas
                elif confirmation == "n":
                    incorrect = False
                    continue
                else:
                    print("please enter y or n ")
    return users_pizzas


def toppings(question, list_in):
    pizza = list_in
    pizza_toppings = input(question)
    int_pizza_topping = int(pizza_toppings)
    if int_pizza_topping < 12:
        users_toppings = pizza[int_pizza_topping]
        return users_toppings
    else:
        print("please enter a number between 0 and 12")


# main routine
order_type = pick_deliv("Would you like to have your order delivered? (y/n) ")

print(available_pizzas)

pizzas = pizza_list("Enter the number of the pizza you would like and press any letter when finished ordering"
                    " (pizza limit is 5) ", available_pizzas)

pizza1_top = input("Would you like extra toppings on your first pizza for $0.50 (maximum of 3 extras) (y/n) ")
if pizza1_top == "y":
    while another == "y" and len(pizza1_top_list) < 3:
        if None in pizza1_top_list:
                pizza1_top_list.remove(None)
        print(available_toppings)
        extra_toppings = toppings("Enter the number of the extra topping you would from the list above ",
                                  available_toppings)
        pizza1_top_list.append(extra_toppings)
        print(pizza1_top_list)
        another = input("Would you like another extra topping? (y/<enter> for no) ")
    another = "y"


if len(pizzas) > 1:
    pizza2_top = input("Would you like extra toppings on your second pizza for $0.50 (maximum of 3 extras) (y/n) ")
    if pizza2_top == "y":
        while another == "y" and len(pizza2_top_list) < 3:
            if None in pizza2_top_list:
                pizza2_top_list.remove(None)
            print(available_toppings)
            extra_toppings = toppings("Enter the number of the extra topping you would from the list above ",
                                      available_toppings)
            pizza2_top_list.append(extra_toppings)
            print(pizza2_top_list)
            another = input("Would you like another extra topping? (y/<enter> for no) ")
        another = "y"

if len(pizzas) > 2:
    pizza3_top = input("Would you like extra toppings on your third pizza for $0.50 (maximum of 3 extras) (y/n) ")
    if pizza3_top == "y":
        while another == "y" and len(pizza3_top_list) < 3:
            if None in pizza3_top_list:
                pizza3_top_list.remove(None)
            print(available_toppings)
            extra_toppings = toppings("Enter the number of the extra topping you would from the list above ",
                                      available_toppings)
            pizza3_top_list.append(extra_toppings)
            print(pizza3_top_list)
            another = input("Would you like another extra topping? (y/<enter> for no) ")
        another = "y"

if len(pizzas) > 3:
    pizza4_top = input("Would you like extra toppings on your fourth pizza for $0.50 (maximum of 3 extras) (y/n) ")
    if pizza4_top == "y":
        while another == "y" and len(pizza4_top_list) < 3:
            if None in pizza4_top_list:
                pizza4_top_list.remove(None)
            print(available_toppings)
            extra_toppings = toppings("Enter the number of the extra topping you would from the list above ",
                                      available_toppings)
            pizza4_top_list.append(extra_toppings)
            print(pizza4_top_list)
            another = input("Would you like another extra topping? (y/<enter> for no) ")
        another = "y"

if len(pizzas) > 4:
    pizza5_top = input("Would you like extra toppings on your fifth pizza for $0.50 (maximum of 3 extras) (y/n) ")
    if pizza5_top == "y":
        while another == "y" and len(pizza5_top_list) < 3:
            if None in pizza5_top_list:
                pizza5_top_list.remove(None)
            print(available_toppings)
            extra_toppings = toppings("Enter the number of the extra topping you would from the list above ",
                                      available_toppings)
            pizza5_top_list.append(extra_toppings)
            print(pizza5_top_list)
            another = input("Would you like another extra topping? (y/<enter> for no) ")
        another = "y"

classic_pizzas = ["0. Hawaiian $8.50 ", "1. Margarita $8.50 ", "2. Meat lovers $8.50 ", "3. Classic Cheese $8.50 ",
                  "4.Pepperoni $8.50 ", "5. Ham and Cheese $8.50 ", "6. Beef and Onion $8.50 "]

deluxe_pizzas = ["7. BBQ Meat Deluxe $13.50 ", "8. Chicken Deluxe $13.50 ", "9. BBQ Chicken and Bacon Deluxe $13.50 ",
                 "10. Seafood Deluxe $13.50 ", "11. Apricot Chicken Deluxe $13.50 "]

if order_type == "delivery":
    name = input("What is your name? ")
    address = input("What is your delivery address? ")
    cost += 3
    print("Your order is a delivery order for {} to {}".format(name, address))

else:
    name = input("What is your name? ")
    print("Your order is a pick up order for {}".format(name))

print("The pizzas you are ordering are {}".format(pizzas))
if len(pizza1_top_list) > 0:
    print("The toppings for {} are extra: {}".format(pizzas[0], pizza1_top_list))
if len(pizzas) > 1 and len(pizza2_top_list) > 0:
    print("The toppings for {} are extra: {}".format(pizzas[1], pizza2_top_list))
if len(pizzas) > 2 and len(pizza3_top_list) > 0:
    print("The toppings for {} are extra: {}".format(pizzas[2], pizza3_top_list))
if len(pizzas) > 3 and len(pizza4_top_list) > 0:
    print("The toppings for {} are extra: {}".format(pizzas[3], pizza4_top_list))
if len(pizzas) > 4 and len(pizza5_top_list) > 0:
    print("The toppings for {} are extra: {}".format(pizzas[4], pizza5_top_list))

if pizzas[0] in classic_pizzas:
    cost += 8.5
if pizzas[0] in deluxe_pizzas:
    cost += 13.5
if len(pizzas) > 1 and pizzas[1] in classic_pizzas:
    cost += 8.5
if len(pizzas) > 1 and pizzas[1] in deluxe_pizzas:
    cost += 13.5
if len(pizzas) > 2 and pizzas[2] in classic_pizzas:
    cost += 8.5
if len(pizzas) > 2 and pizzas[2] in deluxe_pizzas:
    cost += 13.5
if len(pizzas) > 3 and pizzas[3] in classic_pizzas:
    cost += 8.5
if len(pizzas) > 3 and pizzas[3] in deluxe_pizzas:
    cost += 13.5
if len(pizzas) > 4 and pizzas[4] in classic_pizzas:
    cost += 8.5
if len(pizzas) > 4 and pizzas[4] in deluxe_pizzas:
    cost += 13.5

if len(pizza1_top_list) > 0:
    cost += (len(pizza1_top_list)*0.5)
if len(pizza2_top_list) > 0:
    cost += (len(pizza2_top_list)*0.5)
if len(pizza3_top_list) > 0:
    cost += (len(pizza3_top_list)*0.5)
if len(pizza4_top_list) > 0:
    cost += (len(pizza4_top_list)*0.5)
if len(pizza5_top_list) > 0:
    cost += (len(pizza5_top_list)*0.5)

print("The total cost is ${} ".format(format(cost, '.2f')))
