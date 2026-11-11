"""Run the trained YOLOv8 tool detector with tracking over an endoscopic video.

Usage:
    python detection/track_video.py --weights path/to/best.pt --video path/to/video.mp4

Press q to quit the preview window.
"""
import argparse

import cv2
from ultralytics import YOLO


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--weights", required=True, help="path to trained YOLOv8 weights (.pt)")
    parser.add_argument("--video", required=True, help="path to an endoscopic video (.mp4)")
    args = parser.parse_args()

    model = YOLO(args.weights)
    cap = cv2.VideoCapture(args.video)

    while True:
        ok, frame = cap.read()
        if not ok:  # end of video
            break
        results = model.track(frame, persist=True)  # detect and keep IDs across frames
        cv2.imshow("CV in ESS: tool tracking", results[0].plot())
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
