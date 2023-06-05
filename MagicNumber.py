import random


def generar_tablero(n):
    # Genera un tablero de tamaño n x n con valores aleatorios del 1 al 9
    # La casilla en la posición (0, 0) siempre tiene un valor de 0
    tablero = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
    tablero[0][0] = 0
    return tablero


def imprimir_tablero(tablero, visitados, valor_acumulado):
    # Imprime el tablero con las casillas visitadas marcadas con una X
    # y muestra el valor acumulado del camino actual
    n = len(tablero)
    for i in range(n):
        for j in range(n):
            if visitados[i][j]:
                print(" X ", end="")
            else:
                print(f" {tablero[i][j]} ", end="")
            print("|", end="")
        print()
        print("-" * (4 * n - 1))
    print("Valor acumulado:", valor_acumulado)


def dentro_del_tablero(x, y, n):
    # Verifica si las coordenadas (x, y) están dentro del tablero de tamaño n x n
    return 0 <= x < n and 0 <= y < n


def dfs(tablero, objetivo, x, y, visitados, valor_acumulado):
    # Realiza una búsqueda en profundidad (DFS) para encontrar un camino que sume el objetivo
    n = len(tablero)

    if tablero[x][y] + valor_acumulado == objetivo:
        # Si se alcanza el objetivo, se ha encontrado un camino válido
        return True

    visitados[x][y] = True

    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if (
            dentro_del_tablero(nx, ny, n)
            and not visitados[nx][ny]
            and tablero[nx][ny] + valor_acumulado <= objetivo
        ):
            visitados[nx][ny] = True
            if dfs(tablero, objetivo, nx, ny, visitados, valor_acumulado + tablero[nx][ny]):
                return True
            visitados[nx][ny] = False

    return False


def jugar_numero_magico(n, objetivo):
    # Configuración inicial del juego
    tablero = generar_tablero(n)
    visitados = [[False for _ in range(n)] for _ in range(n)]
    visitados[0][0] = True  # La casilla (0, 0) siempre comienza visitada
    x, y = 0, 0
    valor_acumulado = 0
    camino = [(x, y)]

    # Si no hay un camino válido con el tablero generado, se vuelve a generar un nuevo tablero
    while not dfs(tablero, objetivo, x, y, visitados, valor_acumulado):
        tablero = generar_tablero(n)
        visitados = [[False for _ in range(n)] for _ in range(n)]
        visitados[0][0] = True
        x, y = 0, 0
        valor_acumulado = 0
        camino = [(x, y)]

    # Juego
    visitados = [[False for _ in range(n)] for _ in range(n)]
    visitados[0][0] = True
    x, y = 0, 0
    valor_acumulado = 0
    camino = [(x, y)]

    print("\n¡Bienvenido al juego 'Número Mágico'!")
    print("El objetivo es encontrar un camino que sume", objetivo, "puntos")
    print("Utiliza las teclas 'W', 'A', 'S', 'D' para moverte por el tablero.")
    print("Cada movimiento suma el valor de la casilla a tu valor acumulado.")
    print("Usted comienza en la casilla (0, 0) con un valor acumulado de 0.")
    print("Presiona 'Q' para salir del juego.")
    print("Presiona 'E' para resolver el juego automáticamente utilizando DFS.")

    while True:
        imprimir_tablero(tablero, visitados, valor_acumulado)

        if valor_acumulado == objetivo:
            print("¡Felicidades! Has encontrado el camino que suma", objetivo)
            break
        elif valor_acumulado > objetivo:
            print("Te has pasado del número objetivo. El juego termina.")
            break

        movimiento = input("Ingresa tu movimiento (W/A/S/D): ").upper()

        if movimiento == "W":
            nx, ny = x - 1, y
        elif movimiento == "A":
            nx, ny = x, y - 1
        elif movimiento == "S":
            nx, ny = x + 1, y
        elif movimiento == "D":
            nx, ny = x, y + 1
        elif movimiento == "E":
            print("Resolviendo el juego automáticamente...")
            visitados = [[False for _ in range(n)] for _ in range(n)]
            visitados[0][0] = True
            x, y = 0, 0
            valor_acumulado = 0
            camino = [(x, y)]
            dfs(tablero, objetivo, x, y, visitados, valor_acumulado)
            imprimir_tablero(tablero, visitados, objetivo)
            break
        elif movimiento == "Q":
            print("Has salido del juego.")
            break
        else:
            print("Movimiento inválido. Intenta nuevamente.")
            continue

        if dentro_del_tablero(nx, ny, n):
            if not visitados[nx][ny]:
                x, y = nx, ny
                valor_acumulado += tablero[x][y]
                camino.append((x, y))
                visitados = [[False for _ in range(n)] for _ in range(n)]  # Reiniciar listado de visitados
                for cx, cy in camino:
                    visitados[cx][cy] = True
            else:
                print("Ya has visitado esa casilla. Intenta nuevamente.")
        else:
            print("Movimiento fuera del tablero. Intenta nuevamente.")


# easy: jugar_numero_magico(4, 20)
# mid: jugar_numero_magico(6, 30)
# hard: jugar_numero_magico(8, 40)
# extreme: jugar_numero_magico(10, 50)


def dificultad():
    # Pregunta al usuario el nivel de dificultad y ejecuta el juego correspondiente
    while True:
        print("¿Qué nivel de dificultad deseas?")
        print("1. Fácil")
        print("2. Medio")
        print("3. Difícil")
        print("4. Extremo")
        print("5. Salir")
        opcion = input("Ingresa tu opción: ")
        if opcion == "1":
            jugar_numero_magico(4, 20)
        elif opcion == "2":
            jugar_numero_magico(6, 60)
        elif opcion == "3":
            jugar_numero_magico(8, 120)
        elif opcion == "4":
            jugar_numero_magico(10, 180)
        elif opcion == "5":
            print("Has salido del juego.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")
        print()


dificultad()
