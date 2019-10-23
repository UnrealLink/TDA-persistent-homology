from functools import total_ordering
from utils import binary_search

@total_ordering
class Simplex:
    def __init__(self, value, dim, *vertices):
        self.value = float(value)
        self.dim = int(dim)
        self.vertices = tuple(sorted([int(x) for x in vertices]))
        self.hash = hash(self.vertices)
        self.faces = list() # indices of faces in sorted simplices list

    def contained(self, simplex):
        for vertex in self.vertices:
            if binary_search(simplex.vertices, vertex) == -1:
                return False
        return True

    def set_faces(self, sorted_complex, index_map):
        if self.dim == 0:
            return
        for i in range(self.dim+1):
            face = Simplex(0., self.dim-1, *[x for j,x in enumerate(self.vertices) if j != i])
            face_index = binary_search(sorted_complex, face, inf_func=lambda s1,s2: s1.vertices<s2.vertices)
            assert face_index != -1
            self.faces.append(index_map.index(face_index))

    def set_faces_hash(self, hash_table):
        if self.dim == 0:
            return
        for i in range(self.dim+1):
            face = Simplex(0., self.dim-1, *[x for j,x in enumerate(self.vertices) if j != i])
            face_index = hash_table.get(face.hash)
            assert face_index != None
            self.faces.append(face_index)

    def __lt__(self, simplex):
        return self.value < simplex.value or self.contained(simplex)

    def __eq__(self, simplex):
        return self.vertices == simplex.vertices
    
    def __len__(self):
        return self.dim + 1

    def __getitem__(self, i):
        return self.vertices[i]

    def __repr__(self):
        return f"{self.value} {self.dim} {self.vertices}"