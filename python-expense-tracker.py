#EXPENSE TRACKER

expense=[]
while True:
    category=input("ENTER THE CATEGORY")
    amount=int(input("ENTER THE AMOUNT:"))
    expense.append({"amount":amount,"category":category})
    if input("Continue?yes/no:")!="yes":
        break
category_total={}
for e in expense:
    cat=e["category"]
    category_total[cat]=category_total.get(cat,0)+e["amount"]
    print("CATEGORY TOTAL:",category_total)
