cliente = str(input("Entró un cliente? (si/no):"))
clientes_activos = 0
contador = 0
total_clientes = 0
clientes_inactivos = 0
producto = 0
saúco = 0
espino = 0
sauce = 0
acebo = 0
while cliente == "si": 
  compra = str(input("Compra algo?  (si/no): "))
  if compra == "si":
    clientes_activos+= 1
    producto = str(input("Que compro?  Varita de sauco [1] Varita de espino [2]  Varita de sauce [3]  Varita de acebo [4]" ))

    if producto == "1":
       saúco += 1
    elif producto == "2":
       espino += 1
    elif producto == "3":
       sauce += 1
    elif producto == "4":
       acebo += 1
    cliente = str(input("Entró un cliente? (si/no): "))
    total_clientes += 1
    clientes_inactivos = total_clientes - clientes_activos
    print(f"Los clientes que compraron productos son {clientes_activos}")
    print(f"Los clientes que no compraron {clientes_inactivos}")
    print(f"El total de clientes sería {total_clientes}")
    print(f"Las varitas de sauco son {saúco}, las varitas de espino son {espino}, las varitas de sauce son {sauce}, las varitas de acebo son {acebo}")
