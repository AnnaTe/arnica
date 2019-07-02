import sys

from PyQt5 import QtWidgets, QtCore

from gui.app import DesignerMainWindow

# create the GUI application
app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
# Enable High DPI display with PyQt5
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
if hasattr(QtWidgets.QStyleFactory, 'AA_UseHighDpiPixmaps'):
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())

