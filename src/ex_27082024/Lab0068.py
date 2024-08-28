my_shopping_list = ["milk", "bread", "butter"]
# To remove duplicate from the list we use set -> data
print(len(my_shopping_list))
print(my_shopping_list[0])


def bring_more_food(my_list):
    more_item = input("Enter items: ")
    my_list.append(more_item)
    # my_list.remove(more_item)
    # my_list.insert(0, more_item)
    return my_list


l = bring_more_food(my_shopping_list)
print(l)
