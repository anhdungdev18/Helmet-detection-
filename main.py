import os
import sys

import cv2
import supervision as sv
import torch
from ultralytics import YOLO

from utils.helperFunctions import checkHeads, imageLoader, saveResultCSV


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "hemletYoloV8_100epochs.pt")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Custom trained Model we are using for helmet detection
model = YOLO(MODEL_PATH)
model.to(DEVICE)

# frame width and height
frame_wid = 640
frame_hyt = 480
SUPPORTED_VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv", ".wmv"}
MAX_VIDEO_DIMENSION = 1280


def build_labels(results, detections):
    return [results.names[class_id] for class_id in detections.class_id]


def resize_video_frame(frame, max_dimension=MAX_VIDEO_DIMENSION):
    height, width = frame.shape[:2]
    longest_side = max(height, width)
    if longest_side <= max_dimension:
        return frame

    scale = max_dimension / float(longest_side)
    resized_width = int(width * scale)
    resized_height = int(height * scale)
    return cv2.resize(frame, (resized_width, resized_height))


def processImages(image_path_list, image_name_list, image_storage_folder):
    """
    Process images in the given list, detect helmets using a pre-trained YOLOv5 model,
    and store the annotated images and detection results in the output folder.

    Args:
        - image_path_list: A list of image paths to be processed.
        - image_name_list: A list of image names corresponding to the images in image_path_list.
        - image_storage_folder: The path to the output folder where annotated images and detection results are to be stored.

    Returns:
        - csv_result_msg_final: A list of messages containing the detection results for each image in the input list.
    """

    box_annotator = sv.BoxAnnotator(thickness=2)
    label_annotator = sv.LabelAnnotator(text_scale=0.5, text_thickness=1)

    csv_result_msg_final = []

    for i in range(len(image_path_list)):
        frame = cv2.imread(image_path_list[i])
        if frame is None:
            print(f"[!] Could not read image: {image_path_list[i]}")
            continue

        # print("Before Compression")
        # show_file_size(image_path_list[i])

        # Resize the image to a fixed size
        image = cv2.resize(frame, (frame_wid, frame_hyt))

        # Use the pre-trained YOLOv5 model to detect helmets
        results = model(image, device=DEVICE)[0]
        detections = sv.Detections.from_ultralytics(results)
        labels = build_labels(results, detections)

        # Annotate the image with bounding boxes around the detected helmets
        image = box_annotator.annotate(scene=image, detections=detections)
        image = label_annotator.annotate(scene=image, detections=detections, labels=labels)

        # Check if the detected helmets are properly worn, and add the detection result to the output list
        csv_result_msg_final = checkHeads(
            labels,
            image_name_list,
            image_path_list,
            image,
            csv_result_msg_final,
            i,
            image_storage_folder,
        )

        # Show the annotated image
        # cv2.imshow("Helmet Detection", image)
        # if cv2.waitKey(1) == 27:
        #     break

    return csv_result_msg_final


def processVideo(video_path, output_folder_name):
    """
    Process a video file, draw detection boxes and labels on each frame,
    and save the annotated video in the output folder.
    """

    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    fps = capture.get(cv2.CAP_PROP_FPS) or 25.0

    output_video_path = os.path.join(
        output_folder_name,
        f"{os.path.splitext(os.path.basename(video_path))[0]}_annotated.mp4",
    )
    writer = None

    box_annotator = sv.BoxAnnotator(thickness=2)
    label_annotator = sv.LabelAnnotator(text_scale=0.5, text_thickness=1)

    frame_count = 0
    while True:
        success, frame = capture.read()
        if not success:
            break

        resized_frame = resize_video_frame(frame)
        results = model(resized_frame, device=DEVICE, imgsz=640)[0]
        detections = sv.Detections.from_ultralytics(results)
        labels = build_labels(results, detections)

        annotated_frame = box_annotator.annotate(scene=resized_frame.copy(), detections=detections)
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame,
            detections=detections,
            labels=labels,
        )

        if writer is None:
            output_height, output_width = annotated_frame.shape[:2]
            writer = cv2.VideoWriter(
                output_video_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (output_width, output_height),
            )

        writer.write(annotated_frame)
        frame_count += 1

    capture.release()
    if writer is not None:
        writer.release()

    print(
        f"Annotated video saved to '{output_video_path}'\nProcessed {frame_count} frames"
    )


if __name__ == "__main__":
    """
    Main function for the helmet detection program. Parses command line arguments to determine
    the input folder containing images to be processed, and the output folder where annotated
    images and detection results are to be stored. Calls the processImages function to perform
    helmet detection on the input images.
    """
    try:
        if len(sys.argv) < 2:
            raise ValueError("Usage: python main.py <folder-path-containing-images>")

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

        input_path = os.path.abspath(" ".join(sys.argv[1:]).strip())
        input_name = os.path.splitext(os.path.basename(input_path))[0]
        output_folder_name = os.path.join(BASE_DIR, "Result", input_name)
        image_storage_folder = os.path.join(output_folder_name, "images")

        if os.path.isdir(input_path):
            os.makedirs(image_storage_folder, exist_ok=True)

            # Load images from input folder and perform helmet detection
            image_path_list, image_name_list = imageLoader(input_path)
            if not image_path_list:
                raise ValueError(f"No supported image files found in: {input_path}")

            result = processImages(image_path_list, image_name_list, image_storage_folder)

            # Save detection results to a CSV file
            saveResultCSV(result, output_folder_name, csv_file_name=input_name)

            print(
                f"Images saved to '{image_storage_folder}' \nCSV file generate saved to '{output_folder_name}'"
            )
        elif os.path.isfile(input_path) and os.path.splitext(input_path)[1].lower() in SUPPORTED_VIDEO_EXTENSIONS:
            os.makedirs(output_folder_name, exist_ok=True)
            processVideo(input_path, output_folder_name)
        else:
            raise FileNotFoundError(f"Input path not supported: {input_path}")

    except Exception as error:
        print(f"[!] Some error occured during processing: {error} [!]")
