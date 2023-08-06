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

from typing import (
    TYPE_CHECKING,
    Optional,
)

from .base import boulder_opal_workflow

if TYPE_CHECKING:
    from boulderopal.graph import Graph


@boulder_opal_workflow("run_optimization_workflow")
def run_optimization_workflow(
    graph: "Graph",
    optimization_count: int,
    cost_node_name: str,
    output_node_names: list[str],
    target_cost: Optional[float],
    max_iteration_count: Optional[int],
    cost_tolerance: Optional[float],
    cost_history_scope: str,
    seed: Optional[int],
):
    """Runs the `run_optimization_workflow` workflow."""

    return {
        "graph": graph,
        "optimization_count": optimization_count,
        "cost_node_name": cost_node_name,
        "output_node_names": output_node_names,
        "target_cost": target_cost,
        "max_iteration_count": max_iteration_count,
        "cost_tolerance": cost_tolerance,
        "cost_history_scope": cost_history_scope,
        "seed": seed,
    }
