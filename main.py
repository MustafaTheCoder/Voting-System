from playsound import playsound

print("""
=========== Music Player =========== 
[1] Play Music
[2] Quit 
====================================   
""")



while True:
    user_inp = int(input("Option: "))

    if user_inp == 1:
        path = input("File Path: ")
        print("Playing Audio...")
        playsound(path)
        
    else:
        break    