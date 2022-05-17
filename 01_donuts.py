"""
01. donuts    RESOLVIDO

Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""

"""
def donuts():
    
    primeiro modo que eu fiz
    count = 1

    while count < 20:
        if count < 10:
            print("'" + "Number of donuts: %s' " % (count) )
            count += 1
        else:
            print("'Number of donuts:" + "many'")
            count += 1
            # +++ SUA SOLUÇÃO +++


    for count in range(1, 20): # Segundo modo que eu fiz
        if count < 10:
            print("'" + "Number of donuts: %s' " % (count))
            count += 1
        else:
            print("'Number of donuts:" + "many'")
            count += 1
            # +++ SUA SOLUÇÃO +++


     
donuts()
"""

def donuts(count):
    # LEITURA DA LINHA
    # RETORNE Number of donuts: mais Many SE count for maior que 9
    #                                     SE NÃO o número do count
       return f"Number of donuts: {'many' if count > 9 else count}"


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(donuts, 4, 'Number of donuts: 4')
    test(donuts, 9, 'Number of donuts: 9')
    test(donuts, 10, 'Number of donuts: many')
    test(donuts, 99, 'Number of donuts: many')
Pablo Full Stack 'DESEJA UM DIA ABENÇÕADO EM NOME DE JESUSPablo Full Stack 'DESEJA UM DIA ABENÇÕADO EM NOME DE JESUS