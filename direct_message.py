
import os
while True:
    print("                 \033[28mDirect message sender\033[28m  ")
    print("          CHOOSE COUNTRY YOU WANNA SEND MESSAGE TO")
    print("OPTION 1...INDIA")
    print("OPTION 2...PAKISTAN")
    print("OPTION 3...AMERICA")
    print("OPTION 4...CANADA")
    print("OPTION 5...GERMANY")
    print("OPTION 6...UNITED KINGDOM")
    print("OPTION 7...CUSTOM")
    q=input("\n\nENTER OPTION ==>>> ")

    while True:
        number = input("ENTER THE PHONE NUMBER===>>> ").replace(" ", "")
        if not len(number)==10:
            print("\n           Please enter a correct number ..!\n")
            print("           ENTER VALID 10 DIGIT NUMBER\n\n")
        else:
            break

    if (q=="india" or q=="1"):
        new_number="+91"+number
    elif (q=="pakistan" or q=="2"):
        new_number="+92"+number
    elif (q=="america" or q=="3"):
        new_number="+1"+number
    elif (q=="canada" or q=="4"):
        new_number="+1"+number
    elif (q=="germany" or q=="5"):
        new_number="+49"+number
    elif (q=="united kingdom" or q=="6"):
        new_number="+44"+number
    elif (q=="custom" or q=="7"):
        custom_code=input("\n\nENTER COUNTRY CODE==>>>")
        if custom_code.startswith("+"):
            new_number=custom_code+number
        else:
            new_number="+"+custom_code+number
    else:
        print("ERROR!!!")


    text_sent=input("ENTER THE MESSAGE===>>>")


    whatsapp='https://api.whatsapp.com/send?phone=' +new_number + '&text=' +text_sent
    os.system("xdg-open"+whatsapp)
    os.system("clear")
    print("                    \033[1mDONE !!!!\033[1m")
    print("\033[91m                   |---------|\033[91m")
    print("\033[0m\033[0m")
