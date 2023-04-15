import level_construct
import time

LEVEL = [{ # design of each level
    "level": 1,
     "i": 4,
     "j": 6,
     "a": 9000,
     "b": 27000,
     "title": 'week 1'
}, {
    "level": 2,
     "i": 2,
     "j": 6,
     "a": 9000,
     "b": 21000,
     "title": 'midterm'
}, {
    "level": 3,
     "i": 1,
     "j": 6,
     "a": 6000,
     "b": 12000,
     "title": 'endterm'
}
]

lv1 = level_construct.main(LEVEL[0]["i"], LEVEL[0]["j"], LEVEL[0]["a"],LEVEL[0]["b"],LEVEL[0]["title"])
time.sleep(3)
lv2 = level_construct.main(LEVEL[1]["i"], LEVEL[1]["j"], LEVEL[1]["a"],LEVEL[1]["b"],LEVEL[1]["title"])
time.sleep(3)
lv3 = level_construct.main(LEVEL[2]["i"], LEVEL[2]["j"], LEVEL[2]["a"],LEVEL[2]["b"],LEVEL[2]["title"])