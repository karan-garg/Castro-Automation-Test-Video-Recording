from castro import Castro
from time import sleep
import os

if __name__ == "__main__":

    output_file_path = os.path.join(os.getcwd(), "test_video.swf")
    vnc_file_path = os.path.join(os.getcwd(), "vnc_passwd")
    
    #Create a Castro video object
    video = Castro(filename = output_file_path, passwd = vnc_file_path)

    #start screen recording
    print "\nStarting 10-second screen capture...\n"
    video.start()

    sleep(10)

    #stop recording and save video file
    video.stop()
