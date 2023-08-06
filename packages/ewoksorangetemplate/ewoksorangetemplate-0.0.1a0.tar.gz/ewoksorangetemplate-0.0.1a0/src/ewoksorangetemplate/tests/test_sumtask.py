import pytest
from ewoksorange.tests.utils import execute_task

from orangecontrib.ewoksorangetemplate.sumtask import OWSumTask
from orangecontrib.ewoksorangetemplate.categories.examples1.sumtask import OWSumTask1
from orangecontrib.ewoksorangetemplate.categories.examples2.sumtask import OWSumTask2


@pytest.mark.parametrize("widget", [OWSumTask, OWSumTask1, OWSumTask2])
def test_sum_task(widget):
    assert_sum_task(widget, None)


@pytest.mark.parametrize("widget", [OWSumTask, OWSumTask1, OWSumTask2])
def test_sum_task_widget(widget, qtapp):
    assert_sum_task(widget, qtapp)


def assert_sum_task(widget, qtapp):
    results = execute_task(
        widget.ewokstaskclass if qtapp is None else widget,
        inputs={"a": 1, "b": 2},
    )
    assert results == {"result": 3}
