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

"""Spherical projection of a cartesian vector according to the ISO
31-11 standard.
"""

from typing import Union

import numpy as np
from orix.vector import SphericalRegion, Vector3d

from kikuchipy._util import deprecated


class SphericalProjection:
    """[*Deprecated*] Spherical projection of a cartesian vector
    according to the ISO 31-11 standard.

    .. deprecated:: 0.8.0

        This class is deprecated and will be removed in 0.9.0, since it
        is not used internally. If you depend on this class, please open
        an issue at https://github.com/pyxem/kikuchipy/issues.
    """

    spherical_region = SphericalRegion([0, 0, 1])

    @classmethod
    @deprecated(since="0.8.0", removal="0.9.0")
    def vector2xy(cls, v: Union[Vector3d, np.ndarray]) -> np.ndarray:
        """Convert from cartesian to spherical coordinates according to
        the ISO 31-11 standard.

        Parameters
        ----------
        v
            3D vector(s) on the form
            ``[[x0, y0, z0], [x1, y1, z1], ...]``.

        Returns
        -------
        spherical_coordinates
            Spherical coordinates theta, phi and r on the form
            ``[[theta1, phi1, r1], [theta2, phi2, r2], ...]``.

        Examples
        --------
        >>> import numpy as np
        >>> from kikuchipy.projections import SphericalProjection
        >>> v = np.random.random_sample(30).reshape((10, 3))
        >>> theta, phi, r = SphericalProjection.vector2xy(v).T
        >>> np.allclose(np.arccos(v[:, 2] / r), theta)
        True
        >>> np.allclose(np.arctan2(v[:, 1], v[:, 0]), phi)
        True
        """
        return _get_polar_coordinates(v)


def _get_polar_coordinates(v: Union[Vector3d, np.ndarray]) -> np.ndarray:
    if isinstance(v, Vector3d):
        x, y, z = v.xyz
    else:
        x, y, z = v[..., 0], v[..., 1], v[..., 2]
    polar = np.zeros(x.shape + (3,), dtype=x.dtype)
    polar[..., 1] = np.where(
        np.arctan2(y, x) < 0, np.arctan2(y, x) + 2 * np.pi, np.arctan2(y, x)
    )  # Azimuth
    polar[..., 2] = np.sqrt(x**2 + y**2 + z**2)  # r
    polar[..., 0] = np.arccos(z / polar[..., 2])  # Polar

    return polar


@deprecated(since="0.8.0", removal="0.9.0")
def get_polar(v: Union[Vector3d, np.ndarray]) -> np.ndarray:
    """Get the polar spherical coordinate from cartesian according to
    the ISO 31-11 standard.

    Parameters
    ----------
    v
        3D vector(s) on the form [[x0, y0, z0], [x1, y1, z1], ...].

    Returns
    -------
    polar
        Polar spherical coordinate.
    """
    if isinstance(v, Vector3d):
        x, y, z = v.xyz
    else:
        x, y, z = v[..., 0], v[..., 1], v[..., 2]
    r = np.sqrt(x**2 + y**2 + z**2)
    return np.arccos(z / r)


@deprecated(since="0.8.0", removal="0.9.0")
def get_azimuth(v: Union[Vector3d, np.ndarray]) -> np.ndarray:
    """Get the azimuthal spherical coordinate from cartesian according
    to the ISO 31-11 standard.

    Parameters
    ----------
    v
        3D vector(s) on the form [[x0, y0, z0], [x1, y1, z1], ...].

    Returns
    -------
    azimuth
        Azimuthal spherical coordinate.
    """
    if isinstance(v, Vector3d):
        x, y, _ = v.xyz
    else:
        x, y = v[..., 0], v[..., 1]
    azimuth = np.arctan2(y, x)
    azimuth += (azimuth < 0) * 2 * np.pi
    return azimuth


@deprecated(since="0.8.0", removal="0.9.0")
def get_radial(v: Union[Vector3d, np.ndarray]) -> np.ndarray:
    """Get the radial spherical coordinate from cartesian coordinates.

    Parameters
    ----------
    v
        3D vector(s) on the form [[x0, y0, z0], [x1, y1, z1], ...].

    Returns
    -------
    radial
        Radial spherical coordinate.
    """
    if isinstance(v, Vector3d):
        x, y, z = v.xyz
    else:
        x, y, z = v[..., 0], v[..., 1], v[..., 2]
    return np.sqrt(x**2 + y**2 + z**2)
