import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel('opa')
label.show()

sys.exit(app.exec_())