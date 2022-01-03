ars = input("How many ARS do you have?: ")
ars = float(ars)

usd_value = 102.96
usd_total = round(ars / usd_value, 2)

print(f"You have {usd_total} USD")
