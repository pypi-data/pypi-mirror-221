class DataHandler():
    def collect_data_for_spreadsheet(self, data):
        if not data:
            # For test purposes
            data_to_export = [
                ['Name', 'Age', 'Email'],  # Header row
                ['Alice', 25, 'alice@example.com'],
                ['Bob', 30, 'bob@example.com'],
            ]

            return data_to_export