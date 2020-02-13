
def foreign_exchange_calculator(amount):
    sol_to_dollar=0.30

    return sol_to_dollar*amount


def run():
    print('**--CALCULADORA DE SOLES A DOLARES--**')

    amount=float(input('Ingrese la cantidad de soles a convertir: '))
    result=foreign_exchange_calculator(amount)
    print('S/{} soles a dólares americanos es: ${}'.format(amount,result))


if __name__ == "__main__":
    run()