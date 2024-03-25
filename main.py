
# constantes:
nome_arquivo_entrada = 'Test.cmp'
nome_arquivo_saida = 'Test1.cmp'


""" def remover_comentario_linha(txt: str):        
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

 """
        

def remover_comentario_linha(txt: str) -> str:
    lista_arquivo = list(txt)
    while txt.find('//') != -1:
        inicio_comentario = txt.find('//')
        fim_comentario = txt.find('\n', inicio_comentario)

        lista_arquivo[inicio_comentario: fim_comentario] = []
        txt = ''.join(lista_arquivo)
        
    return txt

def remover_comentario_multilinhas(txt: str) -> str:
    lista_txt = list(txt)

    while txt.find('/*') != -1:
        inicio = txt.find('/*')
        fim = txt.find("*\\", inicio)

        if fim == -1:
            lista_txt[inicio :] = []
        else:
            lista_txt[inicio : fim + 2] = []

        txt = ''.join(lista_txt)

    return txt


def carregar_arquivo() -> str:
    with open(nome_arquivo_entrada) as arquivo:
        txt_arq = arquivo.read()
        
    return txt_arq
            

def salvar_arquivo(txt: str) -> None:
    with open(nome_arquivo_saida, 'w') as salvar:
            salvar.write(txt)



    
 
arquivo_txt = carregar_arquivo()
texto = remover_comentario_linha(arquivo_txt)
texto_sem_comentarios = remover_comentario_multilinhas(texto)
print(texto_sem_comentarios)
#salvar_arquivo(texto_sem_comentarios)


# remover comentários de bloco




