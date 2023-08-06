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
    Any,
    Optional,
)

import numpy as np

from .base import boulder_opal_workflow


@boulder_opal_workflow("reconstruct_noise_workflow")
def reconstruct_noise_workflow(
    method: dict[str, dict[str, Any]],
    noises_frequencies: list[np.ndarray],
    filter_functions: list[np.ndarray],
    infidelities: np.ndarray,
    infidelity_uncertainties: Optional[np.ndarray],
):
    """
    Run the `reconstruct_noise_workflow` workflow.
    """
    return {
        "method": method,
        "noises_frequencies": noises_frequencies,
        "filter_functions": filter_functions,
        "infidelities": infidelities,
        "infidelity_uncertainties": infidelity_uncertainties,
    }
