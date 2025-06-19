#Plugin Desarrollado por Gabo99x y MartinMigue
from krita import *
from PyQt5.QtWidgets import QWidget, QPushButton, QColorDialog, QVBoxLayout
import random

class GeneradorPaleta(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.window = None

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("GeneradorPaleta","Generar Paleta de Colores","tools/scripts")
        action.triggered.connect(self.elegirColor)

    def elegirColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.generarPaleta(color)

    def generarPaleta(self, base_color):
        r=base_color.red() 
        g=base_color.green()
        b=base_color.blue()
        r=int(r)
        g=int(g)
        b=int(b)
        paleta = []

        for i in range(5):  # Generar 5 colores basados en el color base
            r1 = max(0, min(255, r + random.randint(-30, 30)))  
            g1 = max(0, min(255, g + random.randint(-30, 30)))  
            b1 = max(0, min(255, b + random.randint(-30, 30))) 
            colorNuevo = (r1,g1,b1)
            paleta.append(colorNuevo)
        self.mostrarPaleta(paleta)

    def mostrarPaleta(self, paleta):
        if self.window is not None:
            self.window.close()
        self.window = QWidget()
        layout = QVBoxLayout()

        for colorTupla in paleta:
            label = QLabel()
            pixmap = QPixmap(50, 50)
            color = QColor(colorTupla[0], colorTupla[1], colorTupla[2])
            pixmap.fill(color)
            label.setPixmap(pixmap)
            textoRGB = f"RGB: ({colorTupla[0]}, {colorTupla[1]}, {colorTupla[2]})"
            label1 = QLabel(textoRGB)
            layout.addWidget(label)
            layout.addWidget(label1)
            
        self.window.setLayout(layout)
        self.window.setWindowTitle("Paleta Generada")
        self.window.show()

Krita.instance().addExtension(GeneradorPaleta(Krita.instance()))
