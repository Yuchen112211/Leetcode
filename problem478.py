class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        import random
        import math

        angles = random.randint(0,179)
        x_plex = self.radius * math.sin(angles)
        y_plex = self.radius * math.cos(angles)

        return x_plex, y_plex

        
if __name__ == '__main__':

    radius, x_center, y_center = 1, 0, 0
    obj = Solution(radius,x_center,y_center)
    param1 = obj.randPoint()
    print param1