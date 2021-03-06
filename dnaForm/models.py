import os
from django.db import models
from .match import Match
from Bio import SeqIO
from celery.decorators import task

# Represents one search of one sequence
class SequenceSearch(models.Model):
    sequence = models.CharField(max_length=200)
    search_timestamp = models.DateTimeField()
    protein_sequence = models.CharField(max_length=1000)
    protein_name = models.CharField(max_length=20)
    position = models.IntegerField()
    still_running = models.BooleanField()

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


    # updates the database with the search results
    # this is run async
    @task(name="run_protein_search")
    def runSearch(search_id):
        print("-----------------------------------Running search")
        search = SequenceSearch.objects.get(pk=search_id)
        match = SequenceSearch.findMatches(search.sequence)
        if match is not None:
            search.protein_sequence=match.full_sequence
            search.protein_name=match.getProteinName()
            search.position=match.getPosition()
            search.still_running=False
        else:
            search.protein_sequence="-"
            search.protein_name="No Match Found"
            search.position=-1
            search.still_running=False
        search.save()








