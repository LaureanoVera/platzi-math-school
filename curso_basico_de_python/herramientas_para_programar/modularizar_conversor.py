def conversor(coin_type, usd_value):
    coin = input(f"How many {coin_type} do you have?: ")
    coin = float(coin)

    usd_total = round(coin / usd_value, 2)

    print(f"You have {usd_total} USD")


menu = """
Welcome to the currency converter
1 - ARS
2 - MXN
3 - COL
Choose an option: """

option = input(menu)


if option == "1":
    conversor("ARS", 102.96)
elif option == "2":
    conversor("MXN", 20.55)
elif option == "3":
    conversor("COL", 4064.83)
else:
    print("Choose a correct option.")
