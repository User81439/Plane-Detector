import os


def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        neg_dir = 'Images/empty_sorted/'
        for filename in os.listdir(neg_dir):
            f.write(neg_dir + filename + '\n')


def rename_files():
    directory = "Images/planes3/"
    # directory = "Images/not/"
    img_type = "plane3_"
    # img_type = "empty_"
    img_location = 'Images/planes3/'
    # img_location = 'Images/not/'
    img_destination = 'Images/planes3_sorted/'
    # img_destination = 'Images/empty_sorted/'

    for count, filename in enumerate(os.listdir(directory)):
        new_name = img_type + str(count) + ".jpg"
        source = img_location + filename
        destination = img_destination + new_name
        os.rename(source, destination)
