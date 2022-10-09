position = input('what row and column do you want o=to hide your treasure')
treasure = input('type your treasure value')
row1 = ['😀','😀','😀']
row2 = ['😀','😀','😀']
row3 = ['😀','😀','😀']
map= [row1, row2, row3]
new_postion = position.split(',')

if int(new_postion[1]) >= len(map) and int(new_postion[0]) >= len(map):
    new_postion[1] = -1
    new_postion[0] = -1
    map[int(new_postion[0])][int(new_postion[1])] = treasure
elif int(new_postion[0]) >= len(map):
    new_postion[0] = -1
    map[int(new_postion[0])][int(new_postion[1])] = treasure
elif int(new_postion[1]) >= len(map):
    new_postion[1] = -1
    map[int(new_postion[0])][int(new_postion[1])] = treasure

print(map)

