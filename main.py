import numpy
import math
from uuid import uuid4 as uuid
from PIL import Image

NUMBERS_FILE = "./numbers.txt"     

def normalize(value: int) -> int:
    return value % 255

def createImage(pixelsArray: list, to: str) -> None:
    length = lenOfPixelImageArray(len(pixelsArray))

    pixelsArray = formatPixelImageArray(pixelsArray, length, length)
    pixelsArray = numpy.array(pixelsArray, dtype=numpy.uint8)

    Image.fromarray(pixelsArray).save(f"{to}{ uuid() }.png")

def lenOfPixelImageArray(pixelsLen: int) -> int:
    return math.floor(math.sqrt(pixelsLen))

def formatPixelImageArray(pixels: list, width: int, heigth: int) -> list[list[str]]:

    pixelArray = []

    for i in range(heigth):
        pixelRow = []
        for j in range(width): 

            pixelNormalized = [
                normalize(int(pixels[i*10 + j])),
                normalize(int(pixels[i*10 + j])),
                normalize(int(pixels[i*10 + j]))
            ] 

            pixelRow.append(pixelNormalized)

        pixelArray.append(pixelRow)

    return pixelArray

def wrap(text: str, width: int) -> list[str]:
    return [ text[i: i + width] for i in range(0, len(text), width) ]

def decimalsToPixels(decimals: str) -> list[list[str]]:

    pixels = []

    for pixelRaw in wrap(decimals, 9):
        pixels.append(wrap(pixelRaw, 3))

    return pixels

def getDecimalsFile(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

def main() -> None:
    decimals = getDecimalsFile(NUMBERS_FILE)
    pixels = decimalsToPixels(decimals)
    createImage(pixels, "dist/")

if __name__ == "__main__":
    main()
