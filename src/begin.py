"""
@Project Description:The main function of this project is to generate arithmetic problems for children to practice
@项目描述：这个项目主要功能是生成算数题给小朋友做练习
"""
import tkinter as tk
from UI_initialize import main_window_init


if __name__ == "__main__":
    """
    主要执行程序
    """
    root = tk.Tk()
    main_window = main_window_init.MainWindow(root)
    root.mainloop()
