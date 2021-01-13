from django.db import models

# Represents one search of one sequence
class SequenceSearch(models.Model):
    sequence = models.CharField(max_length=200)
    search_timestamp = models.DateTimeField()

    def __str__(self):
            return self.sequence

    def clean(sequence):
        if len(sequence) < 1:
            raise Exception("Search sequence cannot be empty")
        for letter in sequence.upper():
            if letter not in ['A', 'C', 'T', 'G']:
                raise Exception("Invalid character in DNA Sequence: %s" % letter)
        return sequence.upper()


