import sys

from PyQt5 import QtWidgets

from gui.app import DesignerMainWindow


# create the GUI application
app = QtWidgets.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())

