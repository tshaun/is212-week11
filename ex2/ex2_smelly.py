'''class Shape:
    def calculate_area(self, shape_type, **kwargs):
        if shape_type == 'circle':
            radius = kwargs.get('radius')
            return 3.14 * radius * radius
        elif shape_type == 'rectangle':
            length = kwargs.get('length')
            width = kwargs.get('width')
            return length * width
        elif shape_type == 'triangle':
            base = kwargs.get('base')
            height = kwargs.get('height')
            return 0.5 * base * height
'''
class Shape:
    def calculate_area(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method.")
    
class Circle(Shape):
    def calculate_area(self, **kwargs):
        radius = kwargs.get('radius')
        return 3.14 * radius * radius
    
class Rectangle(Shape):
    def calculate_area(self, **kwargs):
        length = kwargs.get('length')
        width = kwargs.get('width')
        return length * width

class Triangle(Shape):
    def calculate_area(self, **kwargs):
        base = kwargs.get('base')
        height = kwargs.get('height')
        return 0.5 * base * height
    

    

