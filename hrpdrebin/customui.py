try:
    from PyQt5 import QtWidgets
except:
    from PySide import QtWidgets


class DropListView(QtWidgets.QListView):
    """ """

    def dragEnterEvent(self, event):
        m = event.mimeData()
        print("drag started")
        if m.hasUrls():
            print("drag accepted")
            event.acceptProposedAction()

    def dropEvent(self, event):
        m = event.mimeData()
        print("drop started")
        if m.hasUrls():
            print("drop accepted")
            event.acceptProposedAction()
            files = [u.toLocalFile() for u in m.urls()]
            print(files)


#             self.g
#         print(data)
