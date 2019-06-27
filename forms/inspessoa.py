import sys
import json
from datetime import datetime
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from PySide2.QtCore import QFile, QObject
from model.estado import Estado
from model.pessoa import Pessoa
from controller.pessoacontroller import PessoaController
from controller.estadocontroller import EstadoController


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        self.window.setFixedSize(self.window.width(), self.window.height());
        ui_file.close()

        self.txtcpf = self.window.findChild(QLineEdit, 'txtCpf')
        self.txtcpf.textChanged.connect(self.cpf_handler)
        self.txtcpfmsg = self.window.findChild(QLabel, 'lblCpfMsg')

        self.txtnome = self.window.findChild(QLineEdit, 'txtNome')
        self.txtnome.textChanged.connect(self.nome_handler)
        self.txtnomemsg = self.window.findChild(QLabel, 'lblNomeMsg')

        self.txtendereco = self.window.findChild(QLineEdit, 'txtEndereco')
        self.txtendereco.textChanged.connect(self.endereco_handler)
        self.txtenderecomsg = self.window.findChild(QLabel, 'lblEnderecoMsg')

        self.txtcomplemento = self.window.findChild(QLineEdit, 'txtComplemento')
        self.txtcomplemento.textChanged.connect(self.complemento_handler)
        self.txtcomplementomsg = self.window.findChild(QLabel, 'lblComplementoMsg')

        self.txtcidade = self.window.findChild(QLineEdit, 'txtCidade')
        self.txtcidade.textChanged.connect(self.cidade_handler)
        self.txtcidademsg = self.window.findChild(QLabel, 'lblCidadeMsg')

        self.txtbairro = self.window.findChild(QLineEdit, 'txtBairro')
        self.txtbairro.textChanged.connect(self.bairro_handler)
        self.txtbairromsg = self.window.findChild(QLabel, 'lblBairroMsg')

        self.cmbestado = self.window.findChild(QComboBox, 'cmbEstado')
        self.cmbestado.currentIndexChanged.connect(self.cmbestado_handler)
        self.txtestadomsg = self.window.findChild(QLabel, 'lblEstadoMsg')

        self.txtestadonome = self.window.findChild(QLineEdit, 'txtEstadoNome')

        self.txtcep = self.window.findChild(QLineEdit, 'txtCep')
        self.txtcep.textChanged.connect(self.cep_handler)
        self.txtcepmsg = self.window.findChild(QLabel, 'lblCepMsg')

        self.btnsalvar = self.window.findChild(QPushButton, 'btnSalvar')
        self.btnsalvar.clicked.connect(self.salvar_handler)

        self.btncancelar = self.window.findChild(QPushButton, 'btnCancelar')
        self.btncancelar.clicked.connect(self.cancelar_handler)

        self.setMessageInvisible()

        ec = EstadoController()
        json_data = ec.getEstados()
        json_list = json.loads(json_data)
        for sigla in json_list:
            nome = json_list[sigla]
            estado = Estado(sigla, nome)
            self.cmbestado.addItem(estado.descricao, userData=estado)
        self.window.show()
        return

    def cpf_handler(self):
        self.txtcpfmsg.setText("")
        self.txtcpfmsg.setVisible(0)
        return

    def nome_handler(self):
        self.txtnomemsg.setText("")
        self.txtnomemsg.setVisible(0)
        return

    def endereco_handler(self):
        self.txtenderecomsg.setText("")
        self.txtenderecomsg.setVisible(0)
        return

    def complemento_handler(self):
        self.txtcomplementomsg.setText("")
        self.txtcomplementomsg.setVisible(0)
        return

    def cidade_handler(self):
        self.txtcidademsg.setText("")
        self.txtcidademsg.setVisible(0)
        return

    def bairro_handler(self):
        self.txtbairromsg.setText("")
        self.txtbairromsg.setVisible(0)
        return

    def cmbestado_handler(self):
        estado = self.cmbestado.itemData(self.cmbestado.currentIndex())
        self.txtestadonome.setText(estado.nome)
        self.txtestadomsg.setVisible(0)
        return

    def cep_handler(self):
        self.txtcepmsg.setText("")
        self.txtcepmsg.setVisible(0)
        return

    def salvar_handler(self):
        self.setMessageInvisible()
        if "..-" in self.txtcpf.text():
            self.txtcpfmsg.setText("CPF inválido!")
            self.txtcpfmsg.setVisible(1)

        if len(self.txtcpf.text()) < 14:
            self.txtcpfmsg.setText("CPF inválido!")
            self.txtcpfmsg.setVisible(1)

        if len(self.txtnome.text()) == 0:
            self.txtnomemsg.setText("Nome é campo obrigatório!")
            self.txtnomemsg.setVisible(1)

        if len(self.txtendereco.text()) == 0:
            self.txtenderecomsg.setText("Endereço é campo obrigatório!")
            self.txtenderecomsg.setVisible(1)

        if len(self.txtcidade.text()) == 0:
            self.txtcidademsg.setText("Cidade é campo obrigatório!")
            self.txtcidademsg.setVisible(1)

        if len(self.txtbairro.text()) == 0:
            self.txtbairromsg.setText("Bairro é campo obrigatório!")
            self.txtbairromsg.setVisible(1)

        estado = self.cmbestado.itemData(self.cmbestado.currentIndex())
        if "<Selecione>" in estado.sigla:
            self.txtestadomsg.setText("Selecione um estado!")
            self.txtestadomsg.setVisible(1)

        if ".-" in self.txtcep.text():
            self.txtcepmsg.setText("CEP inválido!")
            self.txtcepmsg.setVisible(1)

        if len(self.txtcep.text()) < 10:
            self.txtcepmsg.setText("CEP inválido!")
            self.txtcepmsg.setVisible(1)

        if self.txtcpfmsg.isVisible():
            self.txtcpf.setFocus()
            return
        elif self.txtnomemsg.isVisible():
            self.txtnome.setFocus()
            return
        elif self.txtenderecomsg.isVisible():
            self.txtendereco.setFocus()
            return
        elif self.txtcomplementomsg.isVisible():
            self.txtcomplemento.setFocus()
            return
        elif self.txtcidademsg.isVisible():
            self.txtcidade.setFocus()
            return
        elif self.txtbairromsg.isVisible():
            self.txtbairro.setFocus()
            return
        elif self.txtestadomsg.isVisible():
            self.cmbestado.setFocus()
            return
        elif self.txtcepmsg.isVisible():
            self.txtcep.setFocus()
            return

        resp = self.showMsg("Atualização", "Deseja salvar suas alterações?")

        if resp == QMessageBox.Yes:
            if self.salvar() == 0:
                self.clear()
        return

    def setMessageInvisible(self):
        self.txtcpfmsg.setVisible(0)
        self.txtnomemsg.setVisible(0)
        self.txtenderecomsg.setVisible(0)
        self.txtcomplementomsg.setVisible(0)
        self.txtcidademsg.setVisible(0)
        self.txtbairromsg.setVisible(0)
        self.txtestadomsg.setVisible(0)
        self.txtcepmsg.setVisible(0)

    def clear(self):
        self.txtcpf.setText("")
        self.txtnome.setText("")
        self.txtendereco.setText("")
        self.txtcomplemento.setText("")
        self.txtcidade.setText("")
        self.txtbairro.setText("")
        self.cmbestado.setCurrentIndex(0)
        self.txtestadonome.setText("")
        self.txtcep.setText("")
        self.txtcpf.setFocus()
        self.txtcpf.setCursorPosition(0)

    def cancelar_handler(self):
        sys.exit(0)

    def showMsg(self, title, msg):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setInformativeText(msg)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Yes)
        ret = msgBox.exec_()
        return ret


def salvar(self):
    estado = self.cmbestado.itemData(self.cmbestado.currentIndex())
    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    p = Pessoa()
    p.id = "0"
    p.cpf = self.txtcpf.text()
    p.nome = self.txtnome.text()
    p.endereco = self.txtendereco.text()
    p.complemento = self.txtcomplemento.text()
    p.cidade = self.txtcidade.text()
    p.bairro = self.txtbairro.text()
    p.estado = estado.sigla
    p.cep = self.txtcep.text()
    p.dtainc = today
    pc = PessoaController()
    return pc.insert(p)
