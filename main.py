import sqlite3, json ,ctypes
from pick import pick

# This is my first open-source project. Be nice please :<

# When we're working with restricted paths such as 
# Program Files or Program Files, we need to be elevated
# In order to edit files in that directory. And with
# Default installations, WuWa is installed in Program Files
# So we need to be elevated to edit the LocalStorage.db file

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# function to check for Adimnistrator privileges.
# Which unfortunately means this script doesn't work on Linux
# Maybe soon?
if is_admin(): 
    # Selector for FrameRate and Input for the game folder's path
    framerateOptions = [60, 120, 144, 165, 240, "Unlimited"]
    filePath = input("Enter game path (Wuthering Waves Game): ")

    # Replaces backslashes with forward slashes
    filePath = filePath.replace("\\", "/")

    # Adds a trailing slash if neccessary
    if filePath[-1] != "/":
        filePath += "/"

    # basically opens the LocalStorage.db file
    conn = sqlite3.connect(filePath + "Client/Saved/LocalStorage/LocalStorage.db")
    c = conn.cursor()


    framerate, index = pick(framerateOptions, "Select a framerate: ")
    if framerate == "Unlimited":
        framerate = 1000

    # Selects the GameQualitySetting row from the LocalStorage table
    c.execute("SELECT * FROM LocalStorage WHERE key = 'GameQualitySetting'")
    row = c.fetchone()

    # Edit the JSON object that represents the Framerate Cap
    jsonValue = json.loads(row[1])
    jsonValue["KeyCustomFrameRate"] = framerate

    
    # Saves the updated JSON object back to the Database file
    c.execute("UPDATE LocalStorage SET value = ? WHERE key = 'GameQualitySetting'", (json.dumps(jsonValue),))
    conn.commit()
    conn.close()

    # This is just for console output. This doesn't do anything to the in game framerate.
    framerate = "Unlimited" if framerate == 1000 else framerate

    # More console stuff.
    print("Framerate set to", framerate)
    print("Please restart the game for the changes to take effect.")
    input("Press Enter to exit.")
else:
    # Exit the script if not elevated. 
    print("Please run this program as an administrator.")
    input("Press Enter to exit.")
    exit()
