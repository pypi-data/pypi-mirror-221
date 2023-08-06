from AnyQt import QtWidgets
from ewoksorange.gui.orange_imports import Input, Output
from ewoksorange.bindings import OWEwoksWidgetOneThread

from ewoksorangetemplate.tasks.sumtask import SumTask2


__all__ = ["OWSumTask2"]


class OWSumTask2(OWEwoksWidgetOneThread, ewokstaskclass=SumTask2):
    name = "SumTask2"
    description = "Adds two numbers"
    icon = "icons/sum.png"
    want_main_area = True

    class Inputs:
        a = Input("A", int)
        b = Input("B", int)
        delay = Input("Delay", float)

    class Outputs:
        result = Output("A + B", int)

    def __init__(self) -> None:
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self) -> None:
        super()._init_control_area()

        self._input_widgets = QtWidgets.QWidget()
        self._get_control_layout().addWidget(self._input_widgets)

        grid = QtWidgets.QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(4)
        self._input_widgets.setLayout(grid)

        self._widgetA_label = QtWidgets.QLabel("A")
        self._widgetA_value = QtWidgets.QSpinBox()
        grid.addWidget(self._widgetA_label, 0, 0)
        grid.addWidget(self._widgetA_value, 0, 1)

        self._widgetB_label = QtWidgets.QLabel("B")
        self._widgetB_value = QtWidgets.QSpinBox()
        grid.addWidget(self._widgetB_label, 1, 0)
        grid.addWidget(self._widgetB_value, 1, 1)

        self._widgetDelay_label = QtWidgets.QLabel("Delay")
        self._widgetDelay_value = QtWidgets.QDoubleSpinBox()
        grid.addWidget(self._widgetDelay_label, 2, 0)
        grid.addWidget(self._widgetDelay_value, 2, 1)

        self._update_input_widget_values(self.get_default_input_values())

        self._widgetA_value.editingFinished.connect(self._default_inputs_changed)
        self._widgetB_value.editingFinished.connect(self._default_inputs_changed)
        self._widgetDelay_value.editingFinished.connect(self._default_inputs_changed)

    def _init_main_area(self) -> None:
        super()._init_main_area()

        self._output_widgets = QtWidgets.QWidget()
        self._get_main_layout().addWidget(self._output_widgets)

        grid = QtWidgets.QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(4)
        self._output_widgets.setLayout(grid)

        self._widgetResult_label = QtWidgets.QLabel("Result")
        self._widgetResult_value = QtWidgets.QLineEdit()
        grid.addWidget(self._widgetResult_label, 0, 0)
        grid.addWidget(self._widgetResult_value, 0, 1)

    def _default_inputs_changed(self) -> None:
        self.update_default_inputs(**self._fetch_input_widget_values())

    def handleNewSignals(self) -> None:
        self._update_input_widget_values(self.get_dynamic_input_values())
        super().handleNewSignals()

    def _fetch_input_widget_values(self) -> dict:
        return {
            "a": self._widgetA_value.value(),
            "b": self._widgetB_value.value(),
            "delay": self._widgetDelay_value.value(),
        }

    def _update_input_widget_values(self, data: dict) -> None:
        for name, value in data.items():
            if name == "a":
                self._widgetA_value.setValue(value)
            elif name == "b":
                self._widgetB_value.setValue(value)
            elif name == "delay":
                self._widgetDelay_value.setValue(value)

    def task_output_changed(self) -> None:
        for name, value in self.get_task_output_values().items():
            if name == "result":
                self._widgetResult_value.setText(str(value))
        super().task_output_changed()
