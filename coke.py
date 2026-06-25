
amount_due = 50
accepted_coins = [25,10,5]
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        amount_due -= coin
    else:
        continue

# 4. Calculate change owed once the loop ends
# If amount_due is negative (e.g., -5), the absolute value turns it into positive change (5)
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")
