from .gearbox import Gearbox

class ManualGearbox(Gearbox):
    def __init__(self, gears, **kwargs) -> None:
        super().__init__()
        self.gears = gears
        self.displayname = f"Manuell {gears} Gänge"

        self.infotext = f"""
    Manuelles Getriebe:
        Gänge: {self.gears}
    """

    def get_required_values():
        return ["gears"]