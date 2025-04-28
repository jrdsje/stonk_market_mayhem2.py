# BAD STOCK TRADING APP - DO NOT USE IN REAL LIFE

import random

stocks = {
    "AAPL": 150,
    "GOOG": 2800,
    "TSLA": 720,
    "AMZN": 3400
}

portfolio = {}
money = 10000

def show_menu():
    """
    Displays the main menu options for the stock trading application.
    """
    print("1. View Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit")

def view_stocks():
    """
    Displays the current prices of all stocks, updating each price with a random fluctuation.
    
    Each time this function is called, every stock's price is adjusted by a random integer between -100 and 100, simulating market volatility, and the updated prices are printed.
    """
    for stock, price in stocks.items():
        # Prices fluctuate wildly each time you look
        new_price = price + random.randint(-100, 100)
        stocks[stock] = new_price
        print(f"{stock}: ${new_price}")

def buy_stock():
    """
    Handles the purchase of stocks by prompting the user for a stock symbol and quantity.
    
    If the user has sufficient funds, deducts the total cost from available cash and updates the portfolio with the purchased shares. Prints a confirmation message on success or notifies the user if funds are insufficient.
    """
    global money
    stock = input("Which stock do you want to buy? ")
    qty = int(input("How many shares? "))
    cost = stocks[stock] * qty
    if money >= cost:
        money -= cost
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty
        print(f"Bought {qty} shares of {stock}")
    else:
        print("You broke.")

def sell_stock():
    """
    Sells a specified quantity of owned stock and updates the user's cash balance.
    
    Prompts the user to enter a stock symbol and the number of shares to sell. If the user owns enough shares, the shares are deducted from the portfolio and the proceeds are added to the available cash. If not, an error message is displayed.
    """
    global money
    stock = input("Which stock do you want to sell? ")
    qty = int(input("How many shares? "))
    if stock in portfolio and portfolio[stock] >= qty:
        money += stocks[stock] * qty
        portfolio[stock] -= qty
        print(f"Sold {qty} shares of {stock}")
    else:
        print("You don’t own that much.")

def view_portfolio():
    """
    Displays the user's current stock holdings and available cash balance.
    
    Prints each stock in the portfolio with the number of shares owned, followed by the total cash remaining.
    """
    print("Your portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares")
    print(f"Cash: ${money}")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_stocks()
    elif choice == "2":
        buy_stock()
    elif choice == "3":
        sell_stock()
    elif choice == "4":
        view_portfolio()
    elif choice == "5":
        print("k bye")
        break
    else:
        print("wat")
