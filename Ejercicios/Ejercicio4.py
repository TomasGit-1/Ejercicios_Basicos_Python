ttCompra=float(input("Ingrese el total de la compra "))
if ttCompra<500:
    preFinal=ttCompra
elif ttCompra<=1000:
    preFinal=ttCompra-(ttCompra*0.05)
elif ttCompra<=7000:
    preFinal=ttCompra-(ttCompra*0.11)
elif ttCompra<=15000:
    preFinal=ttCompra-(ttCompra*0.18)
else:
    preFinal=ttCompra-(ttCompra*0.25)
print(f"Total a pagar ={(preFinal)}")