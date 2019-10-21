from functools import total_ordering

@total_ordering
class Simplex:
    def __init__(self, value, dim, *vertices):
        self.value = float(value)
        self.dim = int(dim)
        self.vertices = tuple(sorted([int(x) for x in vertices]))
        self.faces = list()
        self.hash = hash(self.vertices)

    def contained(self, simplex):
        for vertex in self.vertices:
            if not (vertex in simplex.vertices):
                return False
        return True

    def set_faces(self, sorted_complex):
        for i in range(self.dim+1):
            face = [x for j,x in enumerate(self.vertices) if j != i]
            face_hash = hash(tuple(face))
            for j, simplex in enumerate(sorted_complex):
                if simplex.hash == face_hash:
                    self.faces.append(j)

    def __lt__(self, simplex):
        return self.value < simplex.value or self.contained(simplex)

    def __eq__(self, simplex):
        return self.hash == simplex.hash

    def __repr__(self):
        return f"{self.value} {self.dim} {self.vertices} \n"