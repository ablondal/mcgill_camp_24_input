## INPUT ##
###########

n, m, k = map(int, input().split())

current_books = [("Jane Eyre", k)]
future_books = []

for i in range(n):
	book_line = input()
	_, book_name, length = book_line.split('"')
	length = int(length)
	current_books.append((book_name, length))

for j in range(m):
	book_line = input()
	pre_time, book_name, length = book_line.split('"')
	length = int(length)
	pre_time = int(pre_time)
	future_books.append((pre_time, book_name, length))

# current_books is a list of elements (<name of book>, <length of book>)
# future_books is a list of elements (<time of book arrival>, <name>, <length>)

## SOLUTION ##
##############


