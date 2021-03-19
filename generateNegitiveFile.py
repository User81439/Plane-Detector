import os


class generateNegitiveFile:

    def generate_negative_description_file(self):
        # open the output file for writing. will overwrite all existing data in there
        with open('neg.txt', 'w') as f:
            # loop over all the filenames
            for filename in os.listdir('Images/empty_sorted/'):
                f.write('Images/empty_sorted/' + filename + '\n')

####

#  first; from generateNegitiveFile import generate_negative_description_file
#  next;  generate_negative_description_file()
