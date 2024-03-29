
def process_coin_operation(drawer, coin_quantity):
    """
    Auxiliary function that returns the coin networth that should be 
    added/subtracted to/from the drawer each day.
    """
    if coin_quantity < 0:
        # If coins are being removed, the amount removed cannot surpass half of what is currently at the drawer
        if (drawer + 2*coin_quantity) >= 0: 
            return 2 * coin_quantity # For each coin removed, another one disappears
        raise Exception("Cannot take more coins than half of what is currently in the drawer!")
    return coin_quantity # If the amount is positive or 0, it is just a simple addition


def magic_drawer(coin_array):
    """
    Main function that receives the coin operation
    for each day and returns the final value retrieved from the drawer
    on the final day
    """
    drawer = 0 # starts with 0 coins
    
    for coin_quantity in coin_array: # Each loop represents a day
        drawer += process_coin_operation(drawer, coin_quantity)
        drawer = drawer * 2 # Each coin generates another one
    
    return drawer/2 # For every coin removed, another one disappears


if __name__ == '__main__':
    print("Type a list of positive or negative integers that will represent the number " + 
          "of coins added/subtracted to the drawer, separated by spaces:")
    coin_array = input()

    try:
        coin_array = [int(value) for value in coin_array.split()]
        print(magic_drawer(coin_array))
    except Exception as e:
        print(f"Invalid input, error: {e}")

    