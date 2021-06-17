---
title: "Playing Music on Raspberry Pi Pico"
slug: "playing music on raspberry pi pico"
date: 2021-02-19T20:00:00-05:00
draft: false
publishdate: 2021-02-19T20:00:00-05:00
tags:
- raspberry pi
- electronics
- hobbies
---

I purchased a few of the new Raspberry Pi Pico’s from [Adafruit][1] recently. I’ve been playing with [MicroPython][2], and [CircuitPython][3]. I ran across a nice tutorial at [Tom’s Hardware][4] that walked through simple music output using the Pico with a passive buzzer. I liked the idea so I modified the code to also take a list of note durations. This makes the “music” a little closer to the original.

```
from machine import Pin, PWM
from utime import sleep

rled = Pin(15, Pin.OUT) # GP20
yled = Pin(13, Pin.OUT) # GP17
gled = Pin(12, Pin.OUT) # GP16

buzzer = PWM(Pin(9)) # GP12
base_time = 0.26

duration = {
"16": base_time * 0.25,
"8": base_time * 0.5,
"Q": base_time,
"H": base_time * 2,
"F": base_time * 4,
}

tones = {
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
}

aom_not = ["A5","B5","B5","B5","B5","B5","B5","G5",
             "G5","A5","B5","B5","B5","A5","B5","B5",
             "A5","G5","G5","E5","E5","B5","B5","C6",
             "B5","G5","C6","B5","G5","G5","A5","B5",
             "A5","E5","B5","B5","B5","B5","A5","B5",
             "B5","A5","G5","C6","E6","C6","FS6","C6",
             "B5","C6","C6","C6","B5","B5","B5","A5",
             "B5"]
aom_dur = ["8","8","Q","8","8","Q","Q","Q",
              "H","8","8","Q","8","8","Q","16",
              "16","16","16","Q","Q","Q","Q","H",
              "Q","Q","H","Q","8","8","H","Q",
              "Q","H","8","8","Q","8","8","Q",
              "8","8","Q","8","H","8","H","H",
              "H","8","H","8","Q","Q","8","8",
              "8"]
    
def playtone(frequency,duration):
    if duration < base_time:
        gled.value(1)
    elif duration > base_time:
        rled.value(1)
    else:
        yled.value(1)
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
    sleep(duration)
    buzzer.duty_u16(500)
    gled.value(0)
    rled.value(0)
    yled.value(0)
    
def rest(duration):
    buzzer.duty_u16(0)
    sleep(duration)

def playsong(mysong,mydur):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            rest(duration[mydur[i]])
        else:
            playtone(tones[mysong[i]],duration[mydur[i]])
        sleep(.3)
    rest(1)

playsong(aom_not,aom_dur)
```

{{< rawhtml >}}

<video width=100% controls>
<source src="/mov/pico-music-box.mov">
Your browser does not support the video tag. </video>

{{< /rawhtml >}}

[1]: https://www.adafruit.com/product/4864
[2]: https://www.micropython.org
[3]: https://www.circuitpython.org
[4]: https://www.tomshardware.com/how-to/buzzer-music-raspberry-pi-pico
