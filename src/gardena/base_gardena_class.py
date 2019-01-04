class BaseGardenaClass:
    """Base class for information retrieved by gardena"""

    id = None
    name = None

    def __init__(self, smart_system=None):
        """Constructor, create instance of a gardena device"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        self.smart_system = smart_system

    def set_field_if_exists(self, hashmap, hashmap_key, field_name):
        if hashmap_key in hashmap:
            setattr(self, field_name, hashmap[hashmap_key])

    def update_information(self, information):
        self.id = information["id"]
        self.name = information["name"]
