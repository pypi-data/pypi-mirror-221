class Exporter():
    def __init__(self, model=None):
        super().__init__()
        self.model = model

    def export_all_model_data(self):
        print("exporting data ..")