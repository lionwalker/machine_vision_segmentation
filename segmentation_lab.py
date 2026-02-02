import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_FILE = "images/robodk_imgN.png"
OUTPUT_FILE = "images/robodk_imgN_annotated.png"

img = cv2.imread(INPUT_FILE, cv2.IMREAD_GRAYSCALE)

# hist_cv = cv2.calcHist([img], [0], None, [256], [0, 256])

_, th_binary = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)

num_labels, labeled_img, stats, centroids = cv2.connectedComponentsWithStats(
    th_binary, connectivity=4, ltype=cv2.CV_32S)
print(f'Found {num_labels-1} objects')
for (cx, cy) in centroids[1:]:
    cx, cy = int(cx), int(cy)
    print(f'Centroid: ({cx},{cy})')

i = 1
for (p1x, p1y, size_x, size_y, _) in stats[1:]:
    OBJ1_LABEL = f"({p1x},{p1y})"
    OBJ1_RECT_COORDS = (p1x, p1y, p1x+size_x, p1y+size_y)
    OBJ1_COLOR = (0, 0, 255)
    OBJ1_TEXT_COORDS = (p1x, p1y-10)

    cv2.rectangle(img, (p1x, p1y), (p1x+size_x, p1y+size_y), OBJ1_COLOR, 2)
    cv2.putText(
        img,
        OBJ1_LABEL,
        OBJ1_TEXT_COORDS,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 0),
        1,
        cv2.LINE_AA
    )

    i += 1

    print(
        f'Object inside the rectangle with coordinates ({p1x},{p1y}), ({p1x+size_x}, {p1y+size_y})')


cv2.imwrite(OUTPUT_FILE, img)
print(f"Successfully saved annotated image to {OUTPUT_FILE}")

'''
__, th_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
th_mean = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blockSize=5,
    C=2)
th_gauss = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize=5,
    C=2)

plt.figure(figsize=(12, 6))

plt.subplot(3, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Image')

plt.subplot(3, 2, 2)
plt.vlines(range(256), 0, hist_cv)
plt.title('Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])

plt.subplot(3, 2, 3)
plt.imshow(th_binary, cmap='gray', vmin=0, vmax=255)
plt.title('Binary Thresholding')

plt.subplot(3, 2, 4)
plt.imshow(th_otsu, cmap='gray', vmin=0, vmax=255)
plt.title('Otsu Thresholding')

plt.subplot(3, 2, 5)
plt.imshow(th_mean, cmap='gray', vmin=0, vmax=255)
plt.title('Adaptive Thresholding (Mean)')

plt.subplot(3, 2, 6)
plt.imshow(th_gauss, cmap='gray', vmin=0, vmax=255)
plt.title('Adaptive Thresholding (Gauss)')

plt.tight_layout()
plt.show()
'''
