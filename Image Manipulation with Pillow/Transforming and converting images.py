from PIL import Image
import os

# Menggunakan ukuran
size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir("."):
    # File yang akan disimpan berbntuk png
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        # Menyimpan file di folder 300
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))

        # Untuk menyimpan file gambar ke dalam folder png
        # i.save('png/{}.png'.format(fn))

# image1 = Image.open("Bridge.jpg")
# image1.save('Bridge.jpg')
