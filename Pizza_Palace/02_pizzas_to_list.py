# pizza function

available_pizzas = ["0. Hawaiian $8.50 ", "1. Margarita $8.50 ", "2. Meat lovers $8.50 ", "3. Classic Cheese $8.50 ", "4.Pepperoni $8.50 ", "5. Ham and Cheese $8.50 ", "6. Beef and Onion $8.50 ",
                        "7. BBQ Meat Deluxe $13.50 ", "8. Chicken Deluxe $13.50 ", "9. BBQ Chicken and Bacon Deluxe $13.50 ", "10. Seafood Deluxe $13.50 ", "11. Apricot Chicken Deluxe $13.50 "]

def pizza_list(question):
    continue_ = "s"

    error = "Your input does not match the available options "

    available_pizzas = ["0. Hawaiian $8.50 ", "1. Margarita $8.50 ", "2. Meat lovers $8.50 ", "3. Classic Cheese $8.50 ", "4.Pepperoni $8.50 ", "5. Ham and Cheese $8.50 ", "6. Beef and Onion $8.50 ",
                        "7. BBQ Meat Deluxe $13.50 ", "8. Chicken Deluxe $13.50 ", "9. BBQ Chicken and Bacon Deluxe $13.50 ", "10. Seafood Deluxe $13.50 ", "11. Apricot Chicken Deluxe $13.50 "]
    users_pizzas = []

    while len(users_pizzas) < 5 or what_pizza.isdigit() == True:
        what_pizza = input(question)

        if what_pizza.isdigit() == True and len(users_pizzas) < 5:
            what_pizza_int = int(what_pizza)
            what_pizza_int.isdecimal
            if what_pizza_int < 12:
                users_pizzas.append(available_pizzas[what_pizza_int])

                print(users_pizzas)
            else:
                print("that number is not on our list")

        elif len(users_pizzas) == 0:
            print("There are no pizzas on your list")

        else:
            return users_pizzas

    return users_pizzas

print(available_pizzas)

pizzas = pizza_list("Enter the number of the pizza you would like and press any letter when finished ordering pizzas (pizza limit is 5) ")

print("The pizzas you are ordering are {}".format(pizzas))
