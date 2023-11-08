class Spline:
    
    _points = [[0,0]]
    
    def __init__(self, points_list : list):
        self._points = points_list
    
    def intl(self, x):
        for i in range(1, len(self._points)):
            if self._points[i-1][0] <= x <= self._points[i][0]:
                return i
                

class LinearSpline(Spline):
    def __call__(self, x: int):
        i = super().intl(x)
        return self._points[i-1][1] * ((self._points[i][0] - x) / (self._points[i][0] - self._points[i-1][0])) + self._points[i][1] * ((x - self._points[i-1][0]) / (self._points[i][0] - self._points[i-1][0]))
        
 
##CHECK##           
points = [[-3, 9], [-2, 4], [-1, 1], [0, 0], [1, 1], [2, 4], [3, 9]]

B = LinearSpline(points)

print(B(1.56))

