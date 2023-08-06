""" 
Simple Message
"""

from __future__ import annotations

from typing import Callable

from PySide2 import QtWidgets, QtSvg, QtCore


class NotificationMessage(QtWidgets.QWidget):
    def __init__(self, message: str, buttons: list[tuple[str, Callable]] | None = None, icon_path: str | None = None):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)
        layout_margin = QtCore.QMargins(10, 0, 10, 5)

        content_widget = QtWidgets.QWidget()
        content_widget_layout = QtWidgets.QHBoxLayout(content_widget)

        if icon_path:
            layout_margin.setLeft(0)
            svg_widget = QtSvg.QSvgWidget(icon_path)
            svg_widget.setFixedSize(40, 40)
            content_widget_layout.addWidget(svg_widget)

        message_label = QtWidgets.QLabel(message)
        # Wrap the text
        message_label.setWordWrap(True)
        content_widget_layout.addWidget(message_label)

        layout.setContentsMargins(layout_margin)
        layout.addWidget(content_widget)

        if buttons:
            button_layout = QtWidgets.QHBoxLayout()

            spacer = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            button_layout.addItem(spacer)

            for button_text, callback in buttons:
                button = QtWidgets.QPushButton(button_text)
                button.clicked.connect(callback)
                button_layout.addWidget(button)

            layout.addLayout(button_layout)

    def on_button_click(self, callback: Callable) -> None:
        if callback():
            self.close()
