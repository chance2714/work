yk = 'zibiao.txt'
f_finallist = []

with open(yk, encoding = 'gbk')as f:
	f_list = list(f.read())

for j in range(16):
	for i in f_list:
		if (f_list.index(i) - j) % 15 == 0:
			print(i, end = '')
			f_finallist.append(i)

with open('zibiaowancheng.txt', 'w') as f:
	f.write(''.join(f_finallist))