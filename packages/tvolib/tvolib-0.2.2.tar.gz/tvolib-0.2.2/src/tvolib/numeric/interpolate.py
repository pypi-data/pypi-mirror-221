__all__ = ["interpol"]

import astropy.units as u
import numpy as np
from scipy.interpolate import interp1d
from .timing import sampling_period
from .moving import move_avg


def interpol(y, x, xout, window=None, kind="linear"):
    r"""Interpolate a signal onto a new temporal grid.

    This function mimics IDL's interpol routine. When downsampling, the
    window argument can be set to apply a moving average over the
    original temporal grid. Additionally, astropy.Quantity are preserved
    from this function.
    """

    if not (
        (
            np.issubdtype(x.dtype, np.datetime64)
            and np.issubdtype(xout.dtype, np.datetime64)
        )
    ):
        raise NotImplementedError("Time arrays must be datetime64 dtype.")

    interp_kw = dict(kind=kind, bounds_error=False, fill_value=np.nan)
    if window is not None:
        w = (sampling_period(xout) / sampling_period(x)).decompose()
        assert w >= 1, "xout has higher resolution!"
        if window == "box":
            w = np.int64(max(w, 1))

    x = x.astype("f8")
    xout = xout.astype("f8")

    if len(y.shape) == 1:
        yin = move_avg(y, (w,), window=window) if window is not None else y
        yout = interp1d(x, yin, **interp_kw)(xout)
    elif len(y.shape) == 2:
        yout = np.empty((len(xout), N := y.shape[1]))
        for i in range(N):
            yin = (
                move_avg(y[:, i], (w,), window=window)
                if window is not None
                else y[:, i]
            )
            yout[:, i] = interp1d(x, yin, **interp_kw)(xout)
    else:
        raise NotImplementedError("Max dimensionality is 2.")

    if isinstance(y, u.Quantity):
        yout *= u.Unit(y.unit)

    return yout
