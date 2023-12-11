

phone = {"kim" : "111", "lee":"222", "park":"333"}
print("kim" in phone)
print("kang" not in phone)
p = phone

p["kang"] = "123"
print(phone)
print(p)
print(id(phone), id(p))







