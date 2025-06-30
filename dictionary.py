user_dictionary = {
    "username": "benTsai",
    "name": "Ben",
    "age": 31,
}

user_dictionary["married"] = True
# print(user_dictionary.get("username"))  # benTsai
# print(len(user_dictionary))  # 4
# print(user_dictionary)
# user_dictionary.pop("married")
# user_dictionary.clear()
# print(user_dictionary)

for key, value in user_dictionary.items():
    print(key, value)

# 要記得，python 的 dictionary 也是指向記憶體位置，所以如果想要複製一個 dictionary，需要使用 copy

# user_dictionary2 = dictionary # 這會指向同一個記憶體位置

user_dictionary2 = user_dictionary.copy()
print(user_dictionary2)
