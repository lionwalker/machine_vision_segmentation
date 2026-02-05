import cv2
import numpy as np
import matplotlib.pylab as plt


def apply_threshold(
    img_path,
    mode="normal",
    th_value=128,
    invert=True,
    use_otsu=False,
    min_area=500,
):
    img=cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Could not read image")
        return
    
    if mode == "light_tiles":
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_proc = clahe.apply(img)


        th = cv2.adaptiveThreshold(img_proc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 5)

    else:
        if invert == True:
            t_type = cv2.THRESH_BINARY_INV
        else:
            t_type = cv2.THRESH_BINARY


        if use_otsu:
            otsu_val, th = cv2.threshold(img, 0, 255, t_type | cv2.THRESH_OTSU)
        else:
            _, th = cv2.threshold(img, th_value, 255, t_type)

    kernel = np.ones((3,3), np.uint8)
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=1)
    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=1)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(th, connectivity=4)

    annotated = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    objects = 0

    for label in range(1, num_labels):
        x, y, w, h, area = stats[label]

            
        cx, cy = centroids[label]
        cx, cy = int(cx), int(cy)

        objects += 1

        cv2.rectangle(annotated, (x, y), (x + w, y + h), (128, 0, 128), 2)

        cv2.circle(annotated, (cx, cy), 4, (0, 0, 255), -1)

        label_text = f"{x}, {y}"

        cv2.putText(annotated, label_text, (x, max(15, y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.4,  (0,0,255), 1, cv2.LINE_AA)


    out_path = img_path.replace(".jpg", "_annotated.jpg")
    cv2.imwrite(out_path, annotated)
    print("Saved:/n", out_path)


image_settings = [
    ("images/capture_img_light_tiles.jpg", "light_tiles", None, None, None),
    ("images/capture_img_dark_tiles.jpg", "normal", 0, True, True),
    ("images/capture_img_papers.jpg", "normal", 0, True, True),
    ("images/capture_img_mix_tiles.jpg", "light_tiles", None, None, None),
    ("images/robodk_imgN.jpg", "normal", 0, True, True),

]

for img_path, mode, th_value, invert, use_otsu in image_settings:
    apply_threshold(
        img_path,
        mode=mode,
        th_value=th_value if th_value is not None else 128,
        invert=invert if invert is not None else True,
        use_otsu=use_otsu if use_otsu is not None else False,
        min_area=500,
    )