import segno


with open("links.txt") as f:
    list_of_links = f.read().splitlines()
    # print(list_of_links, "\n")


for i in range(len(list_of_links)):
    qr = segno.make(list_of_links[i], micro=False)
    qr.save(
        out="QR_edunews" + str(i + 1) + ".png",
        scale=6,
        border=0,
        dark=(23, 54, 93),
        light=None,
    )

    print("~" * 25 + " (" + str(i + 1) + ") " + "~" * 25)
    print("Generating QR code to the link - " + '"' + list_of_links[i] + '"')
    print("QR code version and error correction level: ", qr.designator)
    print()

# (46, 55, 65, 255)
# (112, 113, 103, 255)
# (23, 54, 93) word blue
