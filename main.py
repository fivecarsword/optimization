import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from typing import Dict

from PolynomialFunc import PolynomialFunc

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x150")

        self.currentFrameKey = "경사하강법"

        self.frameDict : Dict[str, tk.Frame] = dict()

        # 경사하강법 frame 위젯 배치
        self.frameDict["경사하강법"] = tk.Frame(self.root, width=800, height=135)
        frame = self.frameDict["경사하강법"]

        startXLabel = tk.Label(frame, text="Start X : ", font = "Calibri 15")
        startXLabel.place(x=0, y=10, width=80, height=20)

        self.gradientDescentStartXEntry = tk.Entry(frame)
        self.gradientDescentStartXEntry.place(x=80, y=10, width=50, height=20)

        stepSizeLabel = tk.Label(frame, text="λ : ", font = "Calibri 15")
        stepSizeLabel.place(x=0, y=40, width=50, height=20)

        self.gradientDescentStepSizeEntry = tk.Entry(frame)
        self.gradientDescentStepSizeEntry.place(x=50, y=40, width=60, height=20)

        stepLabel = tk.Label(frame, text="step : ", font = "Calibri 13")
        stepLabel.place(x=120, y=40, width=50, height=20)
        
        self.gradientDescentStepEntry = tk.Entry(frame)
        self.gradientDescentStepEntry.place(x=170, y=40, width=50, height=20)

        funcLabel = tk.Label(frame, text="f(x) = ", font = "Calibri 15")
        funcLabel.place(x=220, y=40, width=60, height=20)

        fourDegreeCoefficientEntry = tk.Entry(frame)
        fourDegreeCoefficientEntry.place(x=280, y=40, width=30, height=20)

        fourDegreeLabel = tk.Label(frame, text="x⁴ + ", font = "Calibri 15")
        fourDegreeLabel.place(x=310, y=35, width=60, height=30)

        threeDegreeCoefficientEntry = tk.Entry(frame)
        threeDegreeCoefficientEntry.place(x=370, y=40, width=30, height=20)

        threeDegreeLabel = tk.Label(frame, text="x³ + ", font = "Calibri 15")
        threeDegreeLabel.place(x=400, y=35, width=60, height=30)

        twoDegreeCoefficientEntry = tk.Entry(frame)
        twoDegreeCoefficientEntry.place(x=460, y=40, width=30, height=20)

        twoDegreeLabel = tk.Label(frame, text="x² + ", font = "Calibri 15")
        twoDegreeLabel.place(x=490, y=35, width=60, height=30)

        oneDegreeCoefficientEntry = tk.Entry(frame)
        oneDegreeCoefficientEntry.place(x=550, y=40, width=30, height=20)

        oneDegreeLabel = tk.Label(frame, text="x¹ + ", font = "Calibri 15")
        oneDegreeLabel.place(x=580, y=35, width=60, height=30)

        constantEntry = tk.Entry(frame)
        constantEntry.place(x=640, y=40, width=30, height=20)

        self.gradientDescentCoefficentEntrys = [fourDegreeCoefficientEntry, threeDegreeCoefficientEntry, twoDegreeCoefficientEntry, oneDegreeCoefficientEntry, constantEntry]

        runButton = tk.Button(frame, text="run", font = "Calibri 13", command=self.runGradientDescent)
        runButton.place(x=680, y=40, width=70, height=20)

        # 뉴턴법 frame 위젯 배치
        self.frameDict["뉴턴법"] = tk.Frame(self.root, width=800, height=135)
        frame = self.frameDict["뉴턴법"]

        startXLabel = tk.Label(frame, text="Start X : ", font = "Calibri 15")
        startXLabel.place(x=0, y=10, width=80, height=20)

        self.newtonStartXEntry = tk.Entry(frame)
        self.newtonStartXEntry.place(x=80, y=10, width=50, height=20)

        stepLabel = tk.Label(frame, text="step : ", font = "Calibri 13")
        stepLabel.place(x=120, y=40, width=50, height=20)
        
        self.newtonStepEntry = tk.Entry(frame)
        self.newtonStepEntry.place(x=170, y=40, width=50, height=20)

        funcLabel = tk.Label(frame, text="f(x) = ", font = "Calibri 15")
        funcLabel.place(x=220, y=40, width=60, height=20)

        fourDegreeCoefficientEntry = tk.Entry(frame)
        fourDegreeCoefficientEntry.place(x=280, y=40, width=30, height=20)

        fourDegreeLabel = tk.Label(frame, text="x⁴ + ", font = "Calibri 15")
        fourDegreeLabel.place(x=310, y=35, width=60, height=30)

        threeDegreeCoefficientEntry = tk.Entry(frame)
        threeDegreeCoefficientEntry.place(x=370, y=40, width=30, height=20)

        threeDegreeLabel = tk.Label(frame, text="x³ + ", font = "Calibri 15")
        threeDegreeLabel.place(x=400, y=35, width=60, height=30)

        twoDegreeCoefficientEntry = tk.Entry(frame)
        twoDegreeCoefficientEntry.place(x=460, y=40, width=30, height=20)

        twoDegreeLabel = tk.Label(frame, text="x² + ", font = "Calibri 15")
        twoDegreeLabel.place(x=490, y=35, width=60, height=30)

        oneDegreeCoefficientEntry = tk.Entry(frame)
        oneDegreeCoefficientEntry.place(x=550, y=40, width=30, height=20)

        oneDegreeLabel = tk.Label(frame, text="x¹ + ", font = "Calibri 15")
        oneDegreeLabel.place(x=580, y=35, width=60, height=30)

        constantEntry = tk.Entry(frame)
        constantEntry.place(x=640, y=40, width=30, height=20)

        self.newtonCoefficentEntrys = [fourDegreeCoefficientEntry, threeDegreeCoefficientEntry, twoDegreeCoefficientEntry, oneDegreeCoefficientEntry, constantEntry]

        runButton = tk.Button(frame, text="run", font = "Calibri 13", command=self.runNewtonMethod)
        runButton.place(x=680, y=40, width=70, height=20)

        self.frameCombobox = ttk.Combobox(self.root, values=("경사하강법", "뉴턴법"), state="readonly")
        self.frameCombobox.bind("<<ComboboxSelected>>", self.frameCombobox_selected)
        self.frameCombobox.set(self.currentFrameKey)
        self.frameCombobox.pack(side="bottom")

        self.frameCombobox_selected()

    def main(self):
        self.root.mainloop()

    def frameCombobox_selected(self, event=None):
        self.frameDict[self.currentFrameKey].pack_forget()
        self.frameDict[self.frameCombobox.get()].pack(side="top")

        self.currentFrameKey = self.frameCombobox.get()
    
    def runGradientDescent(self):
        a = float(self.gradientDescentCoefficentEntrys[0].get())
        b = float(self.gradientDescentCoefficentEntrys[1].get())
        c = float(self.gradientDescentCoefficentEntrys[2].get())
        d = float(self.gradientDescentCoefficentEntrys[3].get())

        stepSize = float(self.gradientDescentStepSizeEntry.get())
        step = int(self.gradientDescentStepEntry.get())

        func = PolynomialFunc(d, c, b, a)

        dfunc = func.differentiate()

        x = float(self.gradientDescentStartXEntry.get())

        size = abs(x * 1.1)

        stepXPoints = []
        stepYPoints = []

        for i in range(step):
            try:
                print(f"x{i} = {x}")
                y = func.substitute(x)
                stepXPoints.append(x)
                stepYPoints.append(y)
                x = x - dfunc.substitute(x)*stepSize
            except:
                break

        funcXPoints = []
        funcYPoints = []

        i = -size
        temp = size / 100
        while i < size:
            funcXPoints.append(i)
            funcYPoints.append(func.substitute(i))
            i += temp

        self.showGraph((funcXPoints, funcYPoints, "b-"), (stepXPoints, stepYPoints, "r-"), (stepXPoints, stepYPoints, "ro"))

    def runNewtonMethod(self):
        a = float(self.newtonCoefficentEntrys[0].get())
        b = float(self.newtonCoefficentEntrys[1].get())
        c = float(self.newtonCoefficentEntrys[2].get())
        d = float(self.newtonCoefficentEntrys[3].get())

        step = int(self.newtonStepEntry.get())

        func = PolynomialFunc(d, c, b, a)

        dfunc = func.differentiate()
        ddfunc = dfunc.differentiate()

        x = float(self.newtonStartXEntry.get())

        size = abs(x * 1.1)

        stepXPoints = []
        stepYPoints = []

        for i in range(step):
            try:
                y = func.substitute(x)
                stepXPoints.append(x)
                stepYPoints.append(y)
                x = x - dfunc.substitute(x)/ddfunc.substitute(x)
                print(f"x{i} = {x}")
            except:
                break

        funcXPoints = []
        funcYPoints = []

        i = -size
        temp = size / 100
        while i < size:
            funcXPoints.append(i)
            funcYPoints.append(func.substitute(i))
            i += temp

        self.showGraph((funcXPoints, funcYPoints, "b-"), (stepXPoints, stepYPoints, "r-"), (stepXPoints, stepYPoints, "ro"))

    def showGraph(self, graph, *stepLines):
        x, y, fs = graph

        plt.axis((min(x), max(x), min(y) * 1.1 - 1, max(y) * 1.1 + 1))

        plt.plot(x, y, fs)

        for x, y, fs in stepLines:
            plt.plot(x, y, fs)

        plt.show()

Window().main()