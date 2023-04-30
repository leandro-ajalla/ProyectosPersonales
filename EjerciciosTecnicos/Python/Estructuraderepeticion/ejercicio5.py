while True:
    print("que emoticon dibujo?")
    print("1. feliz") 
    print("2. triste")
    print("3. guiño")
    print("4. esceptico")
    print("0. finalizar")
    emoticon = int(input("> "))
    if emoticon == 1:
        print(":)")
    else:
        if emoticon == 2:
            print(":(")
        else:
            if emoticon == 3:
                print(";)")
            else:
                if emoticon == 4:
                    print(":|")
                else:
                    if emoticon == 0:
                        print("-- hasta luego!! --")
                        break
                