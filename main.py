
# constantes:
nome_arquivo_entrada = 'Test.cmp'
nome_arquivo_saida = 'Test1.cmp'

REMOVER = 0
NEUTRO = 1
FIM_DE_LINHA = 2

def remover_comentario_linha(txt: str):        
    achou_primeira_barra = False
    achou_segunda_barra = False
    achou_fim_linha = False
    mapeamento = []

    indice = 0

    for caractere in txt:
        match caractere:
            case r'/':
                if achou_primeira_barra == True:
                    achou_segunda_barra = True
                else:
                    achou_primeira_barra = True
                    

                
            case _:
                
                if achou_segunda_barra and achou_segunda_barra:
                    pass

                else:
                    achou_fim_linha = False
                    achou_primeira_barra = False
                    achou_segunda_barra = False

        
        indice += 1


        




def carregar_arquivo() -> str:
    with open(nome_arquivo_entrada) as arquivo:
        txt_arq = arquivo.read()
        
    return txt_arq
            

def salvar_arquivo(txt: str) -> None:
    with open(nome_arquivo_saida, 'w') as salvar:
            salvar.write(txt)



    
 
arquivo_txt = carregar_arquivo()
lista_arquivo = list(arquivo_txt)
print(''.join(lista_arquivo))

# remover comentários de linha
while arquivo_txt.find('//') != -1:
    inicio_comentario = arquivo_txt.find('//')
    fim_comentario = arquivo_txt.find('\n', inicio_comentario)

    lista_arquivo[inicio_comentario: fim_comentario] = []
    print(''.join(lista_arquivo))
    arquivo_txt = ''.join(lista_arquivo)
    print('===============================================================')






