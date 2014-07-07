images2gif-example
==================

Pequeño ejemplo del uso de la libreria image2gif creado por Almar Klein, Ant1 y Marius van Voorden
# 2014-07-07: modified by frankzhao66
# 	modified images2gif.py 
	at		line426	:	palettes.append( getheader(im)[1] ) 
	with  	line 427:	palettes.append(im.palette.getdata()[1])
	modified main.py
	at		line11	:	for im in images:
    		line12	:		im.thumbnail(size, Image.ANTIALIAS)
    with	line11	:	for key in range(len(images)):
   			line 12	:		images[key]=images[key].resize(size)
# thanks for the former builder of this work!!! and now it could run normally.
	