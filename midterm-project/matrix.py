class Matrix:
    def __init__(self, data):
        rows, cols = self.check_size(data)
        self.data = data
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return f"{self.data}"

    def check_size(self, data):
        rows = len(data)
        cols = 0
        for x in data:
            if cols != 0:
                if cols != len(x):
                    raise ValueError('raise ValueError("different row sizes")')
            cols = len(x)
        return rows, cols

    def __add__(self, other):
        self.check_add_sizes(other)
        output = [[k + h for k, h in zip(i, j)] for i, j in zip(self.data, other.data)]
        output = Matrix(output)
        return output

    def check_add_sizes(self, other):
        if other.rows == self.rows:
            if other.cols != self.cols:
                raise ValueError('raise ValueError("different matrix sizes")')
        else:
            raise ValueError('raise ValueError("different matrix sizes")')
        pass

    def __mul__(self, other):
        self.check_mul_sizes(other)
        output = []
        for s_row in range(self.rows):
            answer = []
            for o_col in range(other.cols):
                result = 0
                for s_col in range(self.cols):
                    result += self.data[s_row][s_col] * other.data[s_col][o_col]
                answer.append(result)
            output.append(answer)
        output = Matrix(output)
        return output

    def check_mul_sizes(self, other):
        if self.cols != other.rows:
            raise ValueError('raise ValueError("not able to multiply")')
        pass

