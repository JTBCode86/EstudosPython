# Lista de itens que o Roberto já possui na despensa
itens_despensa = ["arroz", "feijão", "macarrão", "óleo", "sal"]

# Solicita ao usuário o item que deseja verificar
item_procurado = input("Digite o item que você quer verificar: ").strip().lower()

# Verifica se o item está na lista
if item_procurado in itens_despensa:
    print(f"O item {item_procurado} já está na despensa.")
else:
    print(f"O item {item_procurado} precisa ser comprado.")