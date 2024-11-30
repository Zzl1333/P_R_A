import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPen, QColor, QBrush


def FIFO(page_capacity, page_references, output_text_edit, graphics_scene):
    """
    FIFO页面置换算法实现。

    :param page_capacity: 内存页框数量
    :param page_references: 页面引用序列
    :param output_text_edit: 输出文本编辑器
    :param graphics_scene: 图形场景
    """
    output_text_edit.append("FIFO页面置换过程为:")
    memory = []  # 用于存储当前在内存中的页面及其进入时间
    page_faults = 0  # 记录缺页次数
    step_graphics = []  # 用于存储每一步的图形状态

    for i, page in enumerate(page_references):
        if page not in [p[0] for p in memory]:
            # 如果页面不在内存中，发生缺页
            page_faults += 1
            if len(memory) >= page_capacity:
                # 如果内存已满，移除最早进入的页面
                removed_page, _ = memory.pop(0)
                # 更新绘图
                for item in graphics_scene.items():
                    if isinstance(item, QGraphicsTextItem) and item.toPlainText().startswith(str(removed_page)):
                        graphics_scene.removeItem(item)
                        break
            # 添加新页面到内存
            memory.append((page, i + 1))  # 存储页面及其进入时间
        # 打印当前页面引用和内存状态
        output_text_edit.append(f"第{i + 1}页: 内存状态 {[f'{p[0]}(t={p[1]})' for p in memory]}")
        # 更新绘图
        current_graphics = update_graphics_scene(graphics_scene, memory)
        step_graphics.append(current_graphics.copy())

    # 计算缺页率
    page_fault_rate = page_faults / len(page_references)
    output_text_edit.append(f"FIFO缺页率为：{page_fault_rate:.2f}")

    # 显示所有步骤的图形状态
    for step in step_graphics:
        graphics_scene.clear()
        for item in step:
            graphics_scene.addItem(item)
         # 处理事件，确保图形更新
        import time
        time.sleep(2)  # 暂停1秒，以便观察每一步的变化


def update_graphics_scene(graphics_scene, memory):
    """
    更新图形场景。

    :param graphics_scene: 图形场景
    :param memory: 当前在内存中的页面及其进入时间
    """
    graphics_scene.clear()
    items = []
    for i, (page, enter_time) in enumerate(memory):
        rect = QGraphicsRectItem(50 + i * 100, 50, 90, 90)
        rect.setPen(QPen(Qt.black))
        rect.setBrush(QColor(128, 128, 128))
        graphics_scene.addItem(rect)
        items.append(rect)
        text = QGraphicsTextItem(f"{page}(t={enter_time})")
        text.setPos(50 + i * 100 + 20, 50 + 20)
        graphics_scene.addItem(text)
        items.append(text)
    return items


class FIFO(QMainWindow):
    """
    FIFO类。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setWindowTitle("FIFO 页面置换算法")
        self.setGeometry(50, 50, 1600, 900)
        self.title_label = QLabel("FIFO", self)
        self.title_label.setGeometry(220, 150, 200, 60)
        self.title_label.setStyleSheet("font-size: 70px; font-weight: bold; color: black;")
        layout.addWidget(self.title_label)

        # 创建输入控件
        self.page_capacity_label = QLabel("内存页框数:", self)
        self.page_capacity_input = QLineEdit(self)
        self.page_references_label = QLabel("页面引用序列:", self)
        self.page_references_input = QLineEdit(self)

        # 创建按钮
        self.return_button = QPushButton("返回上一界面", self)
        self.return_button.clicked.connect(self.close)
        self.run_once_button = QPushButton("一键生成", self)
        self.run_once_button.clicked.connect(self.run_FIFO_once)
        self.run_button = QPushButton("逐步运行", self)
        self.run_button.clicked.connect(self.run_FIFO_step)
        self.clear_button = QPushButton("清除", self)
        self.clear_button.clicked.connect(self.clear_all)

        # 创建输出控件
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setReadOnly(True)

        # 创建绘图区域
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setBackgroundBrush(QBrush(QColor(255, 255, 255)))  # 设置背景颜色为白色
        self.graphics_view.setFixedSize(700, 300)  # 设置固定大小
        self.graphics_scene = QGraphicsScene()
        self.graphics_view.setScene(self.graphics_scene)

        # 设置控件的位置和大小
        self.return_button.setGeometry(1300, 760, 200, 50)
        self.page_capacity_label.setGeometry(50, 650, 100, 30)
        self.page_capacity_input.setGeometry(50, 680, 100, 30)
        self.page_references_label.setGeometry(50, 550, 200, 30)
        self.page_references_input.setGeometry(50, 580, 200, 30)
        self.run_button.setGeometry(470, 560, 100, 30)
        self.run_once_button.setGeometry(470, 630, 100, 30)
        self.clear_button.setGeometry(470, 700, 100, 30)
        self.output_text_edit.setGeometry(760, 400, 500, 300)
        self.graphics_view.setGeometry(750, 50, 700, 300)

        # 初始化变量
        self.page_capacity = 0
        self.page_references = []
        self.memory = []
        self.page_faults = 0
        self.step_index = 0

    @Slot()
    def run_FIFO_step(self):
        """
        每次按下运行按钮时进行一次FIFO页面置换操作。
        """
        try:
            if self.step_index == 0:
                self.page_capacity = int(self.page_capacity_input.text())
                self.page_references = list(map(int, self.page_references_input.text()))
                self.output_text_edit.clear()
                self.graphics_scene.clear()
                self.memory = []
                self.page_faults = 0

            if self.step_index < len(self.page_references):
                page = self.page_references[self.step_index]
                if page not in [p[0] for p in self.memory]:
                    # 如果页面不在内存中，发生缺页
                    self.page_faults += 1
                    if len(self.memory) >= self.page_capacity:
                        # 如果内存已满，移除最早进入的页面
                        removed_page, _ = self.memory.pop(0)
                        # 更新绘图
                        for item in self.graphics_scene.items():
                            if isinstance(item, QGraphicsTextItem) and item.toPlainText().startswith(str(removed_page)):
                                self.graphics_scene.removeItem(item)
                                break
                    # 添加新页面到内存
                    self.memory.append((page, self.step_index + 1))  # 存储页面及其进入时间
                # 打印当前页面引用和内存状态
                self.output_text_edit.append(f"第{self.step_index + 1}页: 内存状态 {[f'{p[0]}(t={p[1]})' for p in self.memory]}")
                # 更新绘图
                update_graphics_scene(self.graphics_scene, self.memory)
                self.step_index += 1
            else:
                # 计算缺页率
                page_fault_rate = self.page_faults / len(self.page_references)
                self.output_text_edit.append(f"FIFO缺页率为：{page_fault_rate:.2f}")
                # 禁用运行按钮
                self.run_button.setEnabled(False)
        except ValueError as e:
            self.output_text_edit.append(f"输入错误: {e}")

    def run_FIFO_once(self):
        """
        单次运行FIFO页面置换算法。
        """
        try:
            page_capacity = int(self.page_capacity_input.text())
            page_references = list(map(int, self.page_references_input.text()))
            self.output_text_edit.clear()
            self.graphics_scene.clear()

            memory = []  # 用于存储当前在内存中的页面及其进入时间
            page_faults = 0  # 记录缺页次数

            for step_index, page in enumerate(page_references):
                if page not in [p[0] for p in memory]:
                    # 如果页面不在内存中，发生缺页
                    page_faults += 1
                    if len(memory) >= page_capacity:
                        # 如果内存已满，移除最早进入的页面
                        removed_page, _ = memory.pop(0)
                        # 更新绘图
                        for item in self.graphics_scene.items():
                            if isinstance(item, QGraphicsTextItem) and item.toPlainText().startswith(str(removed_page)):
                                self.graphics_scene.removeItem(item)
                                break
                    # 添加新页面到内存
                    memory.append((page, step_index + 1))  # 存储页面及其进入时间
                # 打印当前页面引用和内存状态
                self.output_text_edit.append(f"第{step_index + 1}页: 内存状态 {[f'{p[0]}(t={p[1]})' for p in memory]}")
                # 更新绘图
                update_graphics_scene(self.graphics_scene, memory)

            # 计算缺页率
            page_fault_rate = page_faults / len(page_references)
            self.output_text_edit.append(f"FIFO缺页率为：{page_fault_rate:.2f}")
            # 禁用运行按钮
            self.run_button.setEnabled(False)
        except ValueError as e:
            self.output_text_edit.append(f"输入错误: {e}")

    @Slot()
    def clear_all(self):
        """
        清除所有输入和输出内容。
        """
        self.page_capacity_input.clear()
        self.page_references_input.clear()
        self.output_text_edit.clear()
        self.graphics_scene.clear()
        self.page_capacity = 0
        self.page_references = []
        self.memory = []
        self.page_faults = 0
        self.step_index = 0
        # 重新启用运行按钮
        self.run_button.setEnabled(True)


def FIFO_control(parent=None):
    if parent is None:
        parent = QApplication.instance()  # 获取现有的 QApplication 实例
        if not parent:  # 如果没有现有的 QApplication 实例，则创建一个新的
            parent = QApplication(sys.argv)
    win = FIFO(parent)  # 传递 parent 参数
    win.show()
    return parent  # 返回 QApplication 实例以便在主程序中调用 exec()


