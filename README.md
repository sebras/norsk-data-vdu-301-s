This repository is meant to analyze the ROM images from Norsk Data VDU 301 S
as [provided at by Torfinn](http://heim.bitraf.no/tingo/nokiad/nokia-vdu-301s.html).

To combine the two ROM image halves and extract the font portion of it:

> python3 extract-nd.py

You should get a `rom-nd-vdu-301-s.bin` with the complete ROM image and a
`font-nd-vdu-301-s.bin` that contains the font part of the ROM and finally
a `font-nd-vdu-301-s.ppm` that is a [Netpbm image](http://netpbm.sourceforge.net/)
showing each character of the font.

There are 770 black/white characters in `font-nd-vdu-301-s.bin`
concatenated without intervening padding. Each character is 8 pixels wide
and 15 rows tall, i.e. one row of pixels per byte for a total of 15 bytes.
A bit set to `1` should be interpreted as black color while a bit cleared
to `0` should be interpreted as white color.

You should get a `rom.bin` with the complete ROM image and a `font.bin`
that contains the font part of the ROM and finally a `font.ppm` that is
a [Netpbm image](http://netpbm.sourceforge.net/) showing each character
of the font.

This is the output to expect, albeit converted to PNG:

![Image of font for Norsk Data VDU 301 S](https://github.com/sebras/norsk-data-vdu-301-s/blob/master/font-nd-vdu-301-s.png)

The liberty was also taken to include the analysis of the Tandberg TDV 2200/9 S t
ROM image also [provided by Torfinn](http://heim.bitraf.no/tingo/td/tandberg-tdv-2200-9s.html).

The font can similarly be extracted like so:

> python3 extract-tdv.py

You should get a `font-tdv-2200-9-s.ppm` based on the original ROM image
which contains 1024 character concatenated without intervening padding.
Each character is 8 pixels wide and 16 rows tall, for a total of 16 bytes.
Like for ND VDU 301 S above, a bit set to `1` should be interpreted as
black color while a bit cleared to `0` should be interpreted as white
color.

This is the output to expect for TDV 2200/9 S, albeit converted to PNG:

![Image of font for Tandberg TDV 2200/9 S](https://github.com/sebras/norsk-data-vdu-301-s/blob/master/font-tdv-2200-9-s.png)
