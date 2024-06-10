class Type:

    def __init__(self, typeName):
        if not isinstance(typeName, str):
            raise TypeError("Type name must be a string")
        self.typeName = typeName

    def __str__(self):
        return self.typeName