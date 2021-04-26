import os


def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg4.txt', 'w') as f:
        # loop over all the filenames
        neg_dir = 'Images/empty4_sorted/'
        for filename in os.listdir(neg_dir):
            f.write(neg_dir + filename + '\n')


def rename_files():
    directory = "Images/planes4/"
    # directory = "Images/empty4_/"
    img_type = "plane_"
    # img_type = "empty_"
    img_location = 'Images/planes4/'
    # img_location = 'Images/empty4_/'
    img_destination = 'Images/planes4_sorted/'
    # img_destination = 'Images/empty4_sorted/'

    for count, filename in enumerate(os.listdir(directory)):
        new_name = img_type + str(count) + ".jpg"
        source = img_location + filename
        destination = img_destination + new_name
        os.rename(source, destination)
