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

from typing import Union
import warnings

import numpy as np
from orix.vector import Vector3d

from kikuchipy.projections.spherical_projection import SphericalProjection
from kikuchipy._util import deprecated


class GnomonicProjection(SphericalProjection):
    """[*Deprecated*] Gnomonic projection of a vector as implemented in
    MTEX.

    .. deprecated:: 0.8.0

        This class is deprecated and will be removed in 0.9.0, since it
        is not used internally. If you depend on this class, please open
        an issue at https://github.com/pyxem/kikuchipy/issues.
    """

    @classmethod
    @deprecated(since="0.8.0", removal="0.9.0")
    def vector2xy(cls, v: Union[Vector3d, np.ndarray]) -> np.ndarray:
        r"""Convert from 3D cartesian coordinates :math:`(x, y, z)` to
        2D Gnomonic coordinates :math:`(x_g, y_g)`.

        Parameters
        ----------
        v
            3D vector(s) on the form
            ``[[x0, y0, z0], [x1, y1, z1], ...]``.

        Returns
        -------
        gnomonic_coordinates
            Gnomonic coordinates on the form
            ``[[x0, y0], [x1, y1], ...]``.

        Examples
        --------
        >>> import numpy as np
        >>> from kikuchipy.projections import GnomonicProjection
        >>> v = np.random.random_sample(30).reshape((10, 3))
        >>> xy = GnomonicProjection.vector2xy(v)
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            polar_coordinates = super().vector2xy(v)
        polar, azimuth = polar_coordinates[..., 0], polar_coordinates[..., 1]

        # Map to upper hemisphere
        if isinstance(v, Vector3d):
            is_upper = v.z > 0
        else:
            is_upper = v[..., 2] > 0
        polar[is_upper] -= np.pi

        # Formula for gnomonic projection
        r = np.tan(polar)

        # Compute coordinates
        gnomonic = np.zeros(r.shape + (2,), dtype=r.dtype)
        gnomonic[..., 0] = np.cos(azimuth) * r
        gnomonic[..., 1] = np.sin(azimuth) * r

        return gnomonic

    @staticmethod
    @deprecated(since="0.8.0", removal="0.9.0")
    def xy2vector(xy: np.ndarray) -> Vector3d:
        r"""Convert from 2D Gnomonic coordinates :math:`(x_g, y_g)` to
        3D cartesian coordiantes :math:`(x, y, z)`.

        Parameters
        ----------
        xy
            2D coordinates on the form
            ``[[x_g0, y_g0], [x_g1, y_g1], ...]``.

        Returns
        -------
        cartesian_coordinates
            Cartesian coordinates :math:`(x, y, z)` on the form
            ``[[x0, y0, z0], [x1, y1, z1], ...]``.

        Examples
        --------
        >>> import numpy as np
        >>> from kikuchipy.projections import GnomonicProjection
        >>> xy_g = np.random.random_sample(20).reshape((10, 2))
        >>> xyz = GnomonicProjection.xy2vector(xy_g)
        """
        x, y = xy[..., 0], xy[..., 1]
        polar = np.arctan(np.sqrt(x**2 + y**2))
        azimuth = np.arctan2(y, x)
        return Vector3d.from_polar(polar=polar, azimuth=azimuth)
