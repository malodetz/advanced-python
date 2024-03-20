import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrices have different shape")
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.m)]
            for i in range(self.n)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrices have different shape")
        result = [
            [self.matrix[i][j] * other.matrix[i][j] for j in range(self.m)]
            for i in range(self.n)
        ]
        return Matrix(result)

    def __matmul__(self, other):
        if self.m != other.n:
            raise ValueError(
                "Matrices have incompatible dimensions for matrix multiplication"
            )
        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(other.n))
                for j in range(other.m)
            ]
            for i in range(self.n)
        ]
        return Matrix(result)

    def shape(self):
        return self.n, self.m

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            for row in self.matrix:
                f.write(" ".join(str(x) for x in row) + "\n")


if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_add = matrix1 + matrix2
    matrix_add.write_to_file("artifacts/3.1/matrix+.txt")
    matrix_mul = matrix1 * matrix2
    matrix_mul.write_to_file("artifacts/3.1/matrix*.txt")
    matrix_matmul = matrix1 @ matrix2
    matrix_matmul.write_to_file("artifacts/3.1/matrix@.txt")
