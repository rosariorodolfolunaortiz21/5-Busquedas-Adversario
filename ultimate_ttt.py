import juegos_simplificado as js
import minimax

# =========================================================
# JUEGO
# =========================================================

class UltimateTTT(js.JuegoZT2):

    def inicializa(self):
        return (tuple([0]*81), None)

    # -------------------------
    #  FIX PRINCIPAL AQUÍ
    # -------------------------
    def jugadas_legales(self, estado, j):
        tablero, activo = estado

        #  Si no hay tablero activo → libre
        if activo is None:
            return [i for i in range(81) if tablero[i] == 0]

        #  Obtener sub-tablero
        inicio = activo * 9
        sub = tablero[inicio:inicio+9]

        #  Si está lleno o ganado → libre
        if self.tablero_terminado(sub):
            return [i for i in range(81) if tablero[i] == 0]

        #  Si no → solo ese tablero
        return [inicio + i for i in range(9) if sub[i] == 0]
