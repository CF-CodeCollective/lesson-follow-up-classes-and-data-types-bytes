class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y, -(self.z * other.x - self.x * other.z), self.x * other.y - self.y * other.x)

    def run(self):
        return f"({self.x}, {self.y}, {self.z})"