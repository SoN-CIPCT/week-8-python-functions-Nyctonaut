# sandwich ingredients function
def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    
    for ingredient in ingredients:
        print("- " + ingredient)
    
    print("Your sandwich is ready!")


# Function call #1 (3 ingredients)
make_sandwich("turkey", "lettuce", "tomato")


# Function call #2 (5 ingredients)
make_sandwich("ham", "cheese", "mustard", "pickles", "onions")