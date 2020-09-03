# Importar arquivos
from app_functions import PDFfunctions
from ui_functions import UIFunctions
from ui_main import Ui_MainWindow

# Bibliotecas externas
import winsound

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Classes
class Worker(QThread):

    def __init__(self,parent=None):
        super(Worker,self).__init__(parent)
        self.ui = Ui_MainWindow()

    ## ==> BUTTONS FUNCTIONS

    def run(self):
        # Executar uma função da classe PDFFunctions
        # MULTITHREADING

        if self.sender().objectName() == 'pushButton_run_ocr':
            functionValue = PDFfunctions.ocrPDF(self,PDFfunctions.inputPdfPaths_ocr,self.ui.lineEdit_outputPath_ocr.text(),self.ui.lineEdit_filename_ocr.text(),self.ui.lineEdit_intDpi_ocr.text())

        elif self.sender().objectName() == 'pushButton_run_merge':
            functionValue = PDFfunctions.merge(self,PDFfunctions.inputPdfPaths_merge,self.ui.lineEdit_outputPath_merge.text(),self.ui.lineEdit_filename_merge.text())

        elif self.sender().objectName() == 'pushButton_run_extract':
            functionValue = PDFfunctions.extract(self,PDFfunctions.inputPdfPaths_extract,self.ui.lineEdit_intPages_extract.text(),self.ui.lineEdit_outputPath_extract.text(),self.ui.lineEdit_filename_extract.text())

        elif self.sender().objectName() == 'pushButton_run_zip':
            functionValue = PDFfunctions.zipCompress(self,self.ui.lineEdit_rootDirectory_zip.text(),self.ui.lineEdit_outputPath_zip.text(),self.ui.lineEdit_filename_zip.text())

        elif self.sender().objectName() == 'pushButton_addTable_search':
            PDFfunctions.csvPaths = QFileDialog.getOpenFileNames(self, 'Selecionar arquivo csv', QtCore.QDir.currentPath(), 'csv files (*.csv)',options=QFileDialog.DontUseNativeDialog)[0]
            functionValue = PDFfunctions.importFromCSV(self)
        
        else:
            functionValue = PDFfunctions.searchPattern(self,PDFfunctions.inputPdfPaths_search,self.ui.lineEdit_outputPath_search.text(),self.ui.lineEdit_filename_search.text())

        if functionValue:
            winsound.PlaySound('alert.wav',winsound.SND_FILENAME)
            
        return