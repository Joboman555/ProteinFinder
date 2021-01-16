# Run this file from the command line to get all the proteins and put them in the proteins folder
from Bio import Entrez

print("Enter your email address: \nThis information is not recorded, and only used for NCBI record keeping.")
Entrez.email = input()


protein_ids = ["NC_000852", "NC_007346", "NC_008724", "NC_009899", "NC_014637", "NC_020104", "NC_023423", "NC_023640",
            "NC_023719", "NC_027867"]

for protein_id in protein_ids:
    with open("./dnaForm/proteins/" + protein_id + ".fasta", 'w') as f:
        handle = Entrez.efetch(db="nucleotide", id=protein_id, rettype="fasta")
        print("Writing " + protein_id + "...")
        f.write(handle.read())
