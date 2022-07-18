def escrever(nome, txt):
    arquivo = open(nome + '.txt' , 'w')
    arquivo.write(f"{txt}\n")
    arquivo.close()

def atualizar_arq(nome, texto):
    arquivo = open(nome + '.txt', 'a')
    arquivo.write(f"{texto}\n")
    arquivo.close()


print("O que deseja fazer?\n A- Escrever um novo arquivo\n B- Adicionar dados a um arquivo existente\n C- Apagar todos os dados")
opcao = input()
if opcao.upper() == "A":
    nome_arq = input("Digite o nome do arquivo:")
    txt = input("O que deseja escrever?\nCaso não queira escrever nada aperte ENTER!")
    escrever(nome_arq, txt)

elif opcao.upper() == "B":
    nome_arq = input("Digite o nome do arquivo que deseja atualizar:")
    txt = input("O que deseja escrever?\nCaso não queira escrever nada aperte ENTER!")
    atualizar_arq(nome_arq, txt)

elif opcao.upper() == "C":
    nome_arq = input("Digite o nome do arquivo que deseja apagar:")
    txt = ' '
    escrever(nome_arq, txt)