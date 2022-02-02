M = 1
N = 30
S = 7  # WRN: this Quantity is never used in the task
L = 3
tot_price = (M + N / 100) * L
tot_price_typized = tot_price * 100 // 1 / 100
print("общая цена в рублях и копейках=", tot_price_typized)


