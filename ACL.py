ACL = int(input("¿Cuál es el número IPV4 ACL?"))
if ACL >= 1 and ACL <=99:
    print ("Este es un ACL IPV4 estándar.")
elif ACL >=100 and ACL <=199:
    print("Este es una ACL IPV4 extendida.")
else:
    print("El nùmero ingresado no corresponde a una lista de acceso.")
