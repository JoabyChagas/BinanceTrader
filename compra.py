import binance
from binance.client import Client
from setup import API_Key, Secret_Key

client = Client(API_Key, Secret_Key)

# Definindo o ativo e a quantidade
symbol = 'BNBBRL'
quantity = 0.014  # Certifique-se de que essa quantidade é aceitável para a negociação na Binance

print(f"Iniciando a negociação para o ativo: {symbol}.")

try:
    # Criando a ordem de compra
    print("Preparando para comprar...")
    print(f"Ativo: {symbol}, Quantidade: {quantity}, Tipo: COMPRA")
    order = client.create_order(
        symbol=symbol,
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=quantity
    )
    print("Processando a negociação...")

    # Verificando o status da ordem
    print("Verificando o status da ordem...")
    order_status = client.get_order(
        symbol=symbol,
        orderId=order['orderId']
    )

    if order_status['status'] == 'FILLED':
        print("Negociação concluída com sucesso!")
        print(f"Informações da ordem: {order_status}")
    else:
        print("A negociação ainda está sendo processada. Status atual: ", order_status['status'])

except binance.exceptions.BinanceAPIException as e:
    print(f"Erro na negociação: {e.status_code} - {e.message}")
