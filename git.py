class color:
   YELLOW = '\033[93m'
   END = '\033[0m'
step = 0
arr_of_num = []
while step < 6:
    input_number = int(input(color.YELLOW + 'Enter you number: ' + color.END))
    arr_of_num.append(input_number)
    step += 1
arr_of_num = sorted(arr_of_num)
print(*arr_of_num, sep=', ')
