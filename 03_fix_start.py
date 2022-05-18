"""
03. fix_start                  RESOLVIDO

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""

"""                          familia

def fix_start(nome):            DEFINIÇÃO DA FUNÇÃO COM O PARÂMETRO NOME 
    
    print(nome[0])            AQUI EU PRINTO O PRIMEIRO CARACTER DA STRING

    print(nome.replace(nome[0],'*'))           AQUI EU PRINTO O RESULTADO DE REPLACE DE NOME MODIFICANDO OS CARACTERES QUE SÃO IGUAIS AO PRIMIRO POR '*'

    return nome[0] + nome[1:].replace(nome[0], '*')  AQUI EU RETORNO O PRIMEIRO CARACTER DE NOME MAIS O RESULTADO DE REPLACE DE NOME MODIFICANDO OS CARACTERES QUE SÃO IGUAIS AO PRIMIRO POR '*'
                                                     E RETORNO SOMENTE DO SEGUNDO CARACTER ATÉ O FINAL DA STRING

print(fix_start(nome = 'selissa'))                   CHAMO A FUNÇÃO COM O ARGUMENTO NOME

#nome.replace(nome[0], '*')  nome[1:].replace(nome[0], '*')

#####  Explicação que dei para o Douglas resolver

s = 'babble'
print(s)

#print(s[1:])
p = s

p = p.replace(p[0], '*')
print(p)

p = p[1:]
print(p)

s = s[0] + p
print(s)

#print(s[0] + s[1:].replace(s[0], '*'))

p = s
p = p.replace(p[0], '*')
p = p[1:]
s = s[0] + p
print(s)


"""


def fix_start(s):
    # +++ SUA SOLUÇÃO +++
    return s[0] + s[1:].replace(s[0], '*')          #AQUI EU RETORNO O PRIMEIRO CARACTER DE S MAIS O RESULTADO DE REPLACE DE S MODIFICANDO OS CARACTERES QUE SÃO IGUAIS AO PRIMIRO POR '*'
                                                    #E RETORNOR SOMENTE DO SEGUNDO CARACTER ATÉ O FINAL DA STRING


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
    test(fix_start, 'babble', 'ba**le')
    test(fix_start, 'aardvark', 'a*rdv*rk')
    test(fix_start, 'google', 'goo*le')
    test(fix_start, 'donut', 'donut')
