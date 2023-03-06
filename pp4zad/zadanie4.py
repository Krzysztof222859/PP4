class Zajecia:

    def __init__(self):
        self.tablicaStudentow= []

    def zapiszStudenta(self, student):
        if len(self.tablicaStudentow)<=9:
            self.tablicaStudentow.append(student)
        else:
            print("Juz jest 10 studentow, ERROR")

z = Zajecia()

z.zapiszStudenta("jeden")
z.zapiszStudenta("dwa")
z.zapiszStudenta("trzy")
z.zapiszStudenta("cztery")
z.zapiszStudenta("piec")
z.zapiszStudenta("szesc")
z.zapiszStudenta("siedem")
z.zapiszStudenta("osiem")
z.zapiszStudenta("dziewiec")
z.zapiszStudenta("dziesiec")
z.zapiszStudenta("jedenascie")

print(z.tablicaStudentow)

