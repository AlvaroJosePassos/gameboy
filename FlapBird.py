# PicoFlappyBird.py by Matthieu Mistler
# Flappy Bird game for the Raspberry Pi Pico Game Boy

from PicoGameBoy import PicoGameBoy
import time
from random import randint
import gc


def FlapBird_main ():
    gc.collect()
    
    pgb = PicoGameBoy()

    #Picture importation
    sprite1_34x24=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')
    pgb.add_sprite(sprite1_34x24,34,24) # sprite #0
    gc.collect()

    sprite2_34x24=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')
    pgb.add_sprite(sprite2_34x24,34,24) # sprite #1
    gc.collect()

    sprite3_34x24=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')
    pgb.add_sprite(sprite3_34x24,34,24) # sprite #2
    gc.collect()

    pipe_52x52=bytearray(b'v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9')
    pgb.add_sprite(pipe_52x52,52,52) # sprite #3
    gc.collect()
    
    floor_98x14=bytearray(b'Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I\xd5I')
    pgb.add_sprite(floor_98x14,98,14) # sprite #5
    gc.collect()


    # game loop
    while True:
        
        #game settings
        HOLE_SIZE = 130 # pixels
        SPEED = 3
        counter = 0
        sprite_condition = False
        gameover=False

        #sprite settings
        sprite = 0
        x = 50
        y = 50
        vy = 0.0

        #floor settings
        x_f=0
        Y_F=210

        BACKGROUND_COLOR = PicoGameBoy.color(112,197,206)
        FLOOR_COLOR = PicoGameBoy.color(219,218,150)
        
        button_pressed = False
        prev_button_pressed = False

        def print_pipe(x_p1, y_p1) :
            y = y_p1
            pgb.sprite(3, x_p1 ,y)
            
            
            while y>=-52:
                y = y - 52
                pgb.sprite(3, x_p1 ,y)
            
            y = y_p1 + HOLE_SIZE
            pgb.sprite(3, x_p1, y)
            
            while y<320:
                y = y + 52
                pgb.sprite(3, x_p1 ,y)
                
        def intersect(x1,y1,w1,h1,x2,y2,w2,h2):
            
            if x1+w1 < x2:
                return False
            if x2+w2 < x1:
                return False
            if y1+w1 < y2:
                return False
            if y2+w2 < y1:
                return False 
            else :
                return True
                
        #pipe 1 initialisation
        y_p1 = randint(-10,48)
        x_p1 = 320

        #pipe 2 initialisation
        y_p2 = randint(-10,48)
        x_p2 = 320 + 180


        #part_game loop
        while True:
                   
            # update the screen :
               
            #the background
            pgb.fill(BACKGROUND_COLOR)
            #the main sprite
            pgb.sprite(sprite, int(x), int(y))
            
            if sprite_condition == True :
                counter = counter + 1
                
                if sprite >= 2 :
                        sprite = 0
                        sprite_condition = False
                
                if counter == 3  :
                    sprite = sprite + 1
                    counter = 0
                        
            #pipe 1
            print_pipe(x_p1, y_p1)
            #pipe 2
            print_pipe(x_p2, y_p2)
            
            #floor
            for i in range(0,5):        
                pgb.sprite(4,x_f+i*98,Y_F)
                pgb.fill_rect(0,Y_F+14,320,240-Y_F-14,FLOOR_COLOR)

            pgb.show()
           
            vy = vy + 0.20
            y = y + vy
                 
            prev_button_pressed = button_pressed
            
            if pgb.button_A() or pgb.button_B():
                button_pressed = True
            else:
                button_pressed = False
                
            if prev_button_pressed==False and button_pressed==True:
                sprite_condition = True
                vy = -4.4
                
            #update the pipes position
            x_p1 = x_p1 - SPEED
            x_p2 = x_p2 - SPEED
            
            #generate pipe 1
            if x_p1 < -82 :                    
                y_p1 = randint(-20,80)
                x_p1 = 320
            
            #generate pipe 2
            if x_p2 < -82 :
                y_p2 = randint(-20,80)
                x_p2 = 320

                
            #update the floors positions
            x_f = x_f - SPEED
            if x_f<=-98:
                x_f=x_f+98    
         
            #Hit Box verification...
            
            if intersect(x,y,32,20,x_p1+1,y_p1-2,52,240):
                gameover=True
            if intersect(x,y,32,22,x_p1+1,y_p1 + HOLE_SIZE+12,52-3,0):
                gameover=True
            if intersect(x,y,32,20,x_p2+1,y_p2-4,52  ,240):
                gameover=True
            if intersect(x,y,32,22,x_p2+1,y_p2 + HOLE_SIZE+12,52-3,0):
                gameover=True
            if y > Y_F :
                gameover=True
            if gameover:
                break
            
        #Game over
        pgb.fill_rect(100,85,120,60,PicoGameBoy.color(0,0,0))
        pgb.text("GAME OVER",123,113,PicoGameBoy.color(255,255,255))        
        pgb.show()
        
        time.sleep(1)

        while not pgb.any_button():
            time.sleep(0.1)
    
        if pgb.button_down():
            break
        
    pgb.clear_ghost_array()
    return
                
