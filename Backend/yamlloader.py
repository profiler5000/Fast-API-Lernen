try:
    import yaml
except:
    print("Konte nicht geladen werden")
with open("Backend/users.yaml") as userFile:
    try:
        get_data = yaml.safe_load(userFile)
    except:
        print("Userfile not found")
        
if get_data:
    data = userFile["Users"]
    