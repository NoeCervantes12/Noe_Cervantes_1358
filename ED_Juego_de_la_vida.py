"""
Reglas del juego de la vida:

1. Si una celula que se encuentra viva tiene cero o un vecino muere por soledad para la siguiente
generacion. Donde los vecinos son las 8 celulas que lo rodean inmediatamente.

2. Una celula viva que tiene dos o tres vecinos sobrevive para la siguiente generación.

3. Una celula viva que tiene 4 o mas vecinos muere por sobrepoblacion para la siguiente generacion.

4. Una celula muerta con exactamente 3 vecinos vivos resulta en un nacimiento cuya vida empieza en la
siguiente generacion. Todas las demas celulas muertas permanecen muertas para la siguiente eneracion.

"""

from Array2D import Array2D
class JuegoDeLaVida:
    def __init__(self, rows, cols, generaciones, poblacion_inicial):
        self.__cuadro=Array2D(rows, cols)
        self.__filas=rows
        self.__columnas=cols
        self.__generaciones=generaciones
    """"
    poblacion_inicial = [[1,3],[2,2],[2,3],[2,4]]
    """
        self.__cuadro.clearing(0)
            for cell in poblacion_inicial:
                self.__cuadro.set_item(cell[0], cell[1], 1)

      def to_string(cell):
          self.__cuadro.to_string()

    def configure_next_generation(self , nueva_generacion):
        self.__cuadro.clearing( 0 )
          for cell in nueva_generacion:
                self.__cuadro.set_item(cell[0], cell[1], 1)

    def set_cell_death(self,row,col)
        self.__cuadro.set_item(row, col,0)

    def set_cell_alive(self, row, col):
        self.__cuadro.set_item(row, col, 1)

    def ls_alive_cell(self, row, col):
        return self.__cuadro.get_item(row, col)==1

    def get_num_live_neighbors(row, col):
        


# Pruebas
def main():
    inicial = [[1,3],[2,2],[2,3],[2,4]]
    juego = -juegoDeLaVida(5,5,4,inicial)
    juego.to_string()
    
 """   
get_num_rows()
get_num_cols()
configure_next_gen(nueva_poblacion)
set_cell_death(row, col)
set_cell_alive(row, col)
is_live_cell(row, col)
get_num_live_neighbors(row, col)

"""
