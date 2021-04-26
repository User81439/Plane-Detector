import utils
from PlaneViewer import PlaneViewer
from URLbuilder import URLbuilder


def main():

    media_type = "static"
    # media_type = "live"
    classifier_version = "cascade4"  # cascade[-4]
    enable_img_capture = False
    demo_mode = True

    if media_type == "live":
        lc = URLbuilder()
        source = lc.get_stream_url()

    elif media_type == "static":
        source = 'Images/planes4_sorted/plane_0.jpg'
        enable_img_capture = False

    else:
        raise Exception("invalid media type. try; static or live")

    pv = PlaneViewer(source)
    pv.plane_detector(enable_img_capture, classifier_version, demo_mode)

    #  be careful when running, only do when needed
    # utils.rename_files()
    # utils.generate_negative_description_file()


if __name__ == '__main__':
    main()
