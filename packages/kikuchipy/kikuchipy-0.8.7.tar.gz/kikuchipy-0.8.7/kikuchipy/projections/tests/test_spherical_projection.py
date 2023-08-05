# Copyright 2019-2023 The kikuchipy developers
#
# This file is part of kikuchipy.
#
# kikuchipy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kikuchipy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kikuchipy. If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from orix.vector import Vector3d
import pytest

from kikuchipy.projections.spherical_projection import (
    SphericalProjection,
    get_polar,
    get_azimuth,
    get_radial,
)


def test_spherical_projection():
    """Compared against tests in orix."""
    n = 10
    v_arr = np.random.random_sample(n * 3).reshape((n, 3))
    v = Vector3d(v_arr)

    # Vector3d
    with pytest.warns(np.VisibleDeprecationWarning):
        polar = SphericalProjection.vector2xy(v_arr)
    assert np.allclose(polar[..., 0], v.polar.data)
    assert np.allclose(polar[..., 1], v.azimuth.data)
    assert np.allclose(polar[..., 2], v.radial.data)
    with pytest.warns(np.VisibleDeprecationWarning):
        assert np.allclose(get_polar(v), v.polar.data)
    with pytest.warns(np.VisibleDeprecationWarning):
        assert np.allclose(get_azimuth(v), v.azimuth.data)
    with pytest.warns(np.VisibleDeprecationWarning):
        assert np.allclose(get_radial(v), v.radial.data)

    # NumPy array
    with pytest.warns(np.VisibleDeprecationWarning):
        polar2 = SphericalProjection.vector2xy(v)
    assert np.allclose(polar2[..., 0], v.polar.data)
    assert np.allclose(polar2[..., 1], v.azimuth.data)
    assert np.allclose(polar2[..., 2], v.radial.data)
    with pytest.warns(np.VisibleDeprecationWarning):
        assert np.allclose(get_polar(v_arr), v.polar.data)
    with pytest.warns(np.VisibleDeprecationWarning):
        assert np.allclose(get_azimuth(v_arr), v.azimuth.data)
    with pytest.warns(np.VisibleDeprecationWarning):
        assert np.allclose(get_radial(v_arr), v.radial.data)
