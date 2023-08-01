from info import getINFO
import os

os.system("cls")
print()

pseria = input("(AD1234567) Passport seriya raqam: ")
pdate = input("(01.01.2001) Tug'ilgan sana: ")

# os.system("cls")
print()

payload = {
    "passport": pseria,
    "pin": "",
    "passport_type": 1,
    "birth_date": pdate,
    "type": "young"
}

getinfo = getINFO(payload)
if len(getinfo["result"]) > 0:
    citizen = getinfo["result"]['citizen']
    jshir = citizen['pPinpp']
    surename = citizen['pPatronym']
    firstname = citizen['pName']
    lastname = citizen['pSurname']
    sex = citizen['pSex']
    jins = "ERKAK" if sex  else "AYOL"
    print(f"""
          JSHIR: {jshir}
          PASPORT SERIYA RAQAMI: {pseria}
          
          ISMI: {firstname}
          FAMILYASI: {lastname}
          OTASI: {surename}
          TUGILGAN SANASI: {pdate}
          JINSI: {jins}
          """)
else:
    print(getinfo['msg'])
