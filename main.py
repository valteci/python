
# constantes:
nome_arquivo_entrada = 'Test.cmp'
nome_arquivo_saida = 'Test1.cmp'

  

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
        fim = txt.find("*/", inicio)

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

def remover_quebras_de_linha(txt: str) -> str:
    achou_quebra_linha = False
    lista_txt = list(txt)
    novo_texto = []

    for caractere in lista_txt:
        if caractere == '\n':
            if achou_quebra_linha == True:
                pass
            else:
                achou_quebra_linha = True
                novo_texto.append(caractere)
        else:
            novo_texto.append(caractere)
            achou_quebra_linha = False


    while novo_texto[0] == '\n':
        novo_texto.remove('\n') # remove a primeira ocorrência de quebra de linha (\n)

    return ''.join(novo_texto)

def remover_espacos_em_branco(txt: str) -> str:
    achou_espaco_branco = False
    lista_txt = list(txt)

    novo_texto = []
    posicao = 0

    for caractere in lista_txt:
        if caractere == ' ' or caractere == '\t':
            if achou_espaco_branco == True:
                pass
            elif (posicao != 0) and (posicao + 1 < len(lista_txt)):
                if (lista_txt[posicao - 1] == '\n') or (lista_txt[posicao + 1] == '\n'):
                    pass            
            else:
                achou_espaco_branco = True
                novo_texto.append(' ')

        else:
            novo_texto.append(caractere)
            achou_espaco_branco = False

        posicao += 1

    while novo_texto[0] == ' ' or novo_texto[0] == '\t':
        if novo_texto[0] == ' ':
            novo_texto.remove(' ')

        elif novo_texto[0] == '\t':
            novo_texto.remove('\t')

    return ''.join(novo_texto)

 
arquivo_txt = carregar_arquivo()
texto = remover_comentario_linha(arquivo_txt)
texto_sem_comentarios = remover_comentario_multilinhas(texto)
texto_semifinal = remover_quebras_de_linha(texto_sem_comentarios)
texto_final = remover_espacos_em_branco(texto_semifinal)

salvar_arquivo(texto_final)
print(texto_final)

# remover quebras de linha




 