a=list(input("enter the list elements :"))
total=0
for x in a:
	total=total+int(x)
avg=total/len(a)
print("Average",avg)
