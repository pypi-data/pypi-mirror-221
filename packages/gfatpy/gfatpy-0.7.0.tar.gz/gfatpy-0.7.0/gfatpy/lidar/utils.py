import os
import zipfile
import tempfile
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import overload, Any

import xarray as xr
from scipy.signal import savgol_filter
from scipy.integrate import cumulative_trapezoid, cumtrapz

from .types import ParamsDict, LidarInfoType
from gfatpy.atmo import atmo, ecmwf
from gfatpy.utils.io import read_yaml

""" MODULE For General Lidar Utilities
"""

# LIDAR SYSTEM INFO
INFO_FILE = Path(__file__).parent.absolute() / "info.yml"
LIDAR_INFO: LidarInfoType = read_yaml(INFO_FILE)

INFO_PLOT_FILE = Path(__file__).parent.absolute() / "plot" / "info.yml"
LIDAR_PLOT_INFO = read_yaml(INFO_PLOT_FILE)


@overload
def signal_to_rcs(signal: xr.DataArray, ranges: xr.DataArray) -> xr.DataArray:
    ...


@overload
def signal_to_rcs(
    signal: np.ndarray[Any, np.dtype[np.float64]],
    ranges: np.ndarray[Any, np.dtype[np.float64]],
) -> np.ndarray[Any, np.dtype[np.float64]]:
    ...


def signal_to_rcs(signal, ranges):
    """Convert Lidar Signal to range-corrected signal

    Args:
        signal (np.ndarray[Any, np.dtype[np.float64]] | xr.DataArray): Lidar signal
        ranges (np.ndarray[Any, np.dtype[np.float64]] | xr.DataArray): Lidar ranges of signal

    Returns:
         xr.DataArray | np.ndarray[Any, np.dtype[np.float64]]: Range-corrected signal

    """
    return signal * ranges**2


@overload
def rcs_to_signal(rcs: xr.DataArray, ranges: xr.DataArray) -> xr.DataArray:
    ...


@overload
def rcs_to_signal(rcs: np.ndarray, ranges: np.ndarray) -> np.ndarray:
    ...


def rcs_to_signal(rcs, ranges):
    return rcs / ranges**2


def smooth_signal(signal, method="savgol", savgol_kwargs: dict | None = None):
    """Smooth Lidar Signal

    Args:
        signal ([type]): [description]
        method (str, optional): [description]. Defaults to 'savgol'.
    """

    if method == "savgol":
        if savgol_kwargs is None:
            savgol_kwargs = {"window_length": 21, "polyorder": 2}
        smoothed_signal = savgol_filter(signal, **savgol_kwargs)
    else:
        raise NotImplementedError(f"{method} has not been implemented yet")

    return smoothed_signal


def estimate_snr(signal, window=5):
    """[summary]

    Args:
        signal ([type]): [description]
    """

    # ventana: numero impar
    if window % 2 == 0:
        window += 1
    subw = window // 2

    n = len(signal)
    avg = np.zeros(n) * np.nan
    std = np.zeros(n) * np.nan

    for i in range(n):
        ind_delta_min = i - subw if i - subw >= 0 else 0
        ind_delta_max = i + subw if i + subw < n else n - 1

        si = signal[ind_delta_min : (ind_delta_max + 1)]
        avg[i] = np.nanmean(si)
        std[i] = np.nanstd(si)

        # print("%i, %i, %i" % (i, ind_delta_min, ind_delta_max + 1))
        # print(signal[ind_delta_min:(ind_delta_max+1)])
    snr = avg / std

    return snr, avg, std


def get_lidar_name_from_filename(fn):
    """Get Lidar System Name from L1a File Name
    Args:
        fn (function): [description]
    """
    lidar_nick = os.path.basename(fn).split("_")[0]
    if lidar_nick in LIDAR_INFO["metadata"]["nick2name"].keys():
        lidar = lidar_nick
    else:
        lidar = None
    return lidar


def sigmoid(x, x0, k, coeff: float = 1, offset: float = 0):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return (coeff * y) + offset


def extrapolate_beta_with_angstrom(
    beta_ref: np.ndarray,
    wavelength_ref: float,
    wavelength_target: float,
    angstrom_exponent: float | np.ndarray,
) -> np.ndarray:
    return beta_ref * (wavelength_target / wavelength_ref) ** -angstrom_exponent


def integrate_from_reference(integrand, x, reference_index):
    """

    at x[ref_index], the integral equals = 0
    """
    # integrate above reference
    int_above_ref = cumtrapz(integrand[reference_index:], x=x[reference_index:])

    # integrate below reference
    int_below_ref = cumtrapz(
        integrand[: reference_index + 1][::-1], x=x[: reference_index + 1][::-1]
    )[::-1]

    return np.concatenate([int_below_ref, np.zeros(1), int_above_ref])


def optical_depth(extinction, height, ref_index=0):
    """
    Integrate extinction profile along height: r'$\tau(z) = \int_0^z d\dseta \alpha(\dseta)$'
    """

    return integrate_from_reference(extinction, height, reference_index=ref_index)

def refill_overlap(
    atmospheric_profile: np.ndarray[Any, np.dtype[np.float64]],
    height: np.ndarray[Any, np.dtype[np.float64]],
    fulloverlap_height: float = 600,
    fill_with: float | None = None,
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """Fill overlap region [0-`fulloverlap_height`] of the profile `atmospheric_profile` with the value `fill_with` provided by the user. If None, fill with the value at `fulloverlap_height`.

    Args:
        atmospheric_profile (np.ndarray): Atmospheric profile
        height (np.ndarray): Range profile in meters
        fulloverlap_height (float, optional): Fulloverlap height in meters. Defaults to 600 m.
        fill_with (float, optional): Value to fill the overlap region. Defaults to None.

    Returns:
        np.ndarray: Profile `atmospheric_profile` with the overlap region filled.
    """
    if fulloverlap_height < height[0] or fulloverlap_height > height[-1]:
        raise ValueError(
            "The fulloverlap_height is outside the range of height values."
        )

    idx_overlap = np.abs(height - fulloverlap_height).argmin()

    if fill_with is None:
        fill_with = atmospheric_profile[idx_overlap]

    new_profile = np.copy(atmospheric_profile)
    new_profile[:idx_overlap] = fill_with

    return new_profile

def unzip_file_to_temp(file_path):
    # Create a temporary directory
    temp_dir = Path(tempfile.mkdtemp())

    try:
        # Extract the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Return the path to the extracted files
        return temp_dir

    except zipfile.BadZipFile:
        print("Error: The file is not a valid zip file.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Clean up the temporary directory
        if temp_dir.exists():
            temp_dir.rmdir()