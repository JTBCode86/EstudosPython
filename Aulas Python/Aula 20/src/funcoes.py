def organizar_notas_escola():
    print("--- Sistema de Premiação: Concurso de Redação ---")
    
    try:
        # Pergunta a quantidade total de notas
        qtd_notas = int(input("Quantas notas serão fornecidas? "))
        
        if qtd_notas <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        notas = []
        
        # Loop baseado na quantidade informada
        for i in range(qtd_notas):
            # O (i + 1) serve apenas para mostrar '1ª nota', '2ª nota', etc.
            nota = float(input(f"Digite a {i + 1}ª nota: "))
            notas.append(nota)

        # Ordenação
        notas.sort()

        print("\n" + "="*30)
        print(f"Total de participantes: {len(notas)}")
        print(f"Notas ordenadas: {notas}")
        print("="*30)

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")
