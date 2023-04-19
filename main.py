import cv2                      # Import the OpenCV library
source = "apple.png"            # Set the source image file name
destination = 'newimage.jpeg'   # Set the destination image file name
scale_percent = 50              # Set the scale percentage for resizing

src = cv2.imread("apple.png", cv2.IMREAD_UNCHANGED)    # Load the source image into memory and store it in the `src` variable

# Convert BGR to RGB
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)   # Convert the color space of the image from BGR (OpenCV default) to RGB

new_width = int(src.shape[1] * scale_percent / 100)   # Calculate the new width of the resized image
new_height = int(src.shape[0] * scale_percent / 100)  # Calculate the new height of the resized image

output = cv2.resize(src, (new_width, new_height))     # Resize the image to the specified dimensions and store it in the `output` variable
cv2.imwrite(destination, output)                    # Write the resized image to disk as a new file
cv2.waitKey(0)                                      # Wait for a key press before closing the window (not used in this code)
