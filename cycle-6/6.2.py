fn = open('D:\py.txt', 'r')
fn1 = open('D:\write.txt', 'w')
cont = fn.readlines()
for i in range(0, len(cont)):
	if(i%2!=0):
		fn1.write(cont[i])
fn1 = open('D:\write.txt', 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()
