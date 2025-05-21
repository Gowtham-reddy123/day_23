a=int(input("enter the element 1 :"))
b=int(input("enter the element 2 :"))
c=int(input("enter the element 3 :"))
def max_val(a,b,c):
	if a>b and a>c:
		print("a is maximum")
	if b>a and b>c:
		print("b is maximum")
	else:
		print("c is maximum")
max_val(a,b,c)
