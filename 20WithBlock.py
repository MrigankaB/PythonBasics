
with open("16text.txt") as f:     # f= open("16text.txt")
    print(f.tell())
    print(f.readline())
    f.seek(0)
    print(f.tell())
    print(f.readline())
    f.close()


# comment ctrl+/