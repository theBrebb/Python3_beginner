import PIL.Image
# from PIL import ImageFilter
# import numpy


def main():
    # path = input("Enter path to image file: \n")
    path = "/Users/elisabetrank/Desktop/HelloWorld/Ascii_Art/Pauli.png"
    # try:

    image = (PIL.Image.open(path))
    image.show()
    # image = int(image)
    # except:
    # print(path, "Unable to read image...")
    # finally:

    ascii_chars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

    def pixel_to_ascii(image):
        pixels = image.getdata()
        print(image.size)
        ascii_str = ""
        for pixel in pixels:
            ascii_str += ascii_chars[pixel//25]
        return ascii_str

    # resize image
    # width, height = image.size
    res_img = image.reduce(1)
    res_img.show()

    # res_image = resize(image)
    # convert image to greyscale image
    grey_img = res_img.convert("L")
    # img_gray_smooth = grey_img.filter(ImageFilter.SMOOTH)
    # edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    # greyscale_image = to_greyscale(res_image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(grey_img)
    img_width = grey_img.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)


main()
