from struct import pack, unpack ,calcsize
from math import sqrt
import urllib
from urllib import parse
from urllib.parse import unquote

form = 'bbbbb'

file = open('abcd', mode='wb')

data = (1, 25, 3, 4, 7, )
data = pack(form, *data)
file.write(data)

file.close()




file = open('abcd', mode='rb')

data = file.read(calcsize(form))
data = unpack(form, data)

file.close()

print(*data)




def write_to_ppm(file, r, g, b):
    data = pack("BBB", r, g, b)
    file.write(data)

"""

file = open("abcd.ppm", "wb")

file.write(b"P6\n1000 1000\n255\n")

for j in range(1000):
    for i in range(1000):
        r = sqrt(((i-500)**2 + (j-500)**2))
        r = int(r*255/(500*sqrt(2)+1))
        write_to_ppm(file, r, r, 0)

file.close()

"""



a = urllib.parse.parse_qs("client=ubuntu&hs=8Pl&channel=fs&sxsrf=ALeKk02KCIiNyAoMt6vuhNeewR86xrti0w%3A1597522736581&ei=MEM4X9-HI83w-QbSgJHwDA&q=example.comとは&oq=example.comとは&gs_lcp=CgZwc3ktYWIQAzICCAAyBggAEAcQHjIGCAAQBxAeMgYIABAHEB46BwgAEEcQsANQg4YBWIOGAWD0iAFoAXAAeACAAVqIAVqSAQExmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwjf3-_5g57rAhVNeN4KHVJABM4Q4dUDCAs&uact=5")
print(a)
