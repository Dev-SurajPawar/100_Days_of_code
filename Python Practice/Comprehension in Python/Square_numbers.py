num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squared_num = [n*n for n in num]
squared_num = [n**2 for n in num]
print(squared_num)


even_num = [n for n in num if n%2==0 ]
print(even_num)