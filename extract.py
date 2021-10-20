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

