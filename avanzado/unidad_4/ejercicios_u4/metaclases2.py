class Material: pass

class Auto(Material):
    color="Azul"

    def retornar_color(self,):
        return self.color

objeto=Auto()
print(objeto.retornar_color())
print(type(Auto.__class__))

print("---"*23)
 
Auto2=type("Auto2", (Material,), {"color": "Azul", "retornar_color": (lambda x: x.color)})
objeto2=Auto2()
print(objeto2.retornar_color())
print(type(Auto2.__class__))