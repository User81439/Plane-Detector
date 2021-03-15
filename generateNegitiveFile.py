import os


def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('planes/not'):
            f.write('planes/not/' + filename + '\n')

####

#  first; from generateNegitiveFile import generate_negative_description_file
#  next;  generate_negative_description_file()
