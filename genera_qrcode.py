import qrcode
from PIL import Image, ImageDraw


url = "https://mediterranea-olives.it/"

# Genera il QR code
qr = qrcode.QRCode(
    version=1,  # Controlla la dimensione del QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # Controlla la dimensione di ogni box nel QR code
    border=4,  # Controlla la dimensione del bordo
)
qr.add_data(url)
qr.make(fit=True)

# Crea un'immagine del QR code
img_qr = qr.make_image(fill="black", back_color="white").convert('RGBA')

# Carica il logo
logo = Image.open("logo.png").convert('RGBA')

# Calcola la dimensione del logo
box_size = 10
border_size = 4
qr_size = (qr.modules_count + border_size * 2) * box_size

# Riduce ulteriormente la dimensione del logo per migliorarne la qualità
logo_size = qr_size // 4 
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Crea un'immagine bianca per lo sfondo del logo
background = Image.new('RGBA', (logo_size, logo_size), (255, 255, 255, 255))
draw = ImageDraw.Draw(background)
draw.ellipse([(0, 0), (logo_size, logo_size)], fill=(255, 255, 255, 255)) 
# Incolla il logo sul cerchio bianco
background.paste(logo, (0, 0), logo)  

# Ottiene le dimensioni del QR code
qr_width, qr_height = img_qr.size

# Calcola la posizione per il cerchio bianco
logo_pos = (
    (qr_width - logo_size) // 2,
    (qr_height - logo_size) // 2,
)

# Sovrapponi il cerchio bianco con il logo al QR code
img_qr.paste(background, logo_pos, background)

# Salva l'immagine del QR code con logo
img_qr.save("qrcode_with_logo.png", quality=100)

print("QR code con logo generato e salvato come qrcode_with_logo.png")


