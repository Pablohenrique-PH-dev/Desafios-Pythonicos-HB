"""
04. mix_up               RESOLVIDO

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""
"""                                  MEUS TESTES FOI EM CIMA DESSE MODO ABAIXO
def mix_up(a, b):

    print(a + b)               # AQUI FIZ UMA CONCATENAÇÃO              PabloHenrique

    print(f'{a}{b}')           # AQUI FIZ UMA CONCATENÇÃO DE MANEIRA DIFERENTE         PabloHenrique

    print(f'{a} {b}')          # AQUI FIZ UMA CONCATENÇÃO DE MANEIRA DIFERENTE MAS DEIXANDO UM ESPAÇO ENTRE OS 2 ELEMENTOS            Pablo Henrique

    print(f'{a[:2]} {b[:2]}')  # AQUI FIZ UMA CONTATENAÇÃO CONFORME ACIMA UTILIZANDO APENAS OS DOIS PRIMEIROS CARACTER DE CADA STRING            Pa He

    print(f'{a[2:]} {b[2:]}')  # AQUI FIZ UMA CONTATENAÇÃO CONFORME ACIMA UTILIZANDO APENAS DO TERCEIRO CARACTER EM DIANTE DE CADA STRING           blo nrique

    return f'{b[:2]}{a[2:]} {a[:2]}{b[2:]}'   # AQUI FIZ UMA CONTATENAÇÃO CONFORME UTILIZANDO APENAS OS DOIS PRIMEIROS CARACTER DE CADA STRING MAIS O RESTANTE DA SEGUNDA STRING     Heblo Panrique


print(mix_up(a = 'Pablo', b = 'Henrique'))

"""

def mix_up(a, b):
    # +++ SUA SOLUÇÃO +++
    return f'{b[:2]}{a[2:]} {a[:2]}{b[2:]}'


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
