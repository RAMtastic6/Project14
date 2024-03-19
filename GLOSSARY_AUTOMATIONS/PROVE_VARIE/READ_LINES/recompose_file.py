f = open("uc1_1.tex", "r")

content = f.read()

lines = content.split("\n")
print(lines)

new_content = ""
for l in lines:
    new_content+=l + "\n"
new_content = new_content.rstrip("\n")


print(content == new_content)