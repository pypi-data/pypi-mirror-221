"""
Test AV
"""
from __future__ import print_function

import datetime
import time
import vcr
from PIL import Image

import webuntis.utils.remote
from compress import best_compress, decodebytes, bits

webuntis.utils.remote._request_getid = lambda: "4711"

testnr = 2

if testnr == 0:
    with vcr.use_cassette("vcr/test_avhag.yml"):
        start = time.time()
        import createPicture
        import untis

        img = createPicture.create_picture_av("HAG")
        end = time.time()
        print("time: ", end - start)
        img.show()

        untis.s.logout()

if testnr == 1:
    with vcr.use_cassette("vcr/test_5ax.yml"):
        start = time.time()
        import createPicture
        import untis

        img = createPicture.createPictureKlassenraum("5AX")
        end = time.time()
        print("time: ", end - start)
        img.show()

        untis.s.logout()


def img2bitstr(img):
    img = img.convert('L')  # convert image to monochrome
    img = img.convert('1')  # convert image to black and white

    breite = 384
    hoehe = 640
    pixel_list = ""
    for b in range(breite - 1, -1, -1):
        for h in range(0, hoehe):
            p = img.getpixel((b, h))
            if not p:
                # print(p)
                pixel = '1'
            else:
                pixel = '0'
            # print(pixel)
            pixel_list += pixel
    return pixel_list


def encode(bs):
    res = ""
    lastbit = bs[0]
    count = 1
    for bit in bs[1:]:
        if (bit == lastbit) and (count < 26):
            count += 1
        else:
            if lastbit == '1':
                c = ord('A') - 1 + count
            else:
                c = ord('a') - 1 + count
            res += chr(c)

            lastbit = bit
            count = 1
    return res


def encode2(txt):
    lastch = txt[0]
    res = lastch
    count = 0
    for ch in txt[1:]:
        if (ch == lastch) and (count < 9):
            count += 1
        else:
            if count > 0:
                res += chr(ord('0') + count)
            res += ch
            lastch = ch
            count = 0
    return res


def image2str(img):
    bs = img2bitstr(img)
    print("bit string len:", len(bs))
    re = encode(bs)
    print("re string len:", len(re))
    re2 = encode2(re)
    print("re2 string len:", len(re2))
    print(bs)
    print(re)
    print(re2)

if testnr == 2:
        #with vcr.use_cassette("vcr/test_074.yml"):
        start = time.time()
        import lehrerzimmer
        import untis

        DELTA = 0
        #DELTA = +5
        #DELTA += (38) * 60
        ##DELTA -= (34) * 60
        # chk, img = lehrerzimmer.create_picture_room("060", datetime.datetime.now() + datetime.timedelta(minutes=DELTA))
        chk, img = lehrerzimmer.create_picture_room("074", datetime.datetime.now() + datetime.timedelta(minutes=DELTA))
        # chk, img = lehrerzimmer.create_picture_room("253", datetime.datetime.now() + datetime.timedelta(minutes=DELTA))
        # chk, img = lehrerzimmer.create_picture_room("353", datetime.datetime.now() + datetime.timedelta(minutes=DELTA))
        end = time.time()

        untis.s.logout()
        print("next check:", chk)
        print("time: ", end - start)

        with open("img.txt", "w") as f:
            print(img2bitstr(img), file=f)
        #img = img.rotate(90,expand=1).resize((640, 384))
        img.show()
        img.save("img.png")
        img.save("img.jpg")
        img.save("img.bmp")

        """
        bytes_ = img.tobytes()

        print("bytes: ", len(bytes_))

        compr = best_compress(bytes_)
        print("compr:", len(compr))
        print("   ", repr(compr[:50]))

        dc = decodebytes(compr)
        decompr = b''.join(chr(x) for x in dc)
        print(len(decompr))

        print("bytes  ", [x for x in bytes_ if x and x != chr(0xff)])
        print("decompr", [x for x in decompr if x and x != chr(0xff)])

        img2 = Image.frombytes("1", img.size, decompr)
        img2.show()
        """

if testnr == 3:
    with vcr.use_cassette("vcr/test_074_fw.yml"):
        import lehrerzimmer
        import untis

        times = (
            (8, 0), (8, 50), (9, 55), (10, 45), (11, 35), (12, 35), (13, 25), (14, 15), (15, 15), (16, 5), (16, 55))

        room = "074"
        for d in range(1, 14):
            for h, m in times:
                when = datetime.datetime(2018, 10, d, h, m)
                img = lehrerzimmer.create_picture_room(room, when + datetime.timedelta(minutes=1))
                n = "img/" + room + str(when) + ".png"
                img.save(n)
                print(n, "saved")
