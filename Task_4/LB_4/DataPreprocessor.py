class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def add_index_ids(self):
        """Додає унікальний ID для кожного запису індексу цін на житло."""
        for index, entry in enumerate(self.data, start=1):
            entry['_id'] = index
        return self.data