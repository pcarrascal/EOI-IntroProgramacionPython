from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

fechacastellano=datetime.now()

print(fechacastellano)
print("fechacastellano:",fechacastellano.strftime("%A %d %b %Y"))
