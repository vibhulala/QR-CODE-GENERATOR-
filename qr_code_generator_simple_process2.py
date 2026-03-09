from PIL import Image
import qrcode
qr=qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,)
data ="https://rkgit.edu.in/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="yellow")
img.save("RKGIT_WEBSITE_LOGO.png")