file = open("msgs.txt")
lines = file.readlines()
cleaned = ""
for line in lines:
    if not line.startswith("rat with constipation☆ —"):
        cleaned += line

print(cleaned)