import os


def rename(path, header):
    i = 1

    for filename in os.listdir(path):
        dest = path + header + str(i) + ".jpg"
        src = path + filename

        os.rename(src, dest)
        i += 1


if __name__ == '__main__':
    # Rename Planes
    rename('/Users/elp/Downloads/plane-master/plane/planes/planes/', 'plane_')
    # Rename Not Planes
    rename('/Users/elp/Downloads/plane-master/plane/planes/not/', 'empty')
