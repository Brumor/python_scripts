import time
from subprocess import call
from pynput.mouse import Button, Controller
from fpdf import FPDF
from os import listdir
import re
from PIL import Image


pdf = FPDF()
mouse = Controller()
mouse.position = (1416, 476)


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def screenshot_pages(number_of_pages, x, y, width, height):
    for i in range(number_of_pages):
        call(["screencapture", "-R{},{},{},{}".format(x, y,  width, height), "./screenshots/page_{}.jpg".format(i)])
        mouse.position = (1416, 476)
        mouse.click(Button.left, 1)
        time.sleep(0.25)


def create_pdf_from_jpg_list(name):
    # imagelist is the list with all image filenames
    screenshots = listdir('./screenshots')
    screenshots.sort(key=natural_keys)
    print(screenshots)
    img_list = []
    for image in screenshots:
        print(image)

        img = Image.open('./screenshots/{}'.format(image))
        rgb = Image.new('RGB', img.size, (255, 255, 255))  # white background
        rgb.paste(img, mask=img.split()[3])
        img_list.append(rgb)
    img_list[0].save(name, "PDF", resolution=100.0, save_all=True, append_images=img_list[1:-1])


pdf1_filename = "./Phoenix Project.pdf"

screenshot_pages(480, 791, 60, 600, 850)
create_pdf_from_jpg_list(pdf1_filename)

