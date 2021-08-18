# List to Dictionary Function for Fantasy Game Inventory
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory

# Display Inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)