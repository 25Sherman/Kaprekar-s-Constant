#
#
#
# Work of Milan Grewal
#
#
#


num = -1
while num < 0 or num > 9999:
  num = int(input("Enter a four-digit integer:"))


num = str(num)

if num[::1] == num[::-1] and len(num) == 4:
  print(f"{num} > 0")
  print(f"{num} reaches 0 via Kaprekar's routine in 1 iterations")
  quit()


orignal_val = num
#add zeros if needed
zeros = 0
if len(num) < 4:
  zeros = 4 - len(num)
  num = (zeros) * "0" + num

answer = 0
num_lst_str = []
num_lst_int = []
higher = []
lower = []
h_val = ''
l_val = ''


for strg in num:
  num_lst_str.append(strg)



for strg in num_lst_str:
  num_lst_int.append(int(strg))


lower = sorted(num_lst_str)
higher = sorted(num_lst_str, reverse = True)

#create value
for num in higher:
  h_val += num
h_val = int(h_val)

for num in lower:
  l_val += num
l_val = int(l_val)



hold_vals = []
counter = 0

#loop to repeat process till it reaches 6174  
while answer != 6174:
  
  answer = h_val - l_val
  h_val = ''
  l_val = ''
  hold_vals.append(answer)
  new_num = str(answer)

  if len(new_num) < 4:
    zeros = 4 - len(new_num)
    new_num = (zeros) * "0" + new_num

  num_lst_str = []
  for strg in new_num:
    num_lst_str.append(strg)

  num_lst_int = []
  for strg in num_lst_str:
    num_lst_int.append(int(strg))

  lower = sorted(num_lst_str)
  higher = sorted(num_lst_str, reverse = True)

  #create value
  for new_num in higher:
    h_val += new_num
  h_val = int(h_val)

  for new_num in lower:
    l_val += new_num
  l_val = int(l_val)
  
  counter +=1


print_arrow = orignal_val
for x in hold_vals:
  print_arrow += " > " + str(x)
print(print_arrow)

print(f"{orignal_val} reaches 6174 via Kaprekar's routine in {counter} iterations")