import math

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    angle = math.radians(360 / (number_of_sides*2))
    
    apothom = circle_radius * math.sin(angle)
    
    adjacent = circle_radius *  math.cos(angle)
    
    area = apothom * adjacent * number_of_sides
    
    return round(area, 3)