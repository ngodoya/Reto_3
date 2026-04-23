class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float) -> "Point":
        self.x = new_x
        self.y = new_y
        return self

class Line:
    def __init__(self, start: "Point", end: "Point") -> None:
        self.start = start
        self.end = end
        self.dx, self.dy = self.deltas()
        self.length = self.compute_length()
        self.slope = self.compute_slope()
        

    def deltas(self) -> tuple:
        self.dx = self.start.x - self.end.x
        self.dy = self.start.y - self.end.y
        return self.dx, self.dy

    def compute_slope(self) -> float:
        if self.dx != 0:
            slope = self.dy / self.dx
            print(f"The value of the slope is: {slope}")
            return slope
        else: 
            print("Change in x equal to 0, can't divide by 0")
            return float("inf")
        
    def compute_length(self) -> float:

        lenght = (self.dx**2 + self.dy**2) ** (1/2)
        if lenght != 0:
            print(f"The lenght of the line is: {lenght}")
            return lenght
        else:
            print("No Lenght, it's a point")
            return 0
    def compute_horizontal_cross(self) -> float:
        b = self.start.y - (self.slope * self.start.x)
        if self.slope == float("inf"):
            print(f"no change in x, cross in x axis in {self.start.x}")
            return self.start.x
        elif self.slope == 0:
            if b == 0:
                print("Always cut on the x axis")
                return float("inf")
            else:
                print("Never cross the x axis")
                return float("nan")
        else:
            x_cross = - b / self.slope
            print(f"y would be 0, when x equals to {x_cross}")
            return x_cross
            
    def compute_vertical_cross(self) -> float:
        b = self.start.y - (self.slope * self.start.x)
        if self.dx != 0:
            print(f"x would be 0, when y equals to {b}")
            return b
        else:
            print("No change in x, there's no cross in y axis, it's a parallel line to the y axis")
            return 0
    def discretize_line(self, sub_div: int) -> list:
        points = []
        for i in range(sub_div + 1):
            t = i / sub_div
            curr_x = self.start.x + t * (self.end.x - self.start.x)
            curr_y = self.start.y + t * (self.end.y - self.start.y)
            
            points.append((curr_x, curr_y))
        return points
class Rectangle:
    def __init__(self, line1, line2, line3, line4):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4

    @classmethod
    def from_lines(cls, line1, line2, line3, line4):
        return cls(line1, line2, line3, line4)

p1 = Point(1, 1)
p2 = Point(2, 2)
line = Line(p1, p2)
print(line.compute_slope(), line.compute_length(), line.compute_horizontal_cross(), line.compute_vertical_cross(), line.discretize_line(5))