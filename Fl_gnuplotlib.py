#!/usr/bin/python3

import sys
import fltk

sys.path[:0] = '/home/dima/projects/gnuplotlib',
import gnuplotlib as gp


class Fl_Gnuplotlib_Window(fltk.Fl_Window):

    def __init__(self, x,y,w,h, **plot_options):
        super().__init__(x,y,w,h)
        self.end()

        self._gp                   = None
        self._delayed_plot_options = None

        self.init_plot(**plot_options)

    def init_plot(self, **plot_options):
        print("{{{ init_plot()")

        if 'terminal' in plot_options:
            raise Exception("Fl_Gnuplotlib_Window needs control of the terminal, but the user asked for a specific 'terminal'")

        if self._gp is not None:
            self._gp = None

        self._delayed_plot_options = None

        xid = fltk.fl_xid(self)
        if xid == 0:
            # I don't have an xid (yet?), so I delay the init
            self._delayed_plot_options = plot_options
            print("}}} init_plot() no xid yet")
            return

        print(f"xid: 0x{xid:x}")

        # will barf if we already have a terminal
        gp.add_plot_option(plot_options,
                           terminal = f'x11 window "0x{xid:x}" title "xxx"',
                           ascii    = 0,
                           log      = 0,
                           notest   = 0)

        self._gp = gp.gnuplotlib(**plot_options)
        print("}}} init_plot() success")

    def plot(self, *args, **kwargs):

        print("{{{ plot()")
        if self._gp is None:
            if self._delayed_plot_options is None:
                raise Exception("plot has not been initialized")

            print("{{{ init_plot() calling")
            self.init_plot(**self._delayed_plot_options)
            print("}}} init_plot() done")
            if self._gp is None:
                raise Exception("plot has not been initialized. Delayed initialization failed")

        print("{{{ gp.plot()")
        self._gp.plot(*args, **kwargs)
        print("}}} gp.plot()")
        print("}}} plot() success")

    def handle(self, event):
        # print(f"event {event} is FL_SHOW: {event==fltk.FL_SHOW}; xid: {fltk.fl_xid(self)}")
        # Try to execute the delayed init

        # if event == fltk.FL_SHOW and \
        #    fltk.fl_xid(self) != 0 and \
        #    self._gp is None and \
        #    self._delayed_plot_options is not None:

        #     print("trying delayed init")
        #     self.init_plot(**self._delayed_plot_options)
        #     if self._gp is None:
        #         raise Exception("Delayed initialization failed")

        return super().handle(event)

