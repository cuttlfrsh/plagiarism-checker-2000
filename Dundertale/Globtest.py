from glob import glob

# Define pattern to match files
file_pattern = '*.py'

# Retrieve a list of file paths matching the pattern
file_paths = glob.glob(file_pattern)

