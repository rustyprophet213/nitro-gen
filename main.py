import random, string, os

ans=True
while ans:
    
    print("Dicord nitro generator by ! Inferno#7511")
    print("1. Generate Nitro Codes" + os.linesep + "2. Exit")
    

    
    ans= input("What would you like to do? ")


    if ans == "1":
        
        def gen():
            lim = int(input("Enter amount of codes: "))
            for i in range(0, lim + 1):
                x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
                print("discord.gift/", x, sep='')
        gen()
        
    elif ans == "2":
        break
