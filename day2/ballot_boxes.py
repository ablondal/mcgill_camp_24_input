## INPUT ##
###########

integers = list(map(int, open(0).read().split()))

# Inputting input on terminal, you will need to
# 	press CTRL+D to end the input.
# This is needed, as the "constant factor" of
# 	reading from input over and over is high.
# Instead, we read the entire input once,
# 	and then parse it.

i = 0
cases = []
while integers[i] != -1:
	n, b = integers[i:i+2]
	cities = integers[i+2:i+2+n]
	i += 2+n
	cases.append( [n, b, cities] )

## SOLUTION ##
##############


