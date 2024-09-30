def convertBW(image,width,height):
    from PIL import Image

    try:
        for i in range(width):
            for j in range(height):
                pixel_rgb_value = image.getpixel((i,j))
                pixel_bw_value = int(((pixel_rgb_value[0] + pixel_rgb_value[1] + pixel_rgb_value[2])/3))
                pixel_bw = (pixel_bw_value,pixel_bw_value,pixel_bw_value)
                image.putpixel((i, j), pixel_bw)
        return image
    
    except:
        bw_image = Image.fromarray(image)
        for i in range(width):
            for j in range(height):
                pixel_rgb_value = bw_image.getpixel((j,i))
                pixel_bw_value = int(((pixel_rgb_value[0] + pixel_rgb_value[1] + pixel_rgb_value[2])/3))
                pixel_bw = (pixel_bw_value,pixel_bw_value,pixel_bw_value)
                image.putpixel((j,i), pixel_bw)
        return image