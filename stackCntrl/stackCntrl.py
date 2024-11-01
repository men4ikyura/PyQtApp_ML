
class StackCntrl:

    @staticmethod
    def clear_stacked_widget(stack):
        """Удаляет все виджеты из QStackedWidget."""
        while stack.count():
            widget = stack.widget(0)
            stack.removeWidget(widget)
            widget.deleteLater()  # Освобождает память