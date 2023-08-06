# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from __future__ import annotations

from typing import TYPE_CHECKING

from .base import boulder_opal_workflow

if TYPE_CHECKING:
    from boulderopal.graph import Graph


@boulder_opal_workflow("execute_graph_workflow")
def execute_graph_workflow(
    graph: "Graph", output_node_names: list[str], execution_mode: str
):
    """Runs the `execute_graph_workflow` workflow."""

    return {
        "graph": graph,
        "output_node_names": output_node_names,
        "execution_mode": execution_mode,
    }
