book = []
count = int(input("Enter number of books"))
for i in range(0, count):
    bkname = input("Enter the book name")
    aname = input("Enter the author name")
    price = input("Enter the price")
    details = {"Bookname" : bkname, "Author name" : aname, "Price of book" : price}
    book.append(details)

print(book)