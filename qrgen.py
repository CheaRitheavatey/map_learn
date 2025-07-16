import qrcode
import qrcode.constants
# video url
video = "https://www.canva.com/design/DAGtTkX7508/aszzDbtzHvr10J-7QVC-8g/watch"

# genrate qr code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)


qr.add_data(video)
qr.make(fit=True)

# make img qrcode
img = qr.make_image().save("video_qr.png")
print("QR code saved as video_qr.png")