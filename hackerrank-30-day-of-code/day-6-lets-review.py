def process(input_string):
	odd = ''
	even = ''

	for i in range(0, len(input_string)):
		if i % 2 == 0:
			odd += input_string[i]
		else:
			even += input_string[i]
	
	return odd, even

if __name__ == '__main__':
	cnt = input()

	for i in range(int(cnt)):
		answer = process(input())
		print(answer[0] + ' ' + answer[1])