# This file is part of tad-dftd3.
# SPDX-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Test calculation of dispersion energy and nuclear gradients.
"""
import pytest
import torch

from tad_dftd3 import damping, data, dftd3, model, ncoord, reference, util

from .samples import samples


@pytest.mark.parametrize("dtype", [torch.float32, torch.float64])
def test_single(dtype: torch.dtype) -> None:
    sample = samples["PbH4-BiH3"]
    numbers = sample["numbers"]
    positions = sample["positions"].type(dtype)
    ref = sample["disp2"].type(dtype)

    rcov = data.covalent_rad_d3[numbers]
    rvdw = data.vdw_rad_d3[numbers.unsqueeze(-1), numbers.unsqueeze(-2)]
    r4r2 = data.sqrt_z_r4_over_r2[numbers]
    cutoff = torch.tensor(50, dtype=dtype)

    param = {
        "a1": positions.new_tensor(0.49484001),
        "s8": positions.new_tensor(0.78981345),
        "a2": positions.new_tensor(5.73083694),
    }

    energy = dftd3(
        numbers,
        positions,
        param,
        ref=reference.Reference(dtype=dtype),
        rcov=rcov,
        rvdw=rvdw,
        r4r2=r4r2,
        cutoff=cutoff,
        counting_function=ncoord.exp_count,
        weighting_function=model.gaussian_weight,
        damping_function=damping.rational_damping,
    )

    assert energy.dtype == dtype
    assert torch.allclose(energy, ref)


@pytest.mark.parametrize("dtype", [torch.float32, torch.float64])
def test_batch(dtype: torch.dtype) -> None:
    sample1, sample2 = (samples["PbH4-BiH3"], samples["C6H5I-CH3SH"])
    numbers = util.pack(
        (
            sample1["numbers"],
            sample2["numbers"],
        )
    )
    positions = util.pack(
        (
            sample1["positions"].type(dtype),
            sample2["positions"].type(dtype),
        )
    )
    ref = util.pack(
        (
            sample1["disp2"].type(dtype),
            sample2["disp2"].type(dtype),
        )
    )

    param = {
        "a1": positions.new_tensor(0.49484001),
        "s8": positions.new_tensor(0.78981345),
        "a2": positions.new_tensor(5.73083694),
    }

    energy = dftd3(numbers, positions, param)

    assert energy.dtype == dtype
    assert torch.allclose(energy, ref)
