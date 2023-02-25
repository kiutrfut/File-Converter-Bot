import cv2

# Load the input image
img = cv2.imread('path/to/input/image.jpg')

# Load the colorization model
prototxt = 'path/to/colorization_deploy_v2.prototxt'
model = 'path/to/colorization_release_v2.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize the grayscale image to match the input shape of the model
h, w = img.shape[:2]
resized = cv2.resize(gray, (w, h))

# Normalize the input image (resize and subtract mean)
input_blob = cv2.dnn.blobFromImage(resized, scalefactor=1.0, size=(w, h), mean=(128, 128, 128), swapRB=False, crop=False)

# Set the input to the model and forward pass to get the output
net.setInput(input_blob)
output = net.forward()

# Reshape the output to match the input shape of the model
output = output.reshape((2, h, w))

# Merge the output channels and convert to BGR color space
output = output.transpose(1, 2, 0)
output = cv2.resize(output, (w, h))
output = (output * 255).astype("uint8")
output = cv2.cvtColor(output, cv2.COLOR_LAB2BGR)

# Display the output image
cv2.imshow('Colorized Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
