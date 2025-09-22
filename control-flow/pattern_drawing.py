# size = int(input("Enter the size of the pattern: "))
# max = size
# while size>0:
#     print("* "* max)
#     size = size-1


while True:
    size = int(input("Enter the size of the pattern: "))
    for i in range(size):
        print("* " * size)
