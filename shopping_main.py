import sys
import csv

def order_shopping_list(shopping_list):
    """
    Returns a dictionary containing a shopping list sorted by
    store, type, item. Takes a csv file as an argument.
    """
    shop_dict = {}
    with open(shopping_list) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            store, item_type, item = row[2].lower(), row[1].lower(), row[0].lower()
            # if the store dict hasn't been created, create it.
            if not store in shop_dict:
                shop_dict.update({store:{}})
            # if the item_type dict hasn't been created, create it.
            if not item_type in shop_dict[store]:
                shop_dict[store].update({item_type:[]})
             # Add the item to the item_type list.
            shop_dict[store][item_type].append(item)
        return shop_dict

def print_shopping_list(shop_dict):
    """
    Prints a formatted shoping list.
    Called with a shopping_list dictionary.
    """
    print("\n")
    for store, item_type in shop_dict.items():
        under_store = "#" * len(store)
        print("{}\n{}\n".format(store.upper(), under_store))
        for i_type, items in item_type.items():
            under_i_type = "-" * len(i_type)
            print("{}\n{}".format(i_type.title(), under_i_type))
            for item in items:
                print(item)
            print("\n")



if __name__ == "__main__":
    file = sys.argv[1]
    print_shopping_list(order_shopping_list(file))
