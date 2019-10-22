

class Column:
    def __init__(self, simplex):
        self.non_zeroes = sorted(simplex.faces)
        self.simplex = simplex
    
    def __iadd__(self, column):
        # this addition is made assuming we work in Z/2Z
        i, j = 0, 0
        new_column = []
        while i < len(self.non_zeroes) and j < len(column.non_zeroes):
            if self.non_zeroes[i] < column.non_zeroes[j]:
                new_column.append(self.non_zeroes[i])
                i += 1
            elif self.non_zeroes[i] > column.non_zeroes[j]:
                new_column.append(column.non_zeroes[j])
                j += 1
            else:
                i += 1
                j += 1
        if i < len(self.non_zeroes):
            new_column += self.non_zeroes[i:]
        if j < len(column.non_zeroes):
            new_column += column.non_zeroes[j:]

        assert new_column == sorted(new_column)

        self.non_zeroes = new_column
        return self

    def __repr__(self):
        return self.non_zeroes.__repr__()