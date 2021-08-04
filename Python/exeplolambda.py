#calculadora com lambda!

calculadora = {
    'soma': lambda a, b: a+b,
    'subtração': lambda a, b: a-b,
    'multiplicação': lambda a, b: a*b,
    'divisão': lambda a, b: a/b
}

q = input('qual opção deseja da calculadora: {} '.format(calculadora.keys()))

if q in calculadora.keys():
    print(q)
    a = int(input('digite um numero:\n'))
    b = int(input('digite um numero:\n'))
    
