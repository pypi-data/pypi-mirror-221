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

from typing import Optional

import numpy as np

from .base import boulder_opal_workflow


@boulder_opal_workflow("obtain_ion_chain_properties_workflow")
def obtain_ion_chain_properties_workflow(
    atomic_mass: float,
    ion_count: int,
    center_of_mass_frequencies: np.ndarray,
    wavevector: np.ndarray,
    laser_detuning: Optional[float],
):
    """Runs the `obtain_ion_chain_properties_workflow` workflow."""
    return {
        "atomic_mass": atomic_mass,
        "ion_count": ion_count,
        "center_of_mass_frequencies": center_of_mass_frequencies,
        "wavevector": wavevector,
        "laser_detuning": laser_detuning,
    }
