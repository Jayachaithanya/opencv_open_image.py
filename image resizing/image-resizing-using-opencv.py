import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("33170.jpg", 1)

# Resize the image to various scales
half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (0, 0), fx=1.5, fy=1.5)
stretch_linear = cv2.resize(image, (780, 540), interpolation=cv2.INTER_LINEAR)

# Titles and images list
Titles = ["Original", "Half", "Bigger", "Interpolation Linear"]
images = [image, half, bigger, stretch_linear]

# Plotting the images
for i in range(len(images)):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    # Convert BGR to RGB for displaying correctly with Matplotlib
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axes for better visualization

plt.show()
