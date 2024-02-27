class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(a, b):
        return Vector3(a.x + b.x, a.y + b.y, a.z + b.z)

    def subtract(a, b):
        return Vector3(a.x - b.x, a.y - b.y, a.z - b.z)

    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    def cross(a, b):
        return Vector3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
    
    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"