# 寫一個function來計算清單中數字的總數

def sum_of_list(num):
	total = 0
	for l in num:
		total = total + l
	return total

group = []

while True:

	x = input('請輸入要加總數字(輸入完按q)')

	if x == 'q':
		break

	else:
		x = int(x)
		group.append(x)

print(sum_of_list(group))