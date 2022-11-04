class pyt:
    def multiplication_table(n):
        for i in range(2, n + 1):
            for j in range(1, 11):
                print(i, "*", j, "=", i * j)
            print()

    n = int(input('Enter the number: '))
    multiplication_table(n)


p = pyt()
