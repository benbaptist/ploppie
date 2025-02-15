from ploppie import Utility
import random

if __name__ == "__main__":
    utility = Utility(model="gpt-4o-mini")

    # Sample restaurant order
    orders = [
        "I'd like a vegetarian pizza with extra mushrooms and a side salad",
        "Can I get the spicy chicken burger with fries and a milkshake?",
        "I want the seafood pasta with garlic bread, and make it extra spicy",
        "Just a caesar salad and an iced tea for me, dressing on the side",
        "I'll have the steak, medium rare, with mashed potatoes"
    ]

    customer_order = random.choice(orders)

    print(f"Customer order: {customer_order}")
    
    # Identify multiple aspects of the order
    result = utility.selector(
        f"Analyze the following order and select ALL that apply: \n\n`{customer_order}`",
        options=[
            "CONTAINS_MEAT",
            "VEGETARIAN",
            "SPICY_REQUESTED",
            "INCLUDES_SIDES",
            "INCLUDES_BEVERAGE",
            "SPECIAL_INSTRUCTIONS",
            "SEAFOOD"
        ],
        multi_select=True
    )

    # Print the identified order characteristics
    print(f"Order analysis: {result}")
