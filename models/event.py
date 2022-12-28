class BuildInstruction:

    x: int
    y: int
    z: int
    model: str

    def __init__(self, x: int, y: int, z: int, model: str):
        self.x = x
        self.y = y
        self.z = z
        self.model = model

class Event:

    method: object
    parameters: object
    duration: int

    def __init__(self, method, params, duration):
        self.method = method
        self.parameters = params
        self.duration = duration