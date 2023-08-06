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

from typing import Optional

from .base import boulder_opal_workflow


@boulder_opal_workflow("closed_loop_step_workflow")
def closed_loop_step_workflow(
    optimizer: dict, results: Optional[dict], test_point_count: Optional[int]
):
    """Runs the `closed_loop_step_workflow` workflow."""
    return {
        "optimizer": optimizer,
        "results": results,
        "test_point_count": test_point_count,
    }
