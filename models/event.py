class Event:

    method: object
    parameters: object
    duration: int

    def __init__(self, method, params, duration):
        self.method = method
        self.parameters = params
        self.duration = duration