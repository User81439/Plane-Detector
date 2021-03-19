import os

###############################
# change to test data to test #
###############################


class renameFile:

    def rename(self):
        # directory = "Images/planes/"
        directory = "Images/not/"
        # img_type = "plane_"
        img_type = "empty_"
        # img_location = 'Images/planes/'
        img_location = 'Images/not/'
        # img_destination = 'Images/planes_sorted/'
        img_destination = 'Images/empty_sorted/'

        for count, filename in enumerate(os.listdir(directory)):
            new_name = img_type + str(count) + ".jpg"
            source = img_location + filename
            destination = img_destination + new_name
            os.rename(source, destination)
