class Enemy:

    def __init__(self, x, y, born, died, hit, image):
        """ Initializes Enemy object.
            Keyword argumets:
            x -- x coordinate of the image
            y -- y coordinate of the image
            born -- start time of displaying the image in ms
            died -- end time of displaying the image in ms
            hit -- shows if the enemy is clicked
            image -- image of the enemy
        """
        self.x = x
        self.y = y
        self.born = born
        self.died = died
        self.hit = hit
        self.image = image
