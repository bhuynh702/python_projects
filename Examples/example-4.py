access_list = [17, 1728, 14, 25, 81, 343]
print(access_list)
print(access_list[0],access_list[3], access_list[5])
loop_list = [1, 5, 10, 12, 17, 19, 31, 33, 47, 52]
for value in loop_list:
    print(value,end='')

word_list = ['trap','stamp','injure','plane','carrot']
for word in word_list:
    if 'a' in word: 
        print('The word', word,'has an a in it.')
