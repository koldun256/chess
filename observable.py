class Observable:
    def __init__(self):
        self.callbacks = []

    def connect(self, callback):
        self.callbacks.append(callback)

    def emit(self, *args, **kwargs):
        for callback in [*self.callbacks]:
            callback(*args, **kwargs)
