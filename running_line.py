import cv2
import numpy as np
from math import ceil


# Create a video with a running line
def create_video(message, duration=3, fps=30, width=100, height=100):

    # Set the video parameters
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter('running_line.mp4', fourcc, fps, (width, height))

    # Set the video background
    b, g, r = 0x3E, 0x88, 0xE5  # orange
    frame = np.zeros((width, height, 3), np.uint8)
    frame[:, :, 0] = b
    frame[:, :, 1] = g
    frame[:, :, 2] = r

    # Set the starting coordinates of the running line
    x, y = width, height // 2

    # Set the font parameters
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (0xFF, 0xFF, 0xFF)  # white

    # Message size for calculating movement speed
    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    movement = ceil(message_size[0][0] / (fps * duration))

    for _ in range(fps * duration):  # number of frames
        # Frame clearing
        frame[:, :, 0] = b
        frame[:, :, 1] = g
        frame[:, :, 2] = r

        # New coordinates of the running line
        x -= movement

        # Add text to frame
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        # Write frame
        video.write(frame)

    # Сlose video stream
    video.release()


if __name__ == '__main__':
    message = input('Input your message: ')
    create_video(message)