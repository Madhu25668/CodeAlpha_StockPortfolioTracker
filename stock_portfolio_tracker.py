"""
Stock Portfolio Tracker
------------------------
A simple console program that calculates the total value of a user's
stock portfolio using hardcoded stock prices, and saves a summary
report to a text file.
"""

# Step 1: Hardcoded dictionary of stock prices (stock symbol -> price per share)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320
}


def show_available_stocks(prices):
    """Print the list of stocks the user is allowed to enter."""
    print("Available stocks and their prices:")
    for symbol, price in prices.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio_input(prices):
    """
    Ask the user to enter stock names and quantities one at a time.
    Returns a list of dictionaries, each holding details for one stock entry.
    """
    portfolio = []  # will store each entry as {"symbol", "quantity", "price", "total"}

    print("Enter your stock holdings below.")
    print("Type 'done' as the stock name when you are finished.\n")

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()

        # Exit condition for the loop
        if symbol == "DONE":
            break

        # Check if the entered stock exists in our hardcoded dictionary
        if symbol not in prices:
            print("Sorry, that stock is not available. Please choose from the list above.\n")
            continue  # go back to the start of the loop and ask again

        # Ask for quantity and validate it
        quantity_input = input(f"Enter quantity for {symbol}: ")

        if not quantity_input.isdigit():
            print("Please enter a valid whole number for quantity.\n")
            continue

        quantity = int(quantity_input)

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

        # Basic arithmetic: calculate the total cost for this stock
        price = prices[symbol]
        total = price * quantity

        # Store this entry in our portfolio list
        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        print(f"Added: {quantity} share(s) of {symbol} at ${price} each = ${total}\n")

    return portfolio


def calculate_total_investment(portfolio):
    """Sum up the total value across all stock entries in the portfolio."""
    total_investment = 0
    for entry in portfolio:
        total_investment += entry["total"]
    return total_investment


def display_summary(portfolio, total_investment):
    """Print a neat summary table of the portfolio and the final total."""
    print("\n----- Portfolio Summary -----")

    if len(portfolio) == 0:
        print("No stocks were added.")
    else:
        for entry in portfolio:
            print(f"{entry['symbol']:<6} | Qty: {entry['quantity']:<5} "
                  f"| Price: ${entry['price']:<6} | Total: ${entry['total']}")

    print("------------------------------")
    print(f"Total Investment Value: ${total_investment}")
    print("------------------------------\n")


def save_to_file(portfolio, total_investment, filename="stock_portfolio.txt"):
    """Save the portfolio summary and total investment to a text file."""
    with open(filename, "w") as file:  # "w" mode creates/overwrites the file
        file.write("----- Stock Portfolio Report -----\n")

        if len(portfolio) == 0:
            file.write("No stocks were added.\n")
        else:
            for entry in portfolio:
                file.write(f"{entry['symbol']:<6} | Qty: {entry['quantity']:<5} "
                            f"| Price: ${entry['price']:<6} | Total: ${entry['total']}\n")

        file.write("-----------------------------------\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print(f"Portfolio report saved to '{filename}'.")


def main():
    """Main function that runs the stock portfolio tracker program."""
    print("Welcome to the Stock Portfolio Tracker!\n")

    # Show the user which stocks and prices are available
    show_available_stocks(stock_prices)

    # Collect the user's stock choices and quantities
    portfolio = get_portfolio_input(stock_prices)

    # Calculate the total investment value using basic arithmetic
    total_investment = calculate_total_investment(portfolio)

    # Display the summary on the console
    display_summary(portfolio, total_investment)

    # Save the results to a text file for record-keeping
    save_to_file(portfolio, total_investment)


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
