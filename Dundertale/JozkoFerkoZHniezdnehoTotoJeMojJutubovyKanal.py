from difflib import Differ
from difflib import SequenceMatcher

# Opens le funny guy files
with open('Subory/Assignment Files/number guesser two.py', 'r') as AssignmentFile, open('Subory/Example Files/number guesser.py', 'r') as ExampleFile:
    assignment = AssignmentFile.readlines() # Reads them; preparing them for comparison and closes them afterward
    example = ExampleFile.readlines() # -II-
    differobject = Differ() # Prepares differ object

    print("-----------------------------------------------------------------------------------")

    for Difference in differobject.compare(assignment, example):
        print(Difference)
        filexd = open("OUTPUT.txt", "a")
        filexd.writelines(Difference)
        filexd.close()

    print("-----------------------------------------------------------------------------------")

    sm = SequenceMatcher(a=assignment, b=example)
    SimilarityRatio = sm.ratio()
    print("Similarity: " + str(SimilarityRatio * 100) + (" %"))





