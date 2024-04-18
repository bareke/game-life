from matplotlib import pyplot, animation
from random import randint
from matplotlib import colors


class Space:

    def __init__(self, dimension_x: int, dimension_y: int, number_cells: int) -> None:
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.colormap = colors.ListedColormap(["white", "black"])
        self.matriz = [[randint(a=0, b=1) for _ in range(dimension_x)] for _ in range(dimension_y)]
        self.fig, self.ax = pyplot.subplots(figsize=(5, 5))
        self.img = self.ax.imshow(self.matriz, self.colormap)
        self.animation = animation.FuncAnimation(self.fig, self.update_data, interval=500)
        pyplot.show()

    def update_data(self, *args) -> None:
        self.matriz = [[randint(a=0, b=1) for _ in range(self.dimension_x)] for _ in range(self.dimension_y)]
        self.img.set_data(self.matriz)
        return self.img,

    def show(self) -> None:
        pyplot.show()
