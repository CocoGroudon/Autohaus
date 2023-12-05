from .gearbox import Gearbox

class AutomaticGearbox(Gearbox):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.displayname = "Automatik"

        self.infotext = f"""
    Automatik Getriebe
    """

    def get_required_values():
        return  []