#!/usr/bin/python3

import sys
import numpy as np
import numpysane as nps



# sys.path[:0] = '/home/dima/projects/gnuplotlib',
# import gnuplotlib as gp
# import time


# x = np.arange(100)

# gp.plot(x*x, ascii=True, notest=False, log=False, wait=True)
# # time.sleep(3)
# # gp.plot(np.sin(x/10), ascii=True, notest=True)
# # time.sleep(3)
# sys.exit()










from fltk import *
from Fl_gnuplotlib import *



window = Fl_Window(800, 600, "plot")
plot   = Fl_Gnuplotlib_Window(0, 0, 800,600)




i = 0
xy = np.array(((1,2),(4,3)))

def tick(*args):
    global i,xy

    xy = nps.glue(xy,
                  np.array((i, np.cos(i/10.)),),
                  axis = -2)
    print("calling plot...")
    plot.plot(xy + np.array((0., i)), tuplesize = -2)
    print("...done calling plot")

    print(f"xid: 0x{fl_xid(plot):x}")
    Fl.repeat_timeout(1, lambda *args: print(f"xid: 0x{fl_xid(plot):x}"))


    i += 1.
    # Fl.repeat_timeout(.5, tick)


window.resizable(window)
window.end()
window.show()

if 1:
    tick()
else:
    Fl.repeat_timeout(.5, tick)

Fl.run()
