import os

class Match:
    def __init__(self, file_path, full_sequence, search_sequence):
        self.file_path = file_path
        self.full_sequence = full_sequence
        self.search_sequence = search_sequence

    def getProteinName(self):
        base=os.path.basename(self.file_path)
        return os.path.splitext(base)[0]
