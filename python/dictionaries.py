capitals = {"China" : "Beijing",
            "USA" : "Washington DC",
            "France" : "Paris"}
capitals.update({"Germany" : "Berlin"})
#capitals.pop("USA")
#capitals.popitem()
#capitals.clear()
keys = capitals.keys()
#print(keys)

#for i in capitals.values():
    #print(i)
for key, value in capitals.items():
    print(f"{key}, {value}")