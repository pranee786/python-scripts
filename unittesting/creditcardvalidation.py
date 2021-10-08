from datetime import *

def validateCard(expiryDate):
    if expiryDate >= datetime.now().date():
        return "Valid"

    else:
        raise RuntimeError("Card has expired")

#print(validateCard(date(2021,10,31)))
