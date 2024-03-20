import numpy as np


class GetterMixin:
    def get(self):
        return self._matrix


class SetterMixin:
    def set(self, matrix):
        self._matrix = np.array(matrix)


class ToStringMixin:

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self._matrix)


class FileMixin:
    def write_to_file(self, filename):
        with open(filename, "w") as f:
            print(self.__str__(), file=f)


class Matrix(
    GetterMixin,
    SetterMixin,
    ToStringMixin,
    FileMixin,
    np.lib.mixins.NDArrayOperatorsMixin,
):

    def __init__(self, matrix):
        self._matrix = np.array(matrix)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", ())
        new_inputs = []
        for x in out + inputs:
            if isinstance(x, Matrix):
                new_inputs.append(x._matrix)
            else:
                new_inputs.append(x)
        if out:
            kwargs["out"] = tuple(*inputs)
        result = getattr(ufunc, method)(*new_inputs, **kwargs)
        if isinstance(result, tuple):
            return tuple(type(self)(res) for res in result)
        if method == "at":
            return None
        return type(self)(result)


if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_add = matrix1 + matrix2
    matrix_add.write_to_file("artifacts/3.2/matrix+.txt")
    matrix_mul = matrix1 * matrix2
    matrix_mul.write_to_file("artifacts/3.2/matrix*.txt")
    matrix_matmul = matrix1 @ matrix2
    matrix_matmul.write_to_file("artifacts/3.2/matrix@.txt")
