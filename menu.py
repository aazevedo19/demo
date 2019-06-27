import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QObject
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget
from forms.inspessoa import FormPessoa


class Form(QWidget):

    def __init__(self, ui_file):
        super(Form, self).__init__()
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        self.window.setFixedSize(self.window.width(), self.window.height());
        ui_file.close()

        self.tree = self.window.findChild(QTreeWidget, 'treeMenu')
        #        self.tree.itemSelectionChanged.connect(self.itemSelection)
        self.tree.currentItemChanged.connect(self.itemSelection)
        self.tree.itemClicked.connect(self.itemSelection)
        menulist = ["Cadastro de Pessoa"]
        itemlist = ["Inserir", "Atualizar", "Excluir", "Listar"]
        for str in menulist:
            parent = QTreeWidgetItem(self.tree)
            parent.setText(0, str)
            for opcao in itemlist:
                child = QTreeWidgetItem(parent)
                child.setText(0, opcao)
            parent.setExpanded(1)
        self.window.show()
        return

    def itemSelection(self):
        node = self.tree.currentItem()
        print("select " + node.text(0))
        if node.text(0) in "Inserir":
            self.form = FormPessoa('ui/pessoa.ui')
