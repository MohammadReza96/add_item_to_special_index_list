def add_item_to_special_index_list(args,data,index):
    nelis=[]
    if index>len(args)-1:
        args.append(data)
        return args
    else:
        for item in range(len(args)):
            if item == index:
                nelis.append(data)
                nelis.append(args[item])
            else:
                nelis.append(args[item])
        return nelis


li=[1,2,3,4,5,6,7,8]
print(add_item_to_special_index_list(li,31,9))
print(add_item_to_special_index_list([2,3,4,5],31,1))
