## Lab assignment: Segmentation
### Week 1( 02/02/2026)

### Lab Overview
A. Take a simulated image from RoboDK and perform segmentation.

 - Apply thresholding
 - Clean up binary images using morphological operations
 - Extract basic object features (contours, area, centroid)
 - Annotate and visualize detected object positions on the image

B. Capture a real image on the scenario (tiles on the table) and perform segmentation.

By the end of this lab, learn first end-to-end pipeline from a camera image to object locations – a building block for vision-based pick-and-place.

### Learning Goals

 - Choose and apply appropriate thresholding methods for a given image.
 - Use morphological operations to improve segmentation quality.
 - Find connected components/contours in a binary image.
 - Annotate detected objects on the image.


### Part A - Simulated Image

1. Task A1 - Create Simulated Scenario

2. Task A2 - Capture image from RoboDK Simulated Camera

3. Task A3 - Thresholding

4. Task A4 - Cleaning with Morphology

5. Task A5 – Contours, Area, and Centroid

### Part B – Real Image

1. Capture at least 4 new real images with paper markers or tiles on the table:

    - one image with the black paper markers

    - other with mosaic tiles all of the same dark color

    - another with mosaic tiles with mixed dark colors

    - and one with mosaic tiles with mixed bright and dark colors

2. Apply the same pipeline (use your code of part A) to each image:

    - Load image → preprocessing (if needed) → thresholding → morphology → contours → centroids → annotation.

3.Check:
    - Does the pipeline still work?
    - Is preprocessing (filtering) needed?
    - Are morphology operations needed?

    
### Discussion:

- Q1: Which thresholding method gave the most stable results across your images?
- Q2: Did filtering and morphology help improve segmentation?
- Q3: What kinds of errors still remain (false positives, missed objects, shape distortions)?
- Q4: How would you change the lighting or camera setup in the real lab to make segmentation easier?

Discuss your findings (how easy it was, how long did it take, how fast it processes the images, etc.) about the process.