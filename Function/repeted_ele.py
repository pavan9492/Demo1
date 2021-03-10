
in_list = [1,2,3,1,2,3,4,5]
def msg(mylist):
    dict = {}


    for each in mylist:
        if each not in dict.keys():
            dict[each] = 1
        else:
            dict[each] += 1
    print(dict)
msg(in_list)