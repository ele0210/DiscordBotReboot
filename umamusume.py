from enum import Enum

class List(Enum):
    SUPE = 0
    SUZU = 1
    TEIO = 2
    MARU = 3
    OGURI = 4
    GOLD = 5
    VODKA = 6
    DASUKA = 7
    TAIKI = 8
    GLASS = 9
    MEJIRO = 10
    EL = 11
    TEIEMU = 12
    NARITA = 13
    RUDORU = 14
    EAG = 15
    BIWA = 16
    MAYANO = 17
    MIHONO = 18
    RAIAN = 19
    RICE = 20
    TAKION = 21
    CICKET = 22
    KAREN = 23
    BAKUSHIN = 24
    CREEK = 25
    FALCON = 26
    TAISHIN = 27
    URARA = 28
    MACHIKANE = 29
    NEICHA = 30
    KING = 31
    HAPPY = 32
    TAZUNA = 33
    YAYOI = 34
    OTONASHI = 35
    AOI = 36

def get_link(number):
    uma = List(number)
    if uma == List.SUPE:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/e3defdd4ecdb445982532069e25c6037.png"
    elif uma == List.SUZU:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/23920df7cf851ff914746bbfb48277d0.png"
    elif uma == List.TEIO:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/4228d0adce624fa98fa3ad09133f8b6b.png"
    elif uma == List.MARU:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/da44e722139d2939eb9c57c91ec1aeca.png"
    elif uma == List.OGURI:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/a6a6680c5b06facea93d41e05da50681.png"
    elif uma == List.GOLD:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/370c5dc3724814fc868658b71b79222a.png"
    elif uma == List.VODKA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/ec4824add03cc49b95a8455ec4402222.png"
    elif uma == List.DASUKA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/13e0c8c4e105518701f8d67e9038d2ad.png"
    elif uma == List.TAIKI:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/4b9ea2498dec2834d5da2f6adbcf0e6f.png"
    elif uma == List.GLASS:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/5c75feb94bd931d345eecbc5a875e9bf.png"
    elif uma == List.MEJIRO:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/ef8b910d154ef75330153e2dd9f9bf13.png"
    elif uma == List.EL:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/84bdc74ecc33cb02ce07d154b54503df.png"
    elif uma == List.TEIEMU:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/12ed5ffb486236594f60376fef13c206.png"
    elif uma == List.NARITA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/53c3831aadf491f7ec0731580db2c09e.png"
    elif uma == List.RUDORU:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/9234278f50fb2960ca2c84dbe2778a12.png"
    elif uma == List.EAG:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/e90e471a6601afa497aef63c6a6eecc4.png"
    elif uma == List.BIWA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/820b5f2941ae7a45aa9fcb6d1aa13578.png"
    elif uma == List.MAYANO:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/1ae6a9ca4a7e04afbabdb76d3c278480.png"
    elif uma == List.MIHONO:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/e35535c4dae8ebcd2e1857ce7a276dab.png"
    elif uma == List.RAIAN:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/5287f085b3726331f61abffde5c2fc73.png"
    elif uma == List.RICE:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/0546e3d12c8c16426c7bb730c0afc5d9.png"
    elif uma == List.TAKION:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/00cbe4a345f30032ccb328a1fe65e13a.png"
    elif uma == List.CICKET:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/3b73b309ac9545be5b969a369e29d032.png"
    elif uma == List.KAREN:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/33c4ffa80081e3a941f77ecb880e00e3.png"
    elif uma == List.BAKUSHIN:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/25feec398177495f20fdd16676eabe29.png"
    elif uma == List.CREEK:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/accc166d82d3f80dc9d62516a3173654.png"
    elif uma == List.FALCON:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/8e95dc7421f823a1e19e4fff65601b09.png"
    elif uma == List.TAISHIN:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/8de584b09cf92f3d240a09f3b795af79.png"
    elif uma == List.URARA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/7a0480dc52ed454293412c3f8a98e48b.png"
    elif uma == List.MACHIKANE:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/69ef984fc360e7e160610bca256c2fca.png"
    elif uma == List.NEICHA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/337c969981e537f09aac61dd72bac8fe.png"
    elif uma == List.KING:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/e108fde5fad428ae80788bfbc0937b3b.png"
    elif uma == List.HAPPY:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/32e748f59774633f7c9170d6916a073a.png"
    elif uma == List.TAZUNA:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/3f9cd0d8d740aee93fa73b350292381d.png"
    elif uma == List.YAYOI:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/b32b9306d5f71c6b7cdd1b8a14ddedde.png"
    elif uma == List.OTONASHI:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/4012fd00b0ef31d988cd723c6d0cf3d1.png"
    elif uma == List.AOI:
        return "https://umamusume.jp/app/wp-content/uploads/2021/01/a87f07dea835cfe4eb2227639004a3a5.png"
    else:
        return "https://umamusume.jp/"
