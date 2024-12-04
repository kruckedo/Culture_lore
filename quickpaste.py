from PIL import Image
import numpy as np

# Create a sample RGB 4x4 image
pixels = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]],  # Row 1
    [[0, 255, 255], [255, 0, 255], [128, 128, 128], [0, 0, 0]],  # Row 2
    [[128, 0, 0], [0, 128, 0], [0, 0, 128], [128, 128, 0]],  # Row 3
    [[0, 128, 128], [128, 0, 128], [255, 255, 255], [64, 64, 64]]  # Row 4
], dtype=np.uint8)

# Convert RGB to YCrCb
def rgb_to_ycrcb(rgb_image):
    # Conversion matrix from RGB to YCrCb
    transformation_matrix = np.array([
        [0.299, 0.587, 0.114],  # Y
        [-0.168736, -0.331264, 0.5],  # Cr
        [0.5, -0.418688, -0.081312]  # Cb
    ])
    offset = np.array([0, 128, 128])  # Offset for Cr and Cb
    
    # Apply transformation
    ycrcb_image = np.dot(rgb_image, transformation_matrix.T) + offset
    return ycrcb_image.astype(np.uint8)

ycrcb_pixels = rgb_to_ycrcb(pixels)

# Extract Y, Cr, and Cb components
Y = ycrcb_pixels[:, :, 0]  # Luma
Cr = ycrcb_pixels[:, :, 1]  # Red-difference chroma
Cb = ycrcb_pixels[:, :, 2]  # Blue-difference chroma

# Convert components back to PIL Images
rgb_image = Image.fromarray(pixels, 'RGB')  # Original RGB image
y_image = Image.fromarray(Y, 'L')  # Luma
cr_image = Image.fromarray(Cr, 'L')  # Chroma (Cr)
cb_image = Image.fromarray(Cb, 'L')  # Chroma (Cb)

# Reconstruct YCrCb as a colored image for visualization
ycrcb_colored = np.zeros_like(pixels)
ycrcb_colored[:, :, 0] = Y  # Use Y as brightness
ycrcb_colored[:, :, 1] = Cr  # Use Cr as red-difference
ycrcb_colored[:, :, 2] = Cb  # Use Cb as blue-difference
ycrcb_image = Image.fromarray(ycrcb_colored, 'RGB')

# Display all images
rgb_image.show(title="RGB Image")
y_image.show(title="Luma (Y)")
cr_image.show(title="Chroma (Cr)")
cb_image.show(title="Chroma (Cb)")
ycrcb_image.show(title="YCrCb Image")

# Display inline in Jupyter
(rgb_image, y_image, cr_image, cb_image, ycrcb_image)
