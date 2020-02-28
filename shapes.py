import turtle

class Circle:
    def __init__(self, center, radius, fill_colour = 'red'):
        self.center = center
        self.radius = radius
        self.fill_colour = fill_colour
    
    def get_circumference(self):
        return 3.14 * 2 * self.radius
    
    def get_area(self):
        return 3.14 * self.radius**2
    
    def draw(self, board):
        board.penup()
        board.setpos(self.center[0],self.center[1])
        board.fillcolor(self.fill_colour)
        board.begin_fill()
        board.pendown()
        board.circle(self.radius)
        board.end_fill()

def main():
    turtle.setup(800,600)
    board = turtle.Turtle()
    circle_1 = Circle(center = (20,50), radius = 40, fill_colour='green')
    circle_2 = Circle(center = (-70,50), radius = 40, fill_colour='red')
    circle_3 = Circle(center = (-30,-40), radius = 65, fill_colour='tan')
    circle_1.draw(board)
    circle_2.draw(board)
    circle_3.draw(board)
    turtle.done()

if __name__ == '__main__':
    main()