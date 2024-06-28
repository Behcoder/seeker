###################### cleaner ###################################
def cleaner():
    from os import system
    system('cls')

# cleaner()
###################### sleeper ###################################
def sleeper():
    from time import sleep
    sleep(1)

# sleeper()
###################### chap ######################################
def chap(num:int, text:str):
    print(f"{num} => {text}")

# chap(1, "reading from myList")
###################### miladi to shamsi ##########################
from persiantools.jdatetime import JalaliDate

def miladi_to_shamsi(year, month, day):
    jalali_date = JalaliDate.to_jalali(year, month, day)
    return jalali_date

result = miladi_to_shamsi(2024, 6, 23)

# print(f"shamsi tarikh --> {result}")
######################  ###################################

