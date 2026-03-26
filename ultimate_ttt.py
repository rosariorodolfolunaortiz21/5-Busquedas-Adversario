import juegos_simplificado as js
import minimax

# =========================================================
# JUEGO
# =========================================================

class UltimateTTT(js.JuegoZT2):

    def inicializa(self):
        return (tuple([0]*81), None)

    def jugadas_legales(self, estado, j):
        tablero, activo = estado

        #  MODO LIBRE (pero filtrando tableros terminados)
        if activo is None:
            jugadas = []

            for t in range(9):
                inicio = t * 9
                sub = tablero[inicio:inicio+9]

                if self.tablero_terminado(sub):
                    continue

                for i in range(9):
                    if sub[i] == 0:
                        jugadas.append(inicio + i)

            return jugadas

        #  NORMAL
        inicio = activo * 9
        sub = tablero[inicio:inicio+9]

        #  Si ese subtablero ya terminó → modo libre
        if self.tablero_terminado(sub):
            return self.jugadas_legales((tablero, None), j)

        return [inicio + i for i in range(9) if sub[i] == 0]

    def sucesor(self, estado, a, j):
        tablero, activo = estado
        tablero = list(tablero)

        tablero[a] = j

        siguiente = a % 9
        sub = tablero[siguiente*9:(siguiente+1)*9]

        if self.tablero_terminado(sub):
            siguiente = None

        return (tuple(tablero), siguiente)

    def tablero_terminado(self, sub):
        return self.gana_sub(sub) != 0 or 0 not in sub

    def gana_sub(self, s):
        if s[0] == s[4] == s[8] != 0:
            return s[0]
        if s[2] == s[4] == s[6] != 0:
            return s[2]
        for i in range(3):
            if s[3*i] == s[3*i+1] == s[3*i+2] != 0:
                return s[3*i]
            if s[i] == s[i+3] == s[i+6] != 0:
                return s[i]
        return 0

    def ganancia(self, estado):
        tablero, _ = estado

        grande = []
        for i in range(9):
            sub = tablero[i*9:(i+1)*9]
            grande.append(self.gana_sub(sub))

        return self.gana_sub(grande)

    def terminal(self, estado):
        tablero, _ = estado
        return self.ganancia(estado) != 0 or 0 not in tablero

