items = ["pen","book","bag"]
prices = [10,50,200]
for i in range(3):
    print(items[i], "costs", prices[i])


for i in range(3):
    if prices[i] > 20:
        print(items[i], "is expensive")
    else:
        print(items[i], "is cheap")