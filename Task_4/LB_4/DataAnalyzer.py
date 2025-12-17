class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_indices(self):
        """Формує список індексів цін на житло."""
        indices = [
            {'ID': entry['_id'], 'period': entry['period'], 'index1': entry['index1'],
             'index2': entry['index2'], 'index3': entry['index3'], 'index4': entry['index4']}
            for entry in self.data
        ]
        return indices

    def get_periods(self):
        """Формує список унікальних періодів з даних CSV."""
        periods_set = set()
        for entry in self.data:
            periods_set.add(entry['period'])

        periods = [{'id': idx + 1, 'period': period} for idx, period in enumerate(periods_set)]
        return periods

    def get_indices_by_period(self):
        """Формує відношення індексів до періодів."""
        indices_by_period = {}
        for entry in self.data:
            period = entry['period']
            index_data = {
                'index1': entry['index1'],
                'index2': entry['index2'],
                'index3': entry['index3'],
                'index4': entry['index4']
            }
            indices_by_period[period] = index_data
        return indices_by_period