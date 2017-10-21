import random
import os
import time
"""
1	2	3	4	5	6	7	8	9	10
11	12	13	14	15	16	17	18	19	20
21	22	23	24	25	26	27	28	29	30
31	32	33	34	35	36	37	38	39	40
41	42	43	44	45	46	47	48	49	50
51	52	53	54	55	56	57	58	59	60
61	62	63	64	65	66	67	68	69	70
71	72	73	74	75	76	77	78	79	80
81	82	83	84	85	86	87	88	89	90
91	92	93	94	95	96	97	98	99	100
"""
# to find the cell's neighbours, use cell-10, cell+10, cell-1, cell+1 and
# check if they are in [1-100]


def clear():
    os.system("clear")


class Cell:
    __created_cells = 0
    matrix = {}

    def __init__(self):
        Cell.__created_cells += 1
        self.num = Cell.__created_cells
        self.live = random.choice([1, 0])
        self.neighbours = []
        self.live_neighbours = 0
        self.dead_neighbours = 0
        Cell.matrix[Cell.__created_cells] = self

    def __repr__(self):
        if self.live:
            return str(int(self.live))
        return " "

    def kill(self):
        self.live = False

    def wake(self):
        self.live = True

    @classmethod
    def get_neighbours(cls):
        for cell in cls.matrix.values():
            if cell.num + 10 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num + 10])
            if cell.num + 10 - 1 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num + 10 - 1])
            if cell.num + 10 + 1 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num + 10 + 1])
            if cell.num - 10 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num - 10])
            if cell.num - 10 - 1 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num - 10 - 1])
            if cell.num - 10 + 1 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num - 10 + 1])
            if cell.num - 1 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num - 1])
            if cell.num + 1 in range(1, 101):
                cell.neighbours.append(cls.matrix[cell.num + 1])

        for cell in cls.matrix.values():
            if str(cell.num).endswith("1"):
                cell.neighbours.remove(cls.matrix[cell.num + 10 - 1])
                try:
                    cell.neighbours.remove(cls.matrix[cell.num - 1])
                    cell.neighbours.remove(cls.matrix[cell.num - 10 - 1])
                except KeyError:
                    pass
            if str(cell.num).endswith("0"):
                cell.neighbours.remove(cls.matrix[cell.num - 10 + 1])
                try:
                    cell.neighbours.remove(cls.matrix[cell.num + 1])
                    cell.neighbours.remove(cls.matrix[cell.num + 10 + 1])
                except KeyError:
                    pass
        cls.print_matrix()

    @classmethod
    def update_lives(cls):
        for cell in cls.matrix.values():
            cell.live_neighbours = 0
            cell.dead_neighbours = 0
            for n in cell.neighbours:
                if n.live:
                    cell.live_neighbours += 1
                else:
                    cell.dead_neighbours += 1
        # UnderPopulation - Any live cell with fewer than two live neighbours
        # dies, as if caused by underpopulation
        for cell in cls.matrix.values():
            if cell.live and cell.live_neighbours < 2:
                cell.kill()

        # Evolution - Any live cell with two or three live neighbours lives on
        # to the next generation.
            if cell.live and cell.live_neighbours in [2, 3]:
                cell.wake()
        # Overpopulation - Any live cell with more than three live neighbours
        # dies, as if by overpopulation.
            if cell.live and cell.live_neighbours > 3:
                cell.kill()
        # Reproduction - Any dead cell with exactly three live neighbours
        # becomes a live cell, as if by reproduction.
            if not cell.live and cell.live_neighbours == 3:
                cell.wake()
        cls.print_matrix()

    @classmethod
    def print_matrix(cls):
        cell_count = 0
        for cell in cls.matrix.values():
            cell_count += 1
            print(cell, end=" ")
            if cell_count % 10 == 0:
                print("")

    @classmethod
    def run(cls, iterations):
        cls.get_neighbours()
        for _ in range(iterations):
            clear()
            cls.update_lives()
            time.sleep(1)


if __name__ == '__main__':
    for _ in range(100):
        Cell()
