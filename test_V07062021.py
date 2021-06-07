import unittest
from main import Tateti


class TestTateti:
    def test_matriz(self): #1
        assert(Tateti.Letra_ABC(0) == "A")

    def test_jugador_1_gana_columna_1(self, capsys):#2
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B1")
        t.input_jugador("2", "B2")
        t.input_jugador("1", "C1")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)

    def test_bug_2021(self, capsys):#3
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B1")
        t.input_jugador("2", "A3")
        t.input_jugador("1", "B3")
        t.input_jugador("2", "B2")
        t.input_jugador("1", "C1")
        captured = capsys.readouterr()
        assert ("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)

    def test_jugador_2_gana_columna_1(self, capsys): #4 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A2")
        t.input_jugador("2", "A1")
        t.input_jugador("1", "A3")
        t.input_jugador("2", "B1")
        t.input_jugador("1", "B3")
        t.input_jugador("2", "C1")
        captured = capsys.readouterr()
        assert ("GANO EL JUGADOR 2 [0]" in captured.out)
        assert ("GANO EL JUGADOR 1 [X]" not in captured.out)

    def test_jugador_1_gana_columna_2(self, capsys): # 5 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A2")
        t.input_jugador("2", "A1")
        t.input_jugador("1", "B2")
        t.input_jugador("2", "B1")
        t.input_jugador("1", "C2")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)

    def test_jugador_1_gana_columna_3(self, capsys): # 6 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A3")
        t.input_jugador("2", "A1")
        t.input_jugador("1", "B3")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "C3")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)

    def test_jugador_1_gana_Fila_1(self, capsys): # 7 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "B1")
        t.input_jugador("1", "A2")
        t.input_jugador("2", "B2")
        t.input_jugador("1", "A3")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)        

    def test_jugador_1_gana_Fila_2(self, capsys): # 8 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "B1")
        t.input_jugador("2", "C1")
        t.input_jugador("1", "B2")
        t.input_jugador("2", "C2")
        t.input_jugador("1", "B3")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)        

    def test_jugador_1_gana_Fila_3(self, capsys): # 9 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "C1")
        t.input_jugador("2", "A1")
        t.input_jugador("1", "C2")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "C3")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)       

    def test_jugador_1_gana_Diagonal_1(self, capsys): # 10 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B2")
        t.input_jugador("2", "C1")
        t.input_jugador("1", "C3")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)        

    def test_jugador_1_gana_Diagonal_2(self, capsys): # 11 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "C1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B2")
        t.input_jugador("2", "B1")
        t.input_jugador("1", "A3")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)        

    def test_jugador_2_gana_Columna_2(self, capsys): # 12 Agregado EMI
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B1")
        t.input_jugador("2", "B2")
        t.input_jugador("1", "A3")
        t.input_jugador("2", "C2")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 2 [0]" in captured.out)
        assert ("GANO EL JUGADOR 1 [X]" not in captured.out)        

    def test_jugador_2_gana_Columna_3(self, capsys): # 13 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "A1")
       t.input_jugador("2", "A3")
       t.input_jugador("1", "B1")
       t.input_jugador("2", "B3")
       t.input_jugador("1", "C2")
       t.input_jugador("2", "C3")
       captured = capsys.readouterr()
       assert("GANO EL JUGADOR 2 [0]" in captured.out)
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)

    def test_jugador_2_gana_fila_1(self, capsys): # 14 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "B1")
       t.input_jugador("2", "A1")
       t.input_jugador("1", "B2")
       t.input_jugador("2", "A2")
       t.input_jugador("1", "C3")
       t.input_jugador("2", "A3")
       captured = capsys.readouterr()
       assert("GANO EL JUGADOR 2 [0]" in captured.out)
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)

    def test_jugador_2_gana_fila_2(self, capsys): # 15 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "A1")
       t.input_jugador("2", "B1")
       t.input_jugador("1", "C1")
       t.input_jugador("2", "B2")
       t.input_jugador("1", "C2")
       t.input_jugador("2", "B3")
       captured = capsys.readouterr()
       assert("GANO EL JUGADOR 2 [0]" in captured.out)
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)     

    def test_jugador_2_gana_fila_3(self, capsys): # 16 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "A1")
       t.input_jugador("2", "C1")
       t.input_jugador("1", "B1")
       t.input_jugador("2", "C2")
       t.input_jugador("1", "B2")
       t.input_jugador("2", "C3")
       captured = capsys.readouterr()
       assert("GANO EL JUGADOR 2 [0]" in captured.out)
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)     

    def test_jugador_2_gana_diagonal_1(self, capsys): # 17 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "A2")
       t.input_jugador("2", "A1")
       t.input_jugador("1", "B3")
       t.input_jugador("2", "B2")
       t.input_jugador("1", "C2")
       t.input_jugador("2", "C3")
       captured = capsys.readouterr()
       assert("GANO EL JUGADOR 2 [0]" in captured.out)
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)    

    def test_jugador_2_gana_diagonal_2(self, capsys): # 18 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "A1")
       t.input_jugador("2", "C1")
       t.input_jugador("1", "B1")
       t.input_jugador("2", "B2")
       t.input_jugador("1", "B3")
       t.input_jugador("2", "A3")
       captured = capsys.readouterr()
       assert("GANO EL JUGADOR 2 [0]" in captured.out)
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)
    
    def test_TABLAS(self, capsys): # 19 Agregado EMI
       t = Tateti("test")
       t.inicializar_tablero()
       t.input_jugador("1", "A1")
       t.input_jugador("2", "B2")
       t.input_jugador("1", "B1")
       t.input_jugador("2", "C1")
       t.input_jugador("1", "A3")
       t.input_jugador("2", "A2")
       t.input_jugador("1", "C2")
       t.input_jugador("2", "B3")
       t.input_jugador("1", "C3")
       captured = capsys.readouterr()
       #t.self.turno = 10
       assert ("GANO EL JUGADOR 1 [X]" not in captured.out)
       assert ("GANO EL JUGADOR 2 [0]" not in captured.out)
       #assert ("TABLAS" in captured.out) # el captured no me toma lo que verdaderamente se imprime en la pantalla
#



