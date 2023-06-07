from difflib import Differ
from difflib import SequenceMatcher
import glob
import os

# Define where the assignment files are
directory_path = 'Subory/Multiple Assignment Files'

# Define pattern to match files
file_pattern = os.path.join(directory_path,'*.py')

# Retrieve a list of file paths matching the pattern
file_paths = glob.glob(file_pattern)

for file_path in file_paths:
    file_name = os.path.basename(file_path)
    with open(file_path, 'r') as AssignmentFile, open('Subory/Example Files/number guesser.py', 'r') as ExampleFile:
        assignment = AssignmentFile.readlines()  # Reads them; preparing them for comparison and closes them afterward
        example = ExampleFile.readlines()  # -II-
        differobject = Differ()  # Prepares differ object

        print("-----------------------------------------------------------------------------------")
        print(" ")
        print("File name: " + file_name)
        print(" ")
        for Difference in differobject.compare(assignment, example):
            print(Difference)
            filexd = open("Lolita.txt", "a")
            filexd.writelines(Difference)
            filexd.close()
        print("-----------------------------------------------------------------------------------")

        sm = SequenceMatcher(a=assignment, b=example)
        SimilarityRatio = sm.ratio()
        print("Similarity: " + str(SimilarityRatio * 100) + (" %"))




