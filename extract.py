#!/usr/bin/python3


def combine(inputs):

    if len(inputs) == 0:
        return []

    rom = []
    i = 0

    while (byte := inputs[i].read(1)):
        rom.append(byte)

        i = i + 1
        if i >= len(inputs):
            i = 0

    return rom


print('Combine upper and lower ROM image halves.')
with open('9698H.bin', 'rb') as input0:
    with open('9697H.bin', 'rb') as input1:
        rom = combine([input0, input1])


print('Output complete ROM image.')
with open('rom.bin', 'wb') as output:
    for i in range(len(rom)):
        output.write(rom[i])

print('Extract font binary.')
offset = 0xf5e7
chars = 770
bytesperchar = 15

start = offset
end = offset + chars * bytesperchar
font = rom[start:end]

print('Output font binary.')
with open('font.bin', 'wb') as output:
    for i in range(len(font)):
        output.write(font[i])

print('Blit each character in font into an image.')
charwidth = 8
charheight = 15
padding = 2
charsperline = 16
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

    for i in range(len(chardata)):
        chardata[i] = int.from_bytes(chardata[i], 'big')

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
with open('font.ppm', 'w') as output:
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
