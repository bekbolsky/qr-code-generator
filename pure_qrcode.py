import qrcode


with open("links_list.txt", "r") as infa:
    linki = infa.read().splitlines()

for i in range(len(linki)):
    link_to_video = linki[i]
    qr = qrcode.QRCode()
    qr.save("test_" + str(i + 1) + ".png")
    print("Printing QR code to the link - " + linki[i])
