from segno import helpers


UDU_vCard = helpers.make_vcard(
    name='Scientific-Educational Journal;"Uly Dala Ustazy"',
    displayname='"Uly Dala Ustazy" Scientific-Educational Journal',
    email="dala.ustazy@gmail.com",
    phone="+7 747 555 9060",
)

UDU_vCard.save(
    "UDU_vCard_qr.svg",
    scale=6,
    border=0,
    dark="white",
    light=None,
    xmldecl=False,
    nl=False,
    svgns=False,
    svgclass=False,
)

print(UDU_vCard.designator)
