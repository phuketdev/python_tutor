def fee(amt):
    if amt <= 5000:
        return 0
    elif 5000 <= amt <= 30000:
        return 2
    elif 30000 <= amt <= 100000:
        return 5
    else:
        return 10

def fee2(amt): # เงื่อนไขแบบตรวจสอบจากค่ามากไปน้อย
    if amt > 100000:
        fee = 10
    elif amt > 30000:
        fee = 5
    elif amt > 5000:
        fee = 2
    else:
        fee = 0
    print("Fee: ", fee)

# print(fee(200000))
amt = float(input("Transfer amount: "))

if __name__ == '__main__':
    fee2(amt)