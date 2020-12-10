from segno import helpers


my_vCard = helpers.make_vcard(
    name='Kuralbayev;Bekbolat',
    displayname='"Bekbolat Kuralbayev',
    email="example@example.com",
    phone="+7 123 444 5566",
)

my_vCard.save(
    "my_vCard_qr.svg",
    scale=6,
    border=0,
    dark="white",
    light=None,
    xmldecl=False,
    nl=False,
    svgns=False,
    svgclass=False,
)
