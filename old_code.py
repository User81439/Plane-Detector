#capture = cv2.VideoCapture("https://s8.ipcamlive.com/streams/08dftlcyxesvwdrh9/stream_0013258_L3000.ts")
#capture = cv2.VideoCapture(0)

# playlist = m3u8.load('https://s8.ipcamlive.com/streams/08dftlcyxesvwdrh9/stream.m3u8')
#print(playlist.segments)
# print(playlist.files)

# test = playlist.files

# print(test[0])


# while True:
#
#     ret, frame = capture.read()
#     cv2.imshow("window_name", frame)
#
#     for i in range(20):
#         #sleep(60 - time() % 60)
#         return_value, image = capture.read()
#         cv2.imwrite('planes/opencv' + str(i) + '.png', image)
#     exit()
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()