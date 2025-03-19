'''
#1)
word = "this is javascript"
letter = "i"
result = [i for i, c in enumerate(word) if c == letter]
print(result)
'''

'''
#2)
def multi_table(number):
  table = []
  for i in range(1, number + 1):
    row = []
    for j in range(1, i + 1):
      row.append(i * j)
    table.append(row)
  return table

number = 3
multiplication_table = multi_table(number)
print(multiplication_table)
'''

'''
#3)
def groupNames(names):

  name_dict = {}
  for name in names:
    first_letter = name[0].lower() 
    if first_letter in name_dict:
      name_dict[first_letter].append(name)
    else:
      name_dict[first_letter] = [name]


  sorted_dict = dict(sorted(name_dict.items())) 

  return sorted_dict

names = ["ahmed", "lila", "youssef"]
result = groupNames(names)
print(result)
'''