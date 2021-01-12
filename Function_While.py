def compare_numbers(a, b, v):
    while a <= b:
        print("Value of A(" + str(a) + ") is less than b or equal")
        a = a + v
    print("Final A is " + str(a) + " waited")


compare_numbers(1, 15, 2)
