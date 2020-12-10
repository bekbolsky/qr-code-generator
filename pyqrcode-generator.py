import pyqrcode as pqr


with open("links.txt", "r") as infa:
    linki = infa.read().splitlines()

for i in range(len(linki)):
    qr = pqr.create(linki[i], error="H")
    qr.png(
        "qrcode_" + str(i + 1) + ".png",
        scale=8,
        module_color=(46, 55, 65, 255),
        background=(255, 255, 255, 0),
        quiet_zone=0,
    )
    print("Printing QR code to the link - " + linki[i])
