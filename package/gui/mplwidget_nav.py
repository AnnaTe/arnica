#!/usr/bin/env python

# Python Qt5
from PyQt5 import QtGui, QtWidgets

# import the Qt5Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
# Matplotlib Figure object
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = Figure(dpi=300)
        self.ax = self.fig.add_subplot(111)
        self.ax.axis('off')
        self.fig.tight_layout()

        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        self.win = QtWidgets.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtWidgets.QVBoxLayout()
        #self.ntb = NavigationToolbar(self.canvas, parent)
        #self.ntb.move(235,48)
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        self.addToolBar(NavigationToolbar(self.canvas, self))
        #self.ntb.addWidget(self.win)

        # set the layout to the vertical box
        self.setLayout(self.vbl)
