import os


def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('Images/empty_sorted/'):
            f.write('Images/empty_sorted/' + filename + '\n')

def rename_files():
    directory = "Images/planes/"
    # directory = "Images/not/"
    img_type = "plane_"
    # img_type = "empty_"
    img_location = 'Images/planes/'
    # img_location = 'Images/not/'
    img_destination = 'Images/planes_sorted/'
    # img_destination = 'Images/empty_sorted/'

    for count, filename in enumerate(os.listdir(directory)):
        new_name = img_type + str(count) + ".jpg"
        source = img_location + filename
        destination = img_destination + new_name
        os.rename(source, destination)
