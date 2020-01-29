#hiring ppl for companies

skillset=str(input("tell us your skillset: "))
project=int(input("enter the number of projects you have completed: "))
if skillset=="python" or skillset=="c" and project>=2:
    print("you have place in EVERY INDIA COMPANY")
elif skillset=="java" or skillset=="python" and project>=3:
    print("you can place in TCS COMPANY")
elif skillset=="c" or skillset=="java" and project>=4:
    print("you can place in INFOSYS COMPANY")
elif skillset=="c++" or skillset=="C" and project>=5:
    print("you can place in ZOHO COMPANY")
else:
    print("you cannot place in any company")
