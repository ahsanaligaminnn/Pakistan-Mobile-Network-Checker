#Pakistan Mobile Network Checker:
print(r"""
+------------------------------------------------------------------------------+
| ____       _    _     _                __  __       _     _ _                |
||  _ \ __ _| | _(_)___| |_ __ _ _ __   |  \/  | ___ | |__ (_) | ___           |
|| |_) / _` | |/ / / __| __/ _` | '_ \  | |\/| |/ _ \| '_ \| | |/ _ \          |
||  __/ (_| |   <| \__ \ || (_| | | | | | |  | | (_) | |_) | | |  __/          |
||_|  _\__,_|_|\_\_|___/\__\__,_|_| |_| |_| _|_|\___/|_.__/|_|_|\___|          |
|| \ | | ___| |___      _____  _ __| | __  / ___| |__   ___  ___| | _____ _ __ |
||  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ / | |   | '_ \ / _ \/ __| |/ / _ \ '__||
|| |\  |  __/ |_ \ V  V / (_) | |  |   <  | |___| | | |  __/ (__|   <  __/ |   |
||_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\  \____|_| |_|\___|\___|_|\_\___|_|   |
+------------------------------------------------------------------------------+
    """)  
while True:
    
    phone = input("Enter Phone Number : ")
    print()

    #Ufone_Number Checker:
    if phone.startswith("0330") or phone.startswith("0331") or phone.startswith("0332") or phone.startswith("0333") or phone.startswith("0334") or phone.startswith("0335") or phone.startswith("0336") or phone.startswith("0337") or len(phone) == 13:
        print(f"{phone} : Ufone Number.\n")

    #ZongNumber Checker:
    elif  phone.startswith("0310") or phone.startswith("0311") or phone.startswith("0312") or phone.startswith("0313") or phone.startswith("0314") or phone.startswith("0315") or phone.startswith("0316")  or len(phone) == 13:
        print(f"{phone} : Zong Number.\n")

    #Telenor_Number Checker:
    elif phone.startswith("0340") or phone.startswith("0341") or phone.startswith("0342") or phone.startswith("0343") or phone.startswith("0344") or phone.startswith("0345") or phone.startswith("0346") or phone.startswith("0347") or len(phone) == 13:
        print(f"{phone} : Telenor Number.\n")

    #Warid/Jazz_Number Checker  
    elif phone.startswith("0320") or phone.startswith("0321") or phone.startswith("0322") or phone.startswith("0323") or phone.startswith("0324") or phone.startswith("0325") or phone.startswith("0326") or phone.startswith("0327") or phone.startswith("0328") or len(phone) == 13:
        print(f"{phone} : Warid/Jazz ranges (now used by Jazz).\n")

    #Jazz/Mobilink_Number Checker
    elif phone.startswith("0300") or phone.startswith("0301") or phone.startswith("0302") or phone.startswith("0303") or phone.startswith("0304") or phone.startswith("0305") or len(phone) == 13:
        print(f"{phone} : Jazz/Mobilink Number.\n")

    #exit
    elif phone.lower() == "exit":
        print("Thnakyou for using.")
    
        break
    #Invalid_command
    else:
        print("Invalid Command.")

