"""Role model definition."""

class Role:
    """Role model."""

    def __init__(self, name: str, description: str):
        """Initialize a Role instance."""
        self.name = name
        self.description = description

    #getter for the name 
    @property
    def name(self):
        """Get the name of the role."""
        return self._name

    #setter for the name
    @name.setter
    def name(self, value):
        """Set the name of the role."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value 
 

    def __str__(self):        
        return f"Role(name='{self.name}', description='{self.description}')"