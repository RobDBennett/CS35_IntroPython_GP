# lets import what we need and start working on a REPL
from store import Store
from data import cats

my_store = Store("Bobs Emporium", [cats["legs"], cats["fruit"], cats['special'], cats['bats']])

print(my_store)
#repr(my_store)
selection = 0
while selection != len(my_store.categories) + 1:

    selection = input("Please select the number of the department:")
    try:
        selection = int(selection)
        if selection == len(my_store.categories) + 1:
            print(f"Thank you for shoping at {my_store.name}.")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection - 1])
        else:
            print("Please select a valid number for departments.")
    except ValueError:
        print("Please enter a number as it relates to the categories")
