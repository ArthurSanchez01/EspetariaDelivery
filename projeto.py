print("""


\033[32m=======ESPETARIA DELIVERY=======\033[m
""")
print("="*20)
delivery = []
item = {
       "nome": "nome",
       "descricao": "desc",
       "valor": "valor"
       }
opcao = 0


while opcao != 5:


    print("""
        [1] Cadastrar Pedido
        [2] Listar Pedidos
        [3] Deleter Pedido
        [4] Confirmar pedido 
        [5] Sair
        """)


    opcao = int(input("Digite uma opção: "))


    print("="*20)


    if opcao == 1:
        try:


            cafta = "cafta"
            Pedaco = "carne de vaca"
            Medalhao = "nome:Frango, descrição: galinha, Valor:10"
            Mussarela = "nome:queijo, descrição: queijo, Valor:12"
            cardapio = [{ "nome":"cafta",
                      "descrição":"carne moida",
                      "valor": 10},
                    { "nome": "pedaço",
                       "descrição": "carne de vaca",
                       "valor": 12.},
                    {"nome": "medalhão",
                          "descrição":"frango bacon",
                          "valor": 10},
                    {"nome": "mussarela",
                        "descrição": "queijo",
                        "valor": 12}]
       
            for x,i in enumerate(cardapio):
                print(cardapio[x]["nome"])
                print(f"Espeto: {cardapio[x]["nome"]} Valor: {cardapio[x]["valor"]}, Descrição: {cardapio[x]["descrição"]}")
           
       
            print("="*20)


            print("""
            [1] Cafta
            [2] Pedaço(Carne)
            [3] Medalão de frango
            [4] Mussarela
            [5] sair     
            """)
       
         


            Espeto = int(input("Escolha seu espeto: "))
       


            if Espeto ==1:
                   
                        item = {
                            "nome": cardapio[0]["nome"],
                            "descricao": cardapio[0]["descrição"],
                            "valor": cardapio[0]["valor"]
                        }
                        print(f"""
                            __________ESPETARIA DELIVERY__________
                           
                            Resumo de Pedido
                            \*/*\*/\*/*\*/\*/*\*/
                            Você escolheu:
                            {item["nome"]}
                            {item['descricao']}
                            {item['valor']}
                            """)


            elif Espeto ==2:  
                        item = {
                            "nome": cardapio[1]["nome"],
                            "descricao": cardapio[1]["descrição"],
                            "valor": cardapio[1]["valor"]
                        }
                        print(f"""
                            __________ESPETARIA DELIVERY__________
                           
                            Resumo de Pedido
                            \*/*\*/\*/*\*/\*/*\*/
                            Você escolheu:
                            {item["nome"]}
                            {item['descricao']}
                            {item['valor']}
                            """)
            elif Espeto ==3:
                        item = {
                            "nome": cardapio[2]["nome"],
                            "descricao": cardapio[2]["descrição"],
                            "valor": cardapio[2]["valor"]
                        }  
                        print(f"""
                            __________ESPETARIA DELIVERY__________
                           
                            Resumo de Pedido
                            \*/*\*/\*/*\*/\*/*\*/
                            Você escolheu:
                            {item["nome"]}
                            {item['descricao']}
                            {item['valor']}
                            """)


            elif Espeto ==4:
                        item = {
                            "nome": cardapio[3]["nome"],
                            "descricao": cardapio[3]["descrição"],
                            "valor": cardapio[3]["valor"]
                        }
                        print(f"""
                            __________ESPETARIA DELIVERY__________
                           
                            Resumo de Pedido
                            \*/*\*/\*/*\*/\*/*\*/
                            Você escolheu:
                            {item["nome"]}
                            {item['descricao']}
                            {item['valor']}
                            """)
            elif Espeto == 5:
                  print("\033[36m==========Você Saiu Da Escolha Dos Espetos==========\033[m")            
            else:      
                print("\033[31m======ESPETO INVALIDO======\033[m")

            delivery.append(item)
            print("="*20)
        except ValueError as erro:

            print("\033[31m======ESPETO INVALIDO======\033[m")


    elif opcao == 2:
        if len(delivery) >0:
            total = 0
        
            
            
            for x,i in enumerate(delivery):
                print(delivery[x]["nome"])
                print(f"Espeto: {delivery[x]["nome"]} Valor: {delivery[x]["valor"]}")


                total = total + delivery[x]["valor"]
                print("="*20)
            print(f"O total do seu pedido foi de: R${total}")
            print("="*20)
        else:
            print("\033[31m======NÃO TEM PEDIDOS NA SUA LISTA======\033[m")


    elif opcao ==3:
            for x,i in enumerate(delivery):
                print(f"[{x}] Espeto: {delivery[x]["nome"]} Valor: {delivery[x]["valor"]}")


            try:


                deletar = int(input("Escolha o número do seu espeto a ser deletado: "))
            except ValueError as erro:
             print("\033[31m======OPÇÃO INVALIDO======\033[m")


           
            print(f"O produto escolhido foi:Posicao[{[deletar]}] Nome: {delivery[deletar]["nome"] } ")
           
            delivery.pop(deletar)
            print("="*20)
              
            for x,i in enumerate(delivery):
                print(delivery[x]["nome"])
                print(f"Espeto: {delivery[x]["nome"]} Valor: {delivery[x]["valor"]}")
            
            print("="*20)
    elif opcao ==4:
          print("\033[32m=======SEU PEDIDO FOI CONFIRMADO!=======\033[m")        
    elif opcao ==5:
        print("\033[36m==========Você Saiu==========\033[m")
       
    else:
        print("\033[31m==========OPÇÃO INVALIDA==========\033[m")


           


    print("="*20)