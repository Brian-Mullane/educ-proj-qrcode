import qrcode

img = qrcode.make("https://github.com/Brian-Mullane/educ-proj-qrcode")

img.save("qrcode.png")

img.show()
