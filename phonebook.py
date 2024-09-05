phonebook={"arun" : {"name" :"arun" ,"phone":9876543210 },"jay":{"name" :"jay" ,"phone":9898987650 }}
print(phonebook)


phonebook.update({"jay" : {"name":"jay","phone" : 8765432798}})       
print(phonebook)

phonebook["age"] = {"arun":23},{"jay":20}    
print(phonebook)

del phonebook["age"]
print(phonebook)