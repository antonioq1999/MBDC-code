class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def __init__(self, philospher, book) -> None:
        self.philosopher = philospher
        self.book = book
        
    def hand_list(self):
        print(str(self.philosopher) + " wrote the book: " + str(self.book))

whodunnit = MyFirstClass("Sun Tzu", "The Art of War")

print(whodunnit.hand_list())

# Check answer01.py for coursera solution