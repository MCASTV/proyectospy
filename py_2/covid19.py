from pyknow import *

class ContactoContagiado(Fact):
    """ Leyendo tus sintomas """

class FaltaDeAire(Fact):
    """ Leyendo tus sintomas """

class Estornudos(Fact):
    """ Leyendo tus sintomas """

class Fiebre(Fact):
    """ Leyendo tus sintomas """

class Tos(Fact):
    """ Leyendo tus sintomas """

class EscurrimientoNasal(Fact):
    """ Leyendo tus sintomas """

class CuerpoCortado(Fact):
    """ Leyendo tus sintomas """

class DolorGarganta(Fact):
    """ Leyendo tus sintomas """

class Diarrea(Fact):
    """ Leyendo tus sintomas """

class NoFuncionaTratamiento(Fact):
    """ Leyendo tus sintomas """

class SintomasPersistentes(Fact):
    """ Leyendo tus sintomas """

class COVID(KnowledgeEngine):
    contador=0
    contador2=0
    @Rule(ContactoContagiado(contactoContagiado = 'a'))
    def sintomaCovid(self):
        self.contador=self.contador + 1
        self.declare(FaltaDeAire(faltaDeAire = input("¿Tienes sensación de falta de aire? (que no sea causada por alguna enfermedad crónica o previamente diagnosticada) \na) Si \nb) No \n ")))
        print()

    @Rule(ContactoContagiado(contactoContagiado = 'b'))
    def sintomaGripa(self):
        self.contador2=self.contador2 + 1
        self.declare(FaltaDeAire(faltaDeAire = input("¿Tienes sensación de falta de aire? (que no sea causada por alguna enfermedad crónica o previamente diagnosticada) \na) Si \nb) No \n ")))
        print()

    @Rule(ContactoContagiado(contactoContagiado = 'c'))
    def sintomaConfuso(self):
        self.contador2=self.contador2 + 1
        self.declare(FaltaDeAire(faltaDeAire = input("¿Tienes sensación de falta de aire? (que no sea causada por alguna enfermedad crónica o previamente diagnosticada) \na) Si \nb) No \n ")))
        print()

    @Rule(FaltaDeAire(faltaDeAire = 'a'))
    def sintomaCovid2(self):
        self.contador=self.contador + 1
        self.declare(Estornudos(estornudos = input("¿Tienes Estornudos? \na) No \nb) Si \n ")))
        print()

    @Rule(FaltaDeAire(faltaDeAire = 'b'))
    def sintomaGripa2(self):
        self.contador2=self.contador2 + 1
        self.declare(Estornudos(estornudos = input("¿Tienes Estornudos? \na) No \nb) Si \n ")))
        print()

    @Rule(Estornudos(estornudos = 'a'))
    def sintomaCovid3(self):
        self.contador=self.contador + 1
        self.declare(Fiebre(fiebre = input("¿Tienes fiebre mayor a 38°C? \na) Si \nb) No \n ")))
        print()

    @Rule(Estornudos(estornudos = 'b'))
    def sintomaGripa3(self):
        self.contador2=self.contador2 + 1
        self.declare(Fiebre(fiebre = input("¿Tienes fiebre mayor a 38°C? \na) Si \nb) No \n ")))
        print()

    @Rule(Fiebre(fiebre = 'a'))
    def sintomaCovid4(self):
        self.contador=self.contador + 1
        self.declare(Tos(tos = input("¿Tienes tos seca? \na) Siempre \nb) Algunas veces \n ")))
        print()

    @Rule(Fiebre(fiebre = 'b'))
    def sintomaGripa4(self):
        self.contador2=self.contador2 + 1
        self.declare(Tos(tos = input("¿Tienes tos seca? \na) Siempre \nb) Algunas veces \n ")))
        print()

    @Rule(Tos(tos = 'a'))
    def sintomaCovid5(self):
        self.contador=self.contador + 1
        self.declare(EscurrimientoNasal(escurrimientoNasal = input("¿Tienes escurrimiento nasal? \na) Rara vez \nb) Casi siempre \n ")))
        print()

    @Rule(Tos(tos = 'b'))
    def sintomaGripa5(self):
        self.contador2=self.contador2 + 1
        self.declare(EscurrimientoNasal(escurrimientoNasal = input("¿Tienes escurrimiento nasal? \na) Rara vez \nb) Casi siempre \n ")))
        print()

    @Rule(EscurrimientoNasal(escurrimientoNasal = 'a'))
    def sintomaCovid6(self):
        self.contador=self.contador + 1
        self.declare(CuerpoCortado(cuerpoCortado= input("¿Tienes cuerpo cortado o dolor muscular? \na) Algunas veces \nb) Siempre \n ")))
        print()

    @Rule(EscurrimientoNasal(escurrimientoNasal = 'b'))
    def sintomaGripa6(self):
        self.contador2=self.contador2 + 1
        self.declare(CuerpoCortado(cuerpoCortado= input("¿Tienes cuerpo cortado o dolor muscular? \na) Algunas veces \nb) Siempre \n ")))
        print()

    @Rule(CuerpoCortado(cuerpoCortado = 'a'))
    def sintomaCovid7(self):
        self.contador=self.contador + 1
        self.declare(DolorGarganta(dolorGarganta= input("¿Tienes dolor de garganta? \na) Algunas veces \nb) Siempre \n ")))
        print()

    @Rule(CuerpoCortado(cuerpoCortado = 'b'))
    def sintomaGripa7(self):
        self.contador2=self.contador2 + 1
        self.declare(DolorGarganta(dolorGarganta= input("¿Tienes dolor de garganta? \na) Algunas veces \nb) Siempre \n ")))
        print()

    @Rule(DolorGarganta(dolorGarganta = 'a'))
    def sintomaCovid8(self):
        self.contador=self.contador + 1
        self.declare(Diarrea(diarrea= input("¿Tienes diarrea o malestar estomacal? \na) Si \nb) No \n ")))
        print()

    @Rule(DolorGarganta(dolorGarganta = 'b'))
    def sintomaGripa8(self):
        self.contador2=self.contador2 + 1
        self.declare(Diarrea(diarrea= input("¿Tienes diarrea o malestar estomacal? \na) Si \nb) No \n ")))
        print()

    @Rule(Diarrea(diarrea = 'a'))
    def sintomaCovid9(self):
        self.contador=self.contador + 1
        self.declare(NoFuncionaTratamiento(noFuncionaTratamiento= input("¿Has recibido tratamiento médico para tus síntomas? \na) Sí, pero no funciona \nb) Sí, esta funcionando \nc) No \n ")))
        print()

    @Rule(Diarrea(diarrea = 'b'))
    def sintomaGripa9(self):
        self.contador2=self.contador2 + 1
        self.declare(NoFuncionaTratamiento(noFuncionaTratamiento= input("¿Has recibido tratamiento médico para tus síntomas? \na) Sí, pero no funciona \nb) Sí, esta funcionando \nc) No \n ")))
        print()

    @Rule(NoFuncionaTratamiento(noFuncionaTratamiento = 'a'))
    def sintomaCovid10(self):
        self.contador=self.contador + 1
        self.declare(SintomasPersistentes(sintomasPersistentes= input("¿Has salido los últimos días de casa? \na) Si \nb) No \n ")))
        print()

    @Rule(NoFuncionaTratamiento(noFuncionaTratamiento = 'b'))
    def sintomaGripa10(self):
        self.contador2=self.contador2 + 1
        self.declare(SintomasPersistentes(sintomasPersistentes= input("¿Has salido los últimos días de casa? \na) Si \nb) No \n ")))
        print()

    @Rule(NoFuncionaTratamiento(noFuncionaTratamiento = 'c'))
    def sintomaConfuso10(self):
        self.contador=self.contador + 1
        self.declare(SintomasPersistentes(sintomasPersistentes= input("¿Has salido los últimos días de casa? \na) Si \nb) No \n ")))
        print()

    @Rule(SintomasPersistentes(sintomasPersistentes = 'a'))
    def sintomaCovid11(self):
        self.contador=self.contador + 1
        if(self.contador > self.contador2):
           print()
           print("--> Tus síntomas coinciden con los de COVID-19, acude al hospital y asegúrate de ingresar por el área de Urgencias.")
           print("--> Mantén la calma, más del 80 porciento de los casos detectados por el COVID-19 no requieren hospitalización y se recuperan en casa.")
           print("--> Durante tu traslado y llegada al hospital: EVITA EL SALUDO DE BESO O MANO.")
           print()
        else:
           print()
           print("--> Presentas algunos síntomas de enfermedad respiratoria, pero es poco probable que se trate de COVID-19.")
           print("--> En esta temporada es común presentar un resfriado o alergias.")
           print("--> Descansar en casa, beber muchos líquidos e incluir vitaminas y minerales en tu alimentación puede ayudarte a sentirte mejor.")
           print("--> Recuerda no automedicarte y seguir las medidas de prevención.")
           print()

    @Rule(SintomasPersistentes(sintomasPersistentes = 'b'))
    def sintomaGripa11(self):
        self.contador2=self.contador2 + 1
        if(self.contador > self.contador2):
           print()
           print("--> Tus síntomas coinciden con los de COVID-19, acude al hospital y asegúrate de ingresar por el área de Urgencias.")
           print("--> Mantén la calma, más del 80 porciento de los casos detectados por el COVID-19 no requiern hospitalización y se recuperan en casa.")
           print("--> Durante tu traslado y llegada al hospita: EVITA EL SALUDO DE BESO O MANO.")
           print()
        else:
           print()
           print("--> Presentas algunos síntomas de enfermedad respiratoria, pero es poco probable que se trate de COVID-19.")
           print("--> En esta temporada es común presentar un resfriado o alergias.")
           print("--> Descansar en casa, beber muchos líquidos e incluir vitaminas y minerales en tu alimentación puede ayudarte a sentirte mejor.")
           print("--> Recuerda no automedicarte y seguir las medidas de prevención.")
           print()
engine = COVID()
engine.reset()
print()
print("                             ---- TEST COVID19 ----")
p1 = input("¿Has tenido contacto directo con algún paciente positivo confirmado con COVID-19? \na) Si \nb) No \nc) No sé \n " )

print()

engine.declare((ContactoContagiado(contactoContagiado = p1)))
engine.run()
