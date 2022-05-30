def validate_pin(dig):
    if dig == 4:
        print("Su PIN es correcto, posee", dig, "dígitos")
        return True
    elif dig == 6:
        print("Su PIN es correcto, posee", dig, "dígitos")
        return True
    else:
        print("Su PIN es INCORRECTO, debe poseer 4 o 6 dígitos, NO:", dig, "dígitos")
        return False

ask = int(input("Indique su PIN: "))
dig = len(str(ask))
print (validate_pin(dig))




