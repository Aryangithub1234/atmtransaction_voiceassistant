if __name__ == '__main__':
    import pyttsx3
    eg = pyttsx3.init()
    voice = eg.getProperty("voices")
    rate = eg.getProperty("rate")
    eg.setProperty("rate",rate+1)
    eg.setProperty("voice",voice[1].id)
    atm1,atm2,atm3 = "State bank of India","Syndicate Bank","Canara Bank"

if 1:
    def SBI_bank():
        eg.say("dear customer enter your SBI pin")
        eg.runAndWait()
        atm_pin = 6397
        ap = int(input(f"enter your {atm1} pin: "))
        if ap != atm_pin:
            eg.say(f"entered {atm1} pin is incorrect")
            eg.runAndWait()
            print(f"entered {atm1} pin is incorrect")
            exit()

        eg.say("what you want to do (deposit) or (withdrawal) or (checkbalance)")
        eg.runAndWait()
        choice = input("what you want to do (deposit,withdrawal,checkbalance): ")

        if choice == "de" :
            eg.say("enter the amount to submit")
            eg.runAndWait()
            cash_deposit = int(input("enter the amount to submit: "))
            eg.say(f"your amount {cash_deposit} rupees has been deposited successfully...")
            eg.runAndWait()
            print(f"your amount {cash_deposit} rupees has been deposited successfully...")
            exit()

        elif choice == "wi" :
            eg.say("how much cash you want to withdrawa")
            eg.runAndWait()
            cash_withdrawal = int(input("how much cash you want to withdrawa: "))
            eg.say(f"your {atm1} transaction is processing....()")
            print(f"your {atm1} transaction is processing....")
            eg.runAndWait()
            eg.say(f"the cash {cash_withdrawal} rupees has been withdrawad sucessfully...")
            eg.runAndWait()
            print(f"the cash {cash_withdrawal} rupees has been withdrawad sucessfully...")
            exit()

        elif choice == "cb" :
            eg.say("how much cash you deposited")
            eg.runAndWait()
            cash_deposit = int(input("how much cash you deposited: "))
            eg.say("how much cash you withdrawad")
            eg.runAndWait()
            cash_withdrawal = int(input("how much cash you withdrawad: "))
            check_balance = cash_deposit - cash_withdrawal
            eg.say(f"your current balance is {check_balance} rupees")
            eg.runAndWait()
            print(f"your current balance is {check_balance} rupees")
            exit()

        else:
            eg.say("oops something went wrong check again...")
            eg.runAndWait()
            print("oops something went wrong check again...")
            exit()

        main()

    def SD_bank():
        eg.say(f"enter your {atm2} pin")
        eg.runAndWait()
        atm_pin = 3847
        ap = int(input(f"enter your {atm2} pin: "))
        if ap != atm_pin:
            eg.say(f"entered {atm2} pin is incorrect")
            eg.runAndWait()
            exit()

        eg.say("what you want to do (deposit) or (withdrawal) or (checkbalance)")
        eg.runAndWait()
        choice = input("what you want to do (deposit,withdrawal,checkbalance): ")

        if choice == "de":
            eg.say("enter the amount to submit")
            eg.runAndWait()
            cash_deposit = int(input("enter the amount to submit: "))
            eg.say(f"your amount {cash_deposit} rupees has been deposited successfully...")
            eg.runAndWait()
            print(f"your amount {cash_deposit} rupees has been deposited successfully...")
            exit()

        elif choice == "wi":
            eg.say("how much cash you want to withdrawa")
            eg.runAndWait()
            cash_withdrawal = int(input("how much cash you want to withdrawa: "))
            eg.say(f"your {atm2} transaction is processing.....()")
            print(f"your {atm2} transaction is processing....")
            eg.runAndWait()
            eg.say(f"the cash {cash_withdrawal} rupees has been withdrawad sucessfully...")
            eg.runAndWait()
            print(f"the cash {cash_withdrawal} rupees has been withdrawad sucessfully...")
            exit()

        elif choice == "cb":
            eg.say("how much cash you deposited")
            eg.runAndWait()
            cash_deposit = int(input("how much cash you deposited: "))
            eg.say("how much cash you withdrawad")
            eg.runAndWait()
            cash_withdrawal = int(input("how much cash you withdrawad: "))
            check_balance = cash_deposit - cash_withdrawal
            eg.say(f"your current balance is {check_balance} rupees")
            eg.runAndWait()
            print(f"your current balance is {check_balance} rupees")
            exit()

        else:
            eg.say("oops something went wrong check again...")
            eg.runAndWait()
            print("oops something went wrong check again...")
            exit()

        main()

    def CANARA_bank():
        eg.say(f"enter your {atm3} pin")
        eg.runAndWait()
        atm_pin = 4758
        ap = int(input(f"enter your {atm3} pin: "))
        if ap != atm_pin:
            eg.say(f"entered {atm3} pin is incorrect")
            eg.runAndWait()
            print(f"entered {atm3} pin is incorrect")
            exit()

        eg.say("what you want to do (deposit) or (withdrawal) or (checkbalance)")
        eg.runAndWait()
        choice = input("what you want to do (deposit,withdrawal,checkbalance): ")

        if choice == "de":
            eg.say("enter the amount to submit")
            eg.runAndWait()
            cash_deposit = int(input("enter the amount to submit: "))
            eg.say(f"your amount {cash_deposit} rupees has been deposited successfully...")
            eg.runAndWait()
            print(f"your amount {cash_deposit} rupees has been deposited successfully...")
            exit()

        elif choice == "wi":
            eg.say("how much cash you want to withdrawa")
            eg.runAndWait()
            cash_withdrawal = int(input("how much cash you want to withdrawa: "))
            eg.say(f"your {atm3} transaction is processing.....()")
            print(f"your {atm3} transaction is processing....")
            eg.runAndWait()
            eg.say(f"the cash {cash_withdrawal} rupees has been withdrawad sucessfully...")
            eg.runAndWait()
            print(f"the cash {cash_withdrawal} rupees has been withdrawad sucessfully...")
            exit()

        elif choice == "cb":
            eg.say("how much cash you deposited")
            eg.runAndWait()
            cash_deposit = int(input("how much cash you deposited: "))
            eg.say("how much cash you withdrawad")
            eg.runAndWait()
            cash_withdrawal = int(input("how much cash you withdrawad: "))
            check_balance = cash_deposit - cash_withdrawal
            eg.say(f"your current balance is {check_balance} rupees")
            eg.runAndWait()
            print(f"your current balance is {check_balance} rupees")
            exit()

        else:
            eg.say("oops something went wrong check again...")
            eg.runAndWait()
            print("oops something went wrong check again...")
            exit()

        main()

    def main():
        eg.say("which bank account you want to choose (state bank of india) or (syndicate bank) else (canara bank)")
        eg.runAndWait()
        choices = input("which bank account you want to choose? ")
        if choices == "sbi":
            eg.say(f"you choosed {atm1}")
            eg.runAndWait()
            SBI_bank()
        elif choices == "sdb":
            eg.say(f"you choosed {atm2}")
            eg.runAndWait()
            SD_bank()
        elif choices == "cnb":
            eg.say(f"you choosed {atm3}")
            eg.runAndWait()
            CANARA_bank()
        else:
            eg.say("choice is incorrect , ensure to select right choice")
            eg.runAndWait()
            print("choice is incorrect , ensure to select right choice")
    main()