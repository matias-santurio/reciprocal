from reciprocal import Action
from reciprocal import Menu

# An action named Cats that prints a message
cat_action = Action("Cats", lambda: print("You're paw-some!"))

# A menu with the previous action as its only option item
menu = Menu(
    "Root menu",
    [cat_action],
    hovered_fg=(0, 255, 255)  # the hovered option will show with a color of #00FFFF (cyan)
)

# Add another option to the menu
menu.add_option(Action("Dogs", lambda: print("Friends fur-ever!")))

# Display the menu and start the interactive mode
menu.execute()
