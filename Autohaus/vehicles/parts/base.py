class Part:
    def get_data(self, **kwargs):
        data = self.__dict__.copy()
        data["type"] = self.__class__.__name__
        return data
    
















