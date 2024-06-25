f = open("test.ini")
folders = f.readlines()
for folder in folders:
    print(folder.replace("\n", "").replace("\\", "/"))

# C:/Users/fujimichang/Documents
# C:/Users/fujimichang/Downloads
# C:/Users/fujimichang/Pictures