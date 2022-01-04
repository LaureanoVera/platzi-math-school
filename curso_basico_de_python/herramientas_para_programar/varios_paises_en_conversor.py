menu = """
Welcome to the currency converter
1 - ARS
2 - MXN
3 - COL
Choose an option: """

option = input(menu)

if option == "1":
    ars = input("How many ARS do you have?: ")
    ars = float(ars)

    usd_value = 102.96
    usd_total = round(ars / usd_value, 2)

    print(f"You have {usd_total} USD")
elif option == "2":
    mxn = input("How many MXN do you have?: ")
    mxn = float(mxn)

    usd_value = 20.55
    usd_total = round(mxn / usd_value, 2)

    print(f"You have {usd_total} USD")
elif option == "3":
    col = input("How many COL do you have?: ")
    col = float(col)

    usd_value = 4064.83
    usd_total = round(col / usd_value, 2)

    print(f"You have {usd_total} USD")
else:
    print("Choose a correct option.")
