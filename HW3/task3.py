from task1 import Matrix
import numpy as np


class HashMixin:

    def __hash__(self):
        x = 0
        for i in range(self.n):
            for j in range(self.m):
                x += self.matrix[i][j]
        return x


class HashableMatrix(HashMixin, Matrix):
    _cache = {}

    def __matmul__(self, other):
        pair_hash = (self.__hash__(), other.__hash__())
        if pair_hash not in HashableMatrix._cache:
            HashableMatrix._cache[pair_hash] = HashableMatrix(
                super().__matmul__(other).matrix
            )
        return HashableMatrix._cache[pair_hash]


if __name__ == "__main__":
    A = HashableMatrix([[1, 3], [7, 9]])
    B = HashableMatrix([[1, 2], [3, 4]])
    C = HashableMatrix([[2, 4], [6, 8]])
    D = HashableMatrix([[1, 2], [3, 4]])

    assert hash(A) == hash(C)

    A.write_to_file("artifacts/3.3/A.txt")
    B.write_to_file("artifacts/3.3/B.txt")
    C.write_to_file("artifacts/3.3/C.txt")
    D.write_to_file("artifacts/3.3/D.txt")
    AB = A @ B
    CD = HashableMatrix(np.array(C.matrix) @ np.array(D.matrix))
    AB.write_to_file("artifacts/3.3/AB.txt")
    CD.write_to_file("artifacts/3.3/CD.txt")
    with open("artifacts/3.3/hash.txt", "w") as f:
        print("AB hash:", AB.__hash__(), file=f)
        print("CD hash:", CD.__hash__(), file=f)
