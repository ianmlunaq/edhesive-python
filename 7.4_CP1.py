# 7.4_CP1.py | ian luna | 2020.07.24

outFile = open("books.txt", 'w')

for i in range(10):
    book = input("What is the book's title?: ").upper()
    firstName = input("What is the author's first name?: ").capitalize()
    lastName = input("What is the author's last name?: ").capitalize()

    print()

    entry = book + "\t" + lastName + ", " + firstName
    outFile.write(entry + "\n")

outFile = open("books.txt", 'r')
print(outFile.read())
outFile.close()
