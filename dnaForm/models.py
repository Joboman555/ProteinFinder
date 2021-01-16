import os
from django.db import models
from .match import Match
from Bio import SeqIO

# Represents one search of one sequence
class SequenceSearch(models.Model):
    sequence = models.CharField(max_length=200)
    search_timestamp = models.DateTimeField()
    protein_sequence = models.CharField(max_length=1000)
    protein_name = models.CharField(max_length=20)

    def __str__(self):
            return self.sequence

    def clean(sequence):
        if len(sequence) < 1:
            raise Exception("Search sequence cannot be empty")
        for letter in sequence.upper():
            if letter not in ['A', 'C', 'T', 'G']:
                raise Exception("Invalid character in DNA Sequence: %s" % letter)
        return sequence.upper()



    def findMatches(sequence):

         # gets all file handles in folder
        def absoluteFilePaths(directory):
           for root, dirs, files in os.walk(os.path.abspath(directory)):
                       for file in files:
                           yield(os.path.join(root, file))

        # get sequences in proteins folder
        files_traversed = 0
        for seq_file in absoluteFilePaths("./dnaForm/proteins/"):
            files_traversed += 1
            for seq_record in SeqIO.parse(seq_file, "fasta"):
                if sequence in seq_record:
                    return Match(seq_file, seq_record, sequence)

        # this means getProteins.py hasn't been run, because protein files haven't been populated
        if files_traversed == 0:
            raise Exception("No protein files to look at. Please run getProteins.py from command line.")
        return None








