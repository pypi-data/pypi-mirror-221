import matplotlib.pyplot as plt  # type: ignore
import platform

# 中文字体
import matplotlib.font_manager as fm  # type: ignore


def set_matplotlib_cn_font():
    if platform.system() == 'Windows':
        fm.findSystemFonts(fontpaths=None, fontext="ttf")  # type: ignore
        fm.findfont("SimSun")  # for windows
        plt.rcParams['font.sans-serif'] = ['SimSun']  # for windows

    elif platform.system() == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # for mac
