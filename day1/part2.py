def main():
	data = []
	with open('input.txt', 'r') as f:
		for i in f.read().splitlines():
			data.append(int(i))

	count = 0
	for index in range(len(data)):
		try:	
			if data[index] + data[index+1] + data[index+2] > data[index-1] + data[index] + data[index+1]:
				count+=1
		except:
			pass		

	print(count)

if __name__ == '__main__':
	main()