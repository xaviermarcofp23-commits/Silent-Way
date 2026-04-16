from datetime import datetime
class Programador:
    def init(self, n): self.nombre = n
class Proyecto:
    def init(self, n, fi, ffp, ps=None):
        self.nombre, self.fecha_inicio, self.fecha_fin_prevista = n, fi, ffp
        self.fecha_creacion = datetime.now()
        self.programadores = ps or []
    def str(self):
        return f"{self.nombre} | {self.fecha_inicio.date()} | {[p.nombre for p in self.programadores]}"
class Gestor:
    def init(self):
        self.proyectos, self.programadores = {}, {}
    def reg_prog(self, n):
        self.programadores.setdefault(n, Programador(n))
        return self.programadores[n]
    def crear(self, n, fi, ffp, lp=None):
        if n in self.proyectos: return print("Error: ya existe")
        ps = [self.reg_prog(p) for p in (lp or [])]
        self.proyectos[n] = Proyecto(n, fi, ffp, ps)
        print("Creado:", n)
    def mostrar(self):
        for p in self.proyectos.values(): print(p)


class modificar_projecte: