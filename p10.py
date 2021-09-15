# wapp to find the sum and avg of 3 numbers
def compute(n1,n2,n3):
	sum = n1+n2+n3
	avg = n1+n2+n3/3
	print("sum = ", round(sum,2))
	print("avg= ", round(avg,2))
n1= float(input("enter first num"))
n2= float(input("enter second num"))
n3= float(input("enter third num"))
compute(n1,n2,n3)


