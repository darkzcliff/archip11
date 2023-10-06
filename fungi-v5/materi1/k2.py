items = [106, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

store_float = ()
store_str = []
store_dict = {"satuan": [], "puluhan": [], "ratusan": []}

for item in items:
    if isinstance(item, float):
        store_float += (item,)
    elif isinstance(item, str):
        store_str.append(item)
    elif isinstance(item, int):
        if item <= 9: store_dict["satuan"].append(item)
        elif item >= 10 and item <= 99: 
            store_dict["puluhan"].append(item)
        elif item >= 100 and item <= 999:
            store_dict["ratusan"].append(item)

print("Float: ", store_float)
print("Str: ", store_str)
print("Dict: ", store_dict["satuan"], store_dict["puluhan"], store_dict["ratusan"])