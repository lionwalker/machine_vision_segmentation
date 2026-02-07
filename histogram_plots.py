import numpy as np
import matplotlib.pyplot as plt
import cv2 

img1 = cv2.imread('images/capture_img_dark_tiles.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/capture_img_light_tiles.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('images/capture_img_mix_tiles.jpg', cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('images/capture_img_papers.jpg', cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread('images/robodk_imgN.jpg', cv2.IMREAD_GRAYSCALE)

images = {
    "Dark Tiles": img1,
    "Light Tiles": img2,
    "Mixed Tiles": img3,
    "Papers": img4,
    "RoboDK": img5
}

for name, img in images.items():
    fig, axes = plt.subplots(2, 1, figsize=(6, 6))

    axes[0].imshow(img, cmap='gray')
    axes[0].set_title(name)
    axes[0].axis('off')

    axes[1].hist(img.ravel(), bins=256, range=(0, 256))
    axes[1].set_title('Histogram')
    axes[1].set_xlabel('Pixel Intensity')
    axes[1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()