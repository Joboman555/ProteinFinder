from django.db import models

# Represents one search of one sequence
class SequenceSearch(models.Model):
    sequence = models.CharField(max_length=200)
    search_timestamp = models.DateTimeField()

    def __str__(self):
            return self.sequence


