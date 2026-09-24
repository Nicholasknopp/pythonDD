#O nome deste método tem significancia particular em Python: é o método construtor, um método opcional invocado quando a classe e instanciada, que é o nome dado á ação de criar objetos a partir da classe.

class Retangulo:
    lado_a = None
    lado_b = None

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        
    def calcula_Area(self):
        self.area = self.lado_a * self.lado_b

    def calcula_Perimetro(self):
        self.perimetro = 2 * self.lado_a + self.lado_b
