def convertMap(image, width, height, x_padding=2, y_padding=2):
    import numpy as np

    # Define new dimensions including padding
    x = int(width + x_padding)
    y = int(height + y_padding)

    # Initialize the image_map with zeros (black)
    image_map = np.zeros((y, x), dtype=np.uint8)  # Create a 2D array with padding

    # Copy pixel values and convert to grayscale with padding
    for i in range(width):
        for j in range(height):
            pixel_value = image.getpixel((i, j))
            # Calculate the grayscale value
            bw_pixel = int((pixel_value[0] + pixel_value[1] + pixel_value[2]) / 3)
            # Store the grayscale value in the padded position
            image_map[j + 1, i + 1] = bw_pixel  # Fill the center of image_map

    return image_map












# def convertMap(image, width, height, x_padding = 2, y_padding = 2):
#     from PIL import Image
#     import numpy as np

#     #begin padding
#     blank_image = Image.new("RGB", (width + x_padding, height + y_padding), color = (0,0,0))
#     for i in range(width):
#         for j in range(height):
#             blank_image.putpixel((i+1,j+1),image.getpixel((i,j)))
#     #end padding

#     #y = width
#     #x = height
#     # lists use (y,x) so i am creating cartesian coordinates here

#     x = int(width+x_padding)
#     y = int(height+y_padding)

#     image_map = np.zeros((y,x),dtype=np.uint8)
#     for i in range(width):
#         for j in range(height):
#             pixel_value = blank_image.getpixel((i,j))
#             bw_pixel = int((pixel_value[0]+pixel_value[1]+pixel_value[2])/3) ##normalizing anyways?
#             if (i + 1) < image_map.shape[1] and (j + 1) < image_map.shape[0]:
#                 image_map[j + 1, i + 1] = bw_pixel  # Store in numpy array (y, x)

#     return image_map



# def convertBW(image,width,height):

#     for i in range(width):
#         for j in range(height):
#             pixel_rgb_value = image.getpixel((i,j))
#             pixel_bw_value = int(((pixel_rgb_value[0] + pixel_rgb_value[1] + pixel_rgb_value[2])/3))
#             pixel_bw = (pixel_bw_value,pixel_bw_value,pixel_bw_value)
#             image.putpixel((i, j), pixel_bw)

#     return image