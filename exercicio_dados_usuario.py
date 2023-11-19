print ("Digite seu nome completo")   
nome_completo=input()
executar=True
while (executar == True):
     print ("Digite sua ano de nascimento")
     try:
          ano_de_nascimento = int(input())
          if (ano_de_nascimento <1922) or (ano_de_nascimento >2021):
            print ("O ano de nacimento  precisa ser entre 1922 a 2021")
          else:
            idade=2022-ano_de_nascimento
            print ("O usuário", nome_completo, "completou ou completara",  idade ,"anos de idade em 2022")
            executar = False
     except:
            print ("Os anos precisam ser escritos apenas com numero")