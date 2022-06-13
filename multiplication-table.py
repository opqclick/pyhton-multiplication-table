from tkinter.tix import MAX


num = int(input("What multiplication table you want? "))
mx = [(x+1) * num for x in range(20)]

print(mx)