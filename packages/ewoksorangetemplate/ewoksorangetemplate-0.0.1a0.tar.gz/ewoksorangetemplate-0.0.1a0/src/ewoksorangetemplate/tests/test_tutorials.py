from typing import List, Dict

import pytest
from ewoksorange.bindings import ows_to_ewoks
from ewokscore import execute_graph

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources

from orangecontrib.ewoksorangetemplate import tutorials
from orangecontrib.ewoksorangetemplate.categories.examples1 import (
    tutorials as tutorials1,
)
from orangecontrib.ewoksorangetemplate.categories.examples2 import (
    tutorials as tutorials2,
)


_WORKFLOWS = [
    (tutorials, "examples.ows"),
    (tutorials1, "examples1.ows"),
    (tutorials2, "examples2.ows"),
]


@pytest.mark.parametrize("workflow", _WORKFLOWS)
def test_examples_without_qt(workflow):
    module, basename = workflow
    with resources.path(module, basename) as filename:
        assert_examples_without_qt(filename)


@pytest.mark.parametrize("workflow", _WORKFLOWS)
def test_examples_with_qt(workflow, ewoks_orange_canvas):
    module, basename = workflow
    with resources.path(module, basename) as filename:
        assert_examples_with_qt(ewoks_orange_canvas, filename)


def assert_examples_without_qt(filename):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph, inputs=get_inputs(), outputs=[{"all": True}], merge_outputs=False
    )
    expected = get_expected_outputs()
    label_to_id = {
        attrs["label"]: node_id for node_id, attrs in graph.graph.nodes.items()
    }
    expected = {label_to_id[k]: v for k, v in expected.items()}
    assert outputs == expected


def assert_examples_with_qt(ewoks_orange_canvas, filename):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=get_inputs())
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=10)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    assert outputs == get_expected_outputs()


def get_inputs() -> List[dict]:
    return [
        {"label": "node1", "name": "a", "value": 10},
        {"label": "node2", "name": "a", "value": 20},
    ]


def get_expected_outputs() -> Dict[str, dict]:
    return {"node1": {"result": 10}, "node2": {"result": 20}, "node3": {"result": 30}}
