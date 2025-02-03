def reverse_list(list_to_reverse):
    list_to_reverse.reverse()
    return list_to_reverse

campingSupplies = ['tent','sleeping bag','flash light','camping knife']
reversed_supplies = reverse_list(campingSupplies)
print(reversed_supplies)

def add_item(list_to_add_to, item_to_add):
    list_to_add_to.append(item_to_add)
    return list_to_add_to

campingSupplies = ['tent','sleeping bag','flash light','camping knife']
campingSupplies = add_item(campingSupplies, 'first-aid kit')
print(campingSupplies)

def combine_lists(campingSupplies campingFood):
    return campingSupplies + campingFood

campingSupplies = ['tent','sleeping bag','flash light','camping knife']
campingFood = ['marshmellows','gram crackers','chocolate','chicken hot dogs','water']
combined_list = combine_lists(campingSupplies, campingFood)
print(combined_list)

def replace_item(list_to_modify, item_to_remove, item_to_add):
    try:
        index = list_to_modify.index(item_to_remove)
        list_to_modify[index] = item_to_add
    except ValueError:
        print("Item '{item_to_remove}' not found in the list.")
    return list_to_modify

campingSupplies = ['tent','sleeping bag','flash light','camping knife']
campingSupplies = replace_item(campingSupplies, 'flash light', 'camp fire kit')
print(campingSupplies) 