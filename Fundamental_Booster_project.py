print("----Welcome to Interactive Personal Data Collector..!!----")
print("\n")

name= str(input("Enter your name: "))
age= int(input("Enter your age in current year (i.e, 2026): "))
height= float(input("Enter your height in meters: "))
city= str(input("Enter the city you live in: "))
phone= int(input("Enter your phone number: "))
fav_num= int(input("Enter your favourite number: "))
print("\n")

print("----Thank you for providing the details----")
print("\n")
print("Here's the information that we collected:-")

n= type(name)
nid= id(name)
print(f"Name:{name} (Type={n}, Memory Address={nid})")

a= type(age)
aid= id(age)
print(f"Age:{age} (Type={a}, Memory Address={aid})")

h= type(height)
hid= id(height)
print(f"Height:{height} (Type={h}, Memory Address={hid})")

c= type(city)
cid= id(city)
print(f"City:{city} (Type={c}, Memory Address={cid})")

p= type(phone)
pid= id(phone)
print(f"Phone Number:{phone} (Type={p}, Memory Addrres={pid})")

fn= type(fav_num)
fnid= id(fav_num)
print(f"Favourite number:{fav_num} (Type={fn}, Memory Address={fnid})")
print("\n")

current_year= 2026
birth_year= current_year - age
print(f"Your birth year is approximately: {birth_year} (based on your given age= {age})")
print("\n")

print("----Thank you for using Interactive Personal Data Collector:)----")