#!/usr/bin/python3

import sys

print('Read complete ROM image.')
filename = 'tdv2200s_U63_D27128A_965115_-1-.bin'
if len(sys.argv) > 1:
    filename = sys.argv[1].replace('\\', '/').split('/')[-1]
with open(filename, 'rb') as f:
    font = f.read()


print('Blit each character in font into an image.')
charwidth = 8
charheight = 16
padding = 2
charsperline = 16
chars = 1024
lines = int((chars + (charsperline - 1)) / charsperline)

width = padding + charsperline * (charwidth + padding)
height = padding + lines * (charheight + padding)

rgb = []
for y in range(height):
    for x in range(width):
        rgb.append(-1)

cy = padding
cx = padding

for char in range(chars):
    start = char * charheight
    end = start + charheight
    chardata = font[start:end]

    byte = 0
    bit = 7
    for y in range(charheight):
        for x in range(charwidth):
            v = (chardata[byte] >> bit) & 1
            bit = bit - 1
            if bit < 0:
                bit = 7
                byte = byte + 1

            dx = cx + x
            dy = cy + y

            offset = dy * width + dx
            rgb[offset] = v

    cx = cx + charwidth + padding
    if cx >= width:
        cx = padding
        cy = cy + charheight + padding


print('Output sample image with complete font.')
with open(f'font-{filename[:-4]}.ppm', 'w') as output:
    output.write('P3\n')
    output.write('%u %u\n255\n' % (width, height))

    for y in range(height):
        for x in range(width):
            if rgb[y * width + x] == 0:
                output.write('255 255 255 ')
            elif rgb[y * width + x] == 1:
                output.write('  0   0   0 ')
            else:
                output.write('127 127 127 ')
