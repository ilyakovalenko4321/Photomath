import tkinter as tk
import numpy as np
import os

sights_list = []
class Paint:
    """
    Программа Paint позволяет рисовать на холсте с помощью мыши.
    """

    def __init__(self, canvas_size=280):
        """
        Инициализация программы Paint.

        Параметры:
        - canvas_size: размер холста (по умолчанию 28x28 пикселей)
        """
        self.canvas_size = canvas_size

        self.root = tk.Tk()
        self.root.title("Paint")

        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.on_mouse)
        self.root.bind("<space>", self.save_canvas)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.canvas_data = np.zeros((canvas_size, canvas_size))

    def on_mouse(self, event):
        """
        Обработчик события движения мыши.

        Параметры:
        - event: объект события
        """
        x = event.x * self.canvas_size // self.canvas.winfo_width()
        y = event.y * self.canvas_size // self.canvas.winfo_height()
        self.canvas.create_oval(x, y, x+10, y+10, fill="black")
        self.canvas_data[y-4:y+4, x-4:x+4] = 1


    def save_canvas(self, event):
        """
        Сохранение холста в виде numpy списка и очистка холста.

        Параметры:
        - event: объект события
        """
        sights_list.append(self.canvas_data)
        self.canvas.delete("all")
        self.canvas_data = np.zeros((self.canvas_size, self.canvas_size))

    def on_close(self):
        """
        Обработчик события закрытия программы.
        """
        sight_list = np.asarray(sights_list)
        print(sight_list.shape)
        np.save("canvas_data.npy", sight_list)
        self.save_canvas(None)  # Сохраняем холст перед закрытием
        self.root.destroy()

    def run(self):
        """
        Запуск программы Paint.
        """
        self.root.mainloop()

# Пример использования программы Paint
paint = Paint()
paint.run()


