import cv2
import mediapipe as mp
import argparse

import os 
if not os.path.exists('output'):
    os.makedirs('output')

def process_img(img, face_detection):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    H, W, _ = img.shape
    if out.detections is not None:
        for detection in out.detections:
            bbox = detection.location_data.relative_bounding_box
            x1, y1, x2, y2= bbox.xmin, bbox.ymin, (bbox.xmin + bbox.width), (bbox.ymin + bbox.height)
            x1 = int(x1 * W)
            y1 = int(y1 * H)
            x2 = int(x2 * W)
            y2 = int(y2 * H)
            # blur faces
            img[y1:y2, x1:x2, :] = cv2.blur(img[y1:y2, x1:x2, :], (30, 30)) # area , blur strength
    return img


args = argparse.ArgumentParser()

# args.add_argument('--mode', default = 'image')
# args.add_argument('--filePath', default = 'data/testImg.jpg')

# args.add_argument('--mode', default = 'video')
# args.add_argument('--filePath', default = 'data/testVideo.mp4')

args.add_argument('--mode', default = 'webcam')
args.add_argument('--filePath', default = None)

args = args.parse_args()

# detect faces 
with mp.solutions.face_detection.FaceDetection(model_selection = 0, min_detection_confidence = 0.5) as face_detection:
    # image
    if args.mode in ['image']:
        # read image
        img = cv2.imread(args.filePath)
        H, W, _ = img.shape

        # detect face and blur face
        img = process_img(img, face_detection)

        # save image        
        cv2.imwrite('output/output_face_blur.png', img)

    # video
    elif args.mode in ['video']:
        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()
        
        output_video = cv2.VideoWriter('output/output_video.mp4',
                                       cv2.VideoWriter_fourcc(*'MP4V'),
                                       25,
                                       (frame.shape[1], frame.shape[0])
                                       )
               
        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            ret, frame = cap.read()

        cap.release()
        output_video.release()
    
    # web cam
    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        
        while ret:
            frame = process_img(frame, face_detection)
            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            ret, frame = cap.read()
        
        cap.release()