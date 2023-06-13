from reciprocal import Menu

# Menu for choosing a fruit

# The handler will execute for the chosen option
fruits_menu = Menu(
    "Fruits",  # the name will be displayed in another menu!
    options=["Apples", "Bananas", "Oranges"],
    header="What's your favourite fruit?!",  # the header will display above the options
    handler=lambda fruit: print(f"I love {fruit} too!"),  # the handler will receive the selected option as a parameter
)

# Menu for choosing a vegetable
vegetables_menu = Menu(
    "Vegetables",
    options=["Broccoli", "Carrots", "Lettuce"],
    header="What's your most disliked vegetable?!",
    handler=lambda vegetable: print(f"I HATE {vegetable} too!"),
)

# Menu with two nested menus
menu = Menu("Root menu", [fruits_menu, vegetables_menu])

menu.execute()
