import datetime
name= input("Name")
htown=input("Hometown")
hobby=input("Hobby") 
ffact=input("Fun fact")
doy=int(input("Birthyear"))
ty=datetime.date.today().year
text = f"PROFILE: {name}"
width = len(text) + 8
print("\u2554" + "═" * width + "\u2557")
print("    " + text)
print("\u255A" + "═" * width + "\u255D")
print("Hometown:",htown)
print("Hobby:",hobby)
print("Fun fact:",ffact)
print("Age:",ty-doy)
