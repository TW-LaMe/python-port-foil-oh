rows=input("rows: ")
columns=input("columns: ")
symbol=input("symbol: ")
for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end=" ")
    print()
print("End of the pattern")
print("you made a pattern of", rows, "rows and", columns, "columns with the symbol", symbol)
print("good job")