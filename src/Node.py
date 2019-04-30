class Node():
    def __init__(self, x_pos = -1, y_pos = -1):
        '''

        '''
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = "X" + str(x_pos)+'Y' + str(y_pos)
        pass