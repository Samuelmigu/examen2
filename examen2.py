# Mochila 0-1 (cada objeto como máximo una vez)
from typing import List, Tuple

def knapsack_01(items: List[Tuple[str, int, int]], W: int):
    """
    items: lista de (nombre, peso, valor)
    W: capacidad máxima
    Devuelve: (valor_max, peso_total, lista_items_elegidos)
    """
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, wt, val = items[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]  # no cogerlo
            if wt <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wt] + val)  # cogerlo

    # solución
    w = W
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, wt, val = items[i - 1]
            chosen.append((name, wt, val))
            w -= wt

    chosen.reverse()
    valor_max = dp[n][W]
    peso_total = sum(wt for _, wt, _ in chosen)
    return valor_max, peso_total, chosen

def main():
    items = [
        ("Libro de geometría diferencial (tapa dura)", 5, 11),
        ("Portátil con MATLAB (batería al 12%)", 6, 12),
        ("Tablet con apuntes offline", 4, 9),
        ("Póster enrollado del teorema de Stokes", 2, 5),
        ("Patito de goma 'debugger'", 1, 3),
        ("Memoria USB 'Ecuaciones diferenciales para vagos'", 1, 4),
        ("Calculadora programable 'casi un ordenador'", 3, 7),
        ("Taza térmica 'café = convergencia'", 1, 4),
    ]

    # d (último dígito)
    s = input("Último dígito d de tu DNI/NIE (si acaba en letra, usa el último dígito numérico): ").strip()
    if not s.isdigit():
        raise ValueError("d debe ser un dígito (0-9).")

    d = int(s)
    W = 14 + (d % 4)

    valor_max, peso_total, chosen = knapsack_01(items, W)

    print("\n================ RESULTADO ================")
    print(f"d = {d}")
    print(f"W = 14 + (d mod 4) = 14 + ({d} mod 4) = {W}")
    print(f"Valor máximo = {valor_max}")
    print(f"Peso total usado = {peso_total} / {W}")
    print("\nObjetos elegidos:")
    for name, wt, val in chosen:
        print(f" - {name} | peso {wt} | valor {val}")

    print("\nProblema clásico: Mochila 0-1 (0/1 Knapsack).")
    print("Una solución es un subconjunto de objetos (cada uno 0 o 1 vez) que no supera W.")
    print("Se maximiza la suma de valores.")

if __name__ == "__main__":
    main()
