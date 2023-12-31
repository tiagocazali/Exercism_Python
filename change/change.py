def find_fewest_coins(coins, target):
    # Inicialize uma tabela para armazenar o número mínimo de moedas e as moedas escolhidas.
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Para dar troco de 0, não é necessário nenhuma moeda.
    coin_used = [-1] * (target + 1)  # Inicialize com -1 para indicar que nenhuma moeda foi usada.

    for i in range(1, target + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Agora, construa a lista das moedas usadas para dar troco.
    coins_used = []
    while target > 0:
        coin = coin_used[target]
        coins_used.append(coin)
        target -= coin

    return coins_used


x = find_fewest_coins([1, 4, 15, 20, 50], 23)
print(x)
