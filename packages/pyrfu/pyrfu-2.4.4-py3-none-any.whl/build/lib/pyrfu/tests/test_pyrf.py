#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Built-in imports
import datetime
import unittest

# 3rd party imports
import numpy as np
import xarray as xr

from pyrfu import pyrf

__author__ = "Louis Richard"
__email__ = "louisr@irfu.se"
__copyright__ = "Copyright 2020-2023"
__license__ = "MIT"
__version__ = "2.4.2"
__status__ = "Prototype"


def generate_timeline(f_s, n_pts: int = 10000):
    ref_time = np.datetime64("2019-01-01T00:00:00.000")
    times = [ref_time + np.timedelta64(int(i * 1e9 / f_s), "ns") for i in range(n_pts)]
    return np.array(times)


def generate_data(n_pts, kind: str = "scalar"):
    if kind == "scalar":
        data = np.random.random((n_pts,))
    elif kind == "vector":
        data = np.random.random((n_pts, 3))
    elif kind == "tensor":
        data = np.random.random((n_pts, 3, 3))
    else:
        raise ValueError("Invalid kind of data!!")

    return data


def generate_ts(f_s, n_pts, kind: str = "scalar"):
    if kind == "scalar":
        out = pyrf.ts_scalar(generate_timeline(f_s, n_pts), generate_data(n_pts, kind))
    elif kind == "vector":
        out = pyrf.ts_vec_xyz(generate_timeline(f_s, n_pts), generate_data(n_pts, kind))
    elif kind == "tensor":
        out = pyrf.ts_tensor_xyz(
            generate_timeline(f_s, n_pts), generate_data(n_pts, kind)
        )
    else:
        raise ValueError("Invalid kind of data!!")

    return out


def generate_ts_scalar(f_s, n_pts):
    return pyrf.ts_scalar(generate_timeline(f_s, n_pts), generate_data(n_pts, "vector"))


class AutoCorrTestCase(unittest.TestCase):
    def test_autocorr_input_type(self):
        self.assertIsNotNone(pyrf.autocorr(generate_ts(64.0, 100, "scalar")))
        self.assertIsNotNone(pyrf.autocorr(generate_ts(64.0, 100, "scalar"), 25))
        self.assertIsNotNone(pyrf.autocorr(generate_ts(64.0, 100, "scalar"), 25, True))

    def test_autocorr_input_shape(self):
        self.assertIsNotNone(pyrf.autocorr(generate_ts(64.0, 100, "scalar")))
        self.assertIsNotNone(pyrf.autocorr(generate_ts(64.0, 100, "vector")))

    def test_autocorr_input_values(self):
        with self.assertRaises(ValueError):
            pyrf.autocorr(generate_ts(64.0, 100, "scalar"), 100)

    def test_autocorr_output_type(self):
        self.assertIsInstance(
            pyrf.autocorr(generate_ts(64.0, 100, "scalar")), xr.DataArray
        )
        self.assertIsInstance(
            pyrf.autocorr(generate_ts(64.0, 100, "vector")), xr.DataArray
        )

    def test_autocorr_output_shape(self):
        result = pyrf.autocorr(generate_ts(64.0, 100, "scalar"))
        self.assertEqual(result.ndim, 1)
        self.assertEqual(result.shape[0], 100)

        result = pyrf.autocorr(generate_ts(64.0, 100, "scalar"), 25)
        self.assertEqual(result.ndim, 1)
        self.assertEqual(result.shape[0], 26)

        result = pyrf.autocorr(generate_ts(64.0, 100, "vector"))
        self.assertEqual(result.ndim, 2)
        self.assertEqual(result.shape[0], 100)
        self.assertEqual(result.shape[1], 3)


class TsSkymapTestCase(unittest.TestCase):
    def test_ts_skymap_input_type(self):
        with self.assertRaises(AssertionError):
            pyrf.ts_skymap(0, 0, 0, 0, 0)

    def test_ts_skymap_output_type(self):
        result = pyrf.ts_skymap(
            generate_timeline(64.0, 100),
            np.random.random((100, 32, 32, 16)),
            np.random.random((100, 32)),
            np.random.random((100, 32)),
            np.random.random(16),
        )
        self.assertIsInstance(result, xr.Dataset)

    def test_ts_skymap_output_shape(self):
        result = pyrf.ts_skymap(
            generate_timeline(64.0, 100),
            np.random.random((100, 32, 32, 16)),
            np.random.random((100, 32)),
            np.random.random((100, 32)),
            np.random.random(16),
        )
        self.assertEqual(result.data.ndim, 4)
        self.assertListEqual(list(result.data.shape), [100, 32, 32, 16])
        self.assertEqual(result.energy.ndim, 2)
        self.assertListEqual(list(result.energy.shape), [100, 32])
        self.assertEqual(result.phi.ndim, 2)
        self.assertListEqual(list(result.phi.shape), [100, 32])
        self.assertEqual(result.theta.ndim, 1)
        self.assertListEqual(list(result.theta.shape), [16])

    def test_ts_skymap_output_meta(self):
        result = pyrf.ts_skymap(
            generate_timeline(64.0, 100),
            np.random.random((100, 32, 32, 16)),
            np.random.random((100, 32)),
            np.random.random((100, 32)),
            np.random.random(16),
        )
        self.assertListEqual(
            list(result.attrs.keys()), ["energy0", "energy1", "esteptable"]
        )
        self.assertListEqual(
            list(result.attrs["energy0"].shape),
            [
                32,
            ],
        )
        self.assertListEqual(
            list(result.attrs["energy1"].shape),
            [
                32,
            ],
        )
        self.assertListEqual(
            list(result.attrs["esteptable"].shape),
            [
                100,
            ],
        )

        for k in result:
            self.assertEqual(result[k].attrs, {})


class StartTestCase(unittest.TestCase):
    def test_start_input_type(self):
        self.assertIsNotNone(pyrf.start(generate_ts(64.0, 100, "scalar")))
        self.assertIsNotNone(pyrf.start(generate_ts(64.0, 100, "vector")))
        self.assertIsNotNone(pyrf.start(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            pyrf.start(0)
            pyrf.start(generate_timeline(64.0, 100))

    def test_start_output(self):
        result = pyrf.start(generate_ts(64.0, 100, "scalar"))
        self.assertIsInstance(result, np.float64)
        self.assertEqual(
            np.datetime64(int(result * 1e9), "ns"),
            np.datetime64("2019-01-01T00:00:00.000"),
        )


class TsScalarTestCase(unittest.TestCase):
    def test_ts_scalar_input_type(self):
        with self.assertRaises(AssertionError):
            pyrf.ts_scalar(0, 0)
            pyrf.ts_scalar(
                list(generate_timeline(64.0, 100)), list(generate_data(100, "scalar"))
            )

    def test_ts_scalar_input_shape(self):
        with self.assertRaises(AssertionError):
            # Raises error if data and timeline don't have the same size
            pyrf.ts_scalar(generate_timeline(64.0, 100), generate_data(99, "scalar"))
            # Raises error if vector as input
            pyrf.ts_scalar(generate_timeline(64.0, 100), generate_data(100, "vector"))
            # Raises error if tensor as input
            pyrf.ts_scalar(generate_timeline(64.0, 100), generate_data(100, "tensor"))

    def test_ts_scalar_output_type(self):
        result = pyrf.ts_scalar(
            generate_timeline(64.0, 100), generate_data(100, "scalar")
        )
        self.assertIsInstance(result, xr.DataArray)

    def test_ts_scalar_output_shape(self):
        result = pyrf.ts_scalar(
            generate_timeline(64.0, 100), generate_data(100, "scalar")
        )
        self.assertEqual(result.ndim, 1)
        self.assertEqual(len(result), 100)

    def test_ts_scalar_dims(self):
        result = pyrf.ts_scalar(
            generate_timeline(64.0, 100), generate_data(100, "scalar")
        )
        self.assertListEqual(list(result.dims), ["time"])

    def test_ts_scalar_meta(self):
        result = pyrf.ts_scalar(
            generate_timeline(64.0, 100), generate_data(100, "scalar")
        )
        self.assertEqual(result.attrs["TENSOR_ORDER"], 0)


class TsVecXYZTestCase(unittest.TestCase):
    def test_ts_vec_xyz_input_type(self):
        with self.assertRaises(AssertionError):
            pyrf.ts_vec_xyz(0, 0)
            pyrf.ts_vec_xyz(
                list(generate_timeline(64.0, 100)), list(generate_data(100, "vector"))
            )

    def test_ts_vec_xyz_input_shape(self):
        with self.assertRaises(AssertionError):
            # Raises error if data and timeline don't have the same size
            pyrf.ts_vec_xyz(generate_timeline(64.0, 100), generate_data(99, "vector"))
            # Raises error if vector as input
            pyrf.ts_vec_xyz(generate_timeline(64.0, 100), generate_data(100, "scalar"))
            # Raises error if tensor as input
            pyrf.ts_vec_xyz(generate_timeline(64.0, 100), generate_data(100, "tensor"))

    def test_ts_vec_xyz_output_type(self):
        result = pyrf.ts_vec_xyz(
            generate_timeline(64.0, 100), generate_data(100, "vector")
        )
        self.assertIsInstance(result, xr.DataArray)

    def test_ts_vec_xyz_output_shape(self):
        result = pyrf.ts_vec_xyz(
            generate_timeline(64.0, 100), generate_data(100, "vector")
        )
        self.assertEqual(result.ndim, 2)
        self.assertEqual(result.shape[0], 100)
        self.assertEqual(result.shape[1], 3)

    def test_ts_vec_xyz_dims(self):
        result = pyrf.ts_vec_xyz(
            generate_timeline(64.0, 100), generate_data(100, "vector")
        )
        self.assertListEqual(list(result.dims), ["time", "comp"])

    def test_ts_vec_xyz_meta(self):
        result = pyrf.ts_vec_xyz(
            generate_timeline(64.0, 100), generate_data(100, "vector")
        )
        self.assertEqual(result.attrs["TENSOR_ORDER"], 1)


class TsTensorXYZTestCase(unittest.TestCase):
    def test_ts_tensor_xyz_input_type(self):
        with self.assertRaises(AssertionError):
            pyrf.ts_tensor_xyz(0, 0)
            pyrf.ts_tensor_xyz(
                list(generate_timeline(64.0, 100)), list(generate_data(100, "tensor"))
            )

    def test_ts_tensor_xyz_input_shape(self):
        with self.assertRaises(AssertionError):
            # Raises error if data and timeline don't have the same size
            pyrf.ts_tensor_xyz(
                generate_timeline(64.0, 100), generate_data(99, "tensor")
            )
            # Raises error if vector as input
            pyrf.ts_tensor_xyz(
                generate_timeline(64.0, 100), generate_data(100, "scalar")
            )
            # Raises error if tensor as input
            pyrf.ts_tensor_xyz(
                generate_timeline(64.0, 100), generate_data(100, "vector")
            )

    def test_ts_tensor_xyz_output_type(self):
        result = pyrf.ts_tensor_xyz(
            generate_timeline(64.0, 100), generate_data(100, "tensor")
        )
        self.assertIsInstance(result, xr.DataArray)

    def test_ts_tensor_xyz_output_shape(self):
        result = pyrf.ts_tensor_xyz(
            generate_timeline(64.0, 100), generate_data(100, "tensor")
        )
        self.assertEqual(result.ndim, 3)
        self.assertEqual(result.shape[0], 100)
        self.assertEqual(result.shape[1], 3)
        self.assertEqual(result.shape[2], 3)

    def test_ts_tensor_xyz_dims(self):
        result = pyrf.ts_tensor_xyz(
            generate_timeline(64.0, 100), generate_data(100, "tensor")
        )
        self.assertListEqual(list(result.dims), ["time", "comp_h", "comp_v"])

    def test_ts_tensor_xyz_meta(self):
        result = pyrf.ts_tensor_xyz(
            generate_timeline(64.0, 100), generate_data(100, "tensor")
        )
        self.assertEqual(result.attrs["TENSOR_ORDER"], 2)


class CalcFsTestCase(unittest.TestCase):
    def test_calc_fs_input_type(self):
        self.assertIsNotNone(pyrf.calc_fs(generate_ts(64.0, 100)))

        with self.assertRaises(AssertionError):
            # Raises error if input is not a xarray
            pyrf.calc_fs(0)
            pyrf.calc_fs(generate_data(100))

    def test_calc_fs_output_type(self):
        self.assertIsInstance(pyrf.calc_fs(generate_ts(64.0, 100)), float)


class CalcDtTestCase(unittest.TestCase):
    def test_calc_dt_input_type(self):
        self.assertIsNotNone(pyrf.calc_dt(generate_ts(64.0, 100, "scalar")))
        self.assertIsNotNone(pyrf.calc_dt(generate_ts(64.0, 100, "vector")))
        self.assertIsNotNone(pyrf.calc_dt(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            # Raises error if input is not a xarray
            pyrf.calc_dt(0)
            pyrf.calc_dt(generate_data(100))

    def test_calc_dt_output_type(self):
        self.assertIsInstance(pyrf.calc_dt(generate_ts(64.0, 100)), float)


class CalcAgTestCase(unittest.TestCase):
    def test_calc_ag_input_type(self):
        self.assertIsNotNone(pyrf.calc_ag(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            # Raises error if input is not a xarray
            pyrf.calc_ag(0.0)
            pyrf.calc_ag(generate_data(100))

    def test_calc_ag_output_type(self):
        result = pyrf.calc_ag(generate_ts(64.0, 100, "tensor"))

        # Output must be a xarray
        self.assertIsInstance(result, xr.DataArray)

    def test_calc_ag_output_shape(self):
        result = pyrf.calc_ag(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.ndim, 1)
        self.assertEqual(len(result), 100)

    def test_calc_ag_dims(self):
        result = pyrf.calc_ag(generate_ts(64.0, 100, "tensor"))
        self.assertListEqual(list(result.dims), ["time"])

    def test_calc_ag_meta(self):
        result = pyrf.calc_ag(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.attrs["TENSOR_ORDER"], 0)


class CalcAgyroTestCase(unittest.TestCase):
    def test_calc_agyro_input_type(self):
        self.assertIsNotNone(pyrf.calc_agyro(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            # Raises error if input is not a xarray
            pyrf.calc_agyro(0.0)
            pyrf.calc_agyro(generate_data(100))

    def test_calc_agyro_output_type(self):
        result = pyrf.calc_agyro(generate_ts(64.0, 100, "tensor"))

        # Output must be a xarray
        self.assertIsInstance(result, xr.DataArray)

    def test_calc_agyro_output_shape(self):
        result = pyrf.calc_agyro(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.ndim, 1)
        self.assertEqual(len(result), 100)

    def test_calc_agyro_dims(self):
        result = pyrf.calc_agyro(generate_ts(64.0, 100, "tensor"))
        self.assertListEqual(list(result.dims), ["time"])

    def test_calc_agyro_meta(self):
        result = pyrf.calc_agyro(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.attrs["TENSOR_ORDER"], 0)


class CalcDngTestCase(unittest.TestCase):
    def test_calc_dng_input_type(self):
        self.assertIsNotNone(pyrf.calc_dng(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            # Raises error if input is not a xarray
            pyrf.calc_dng(0.0)
            pyrf.calc_dng(generate_data(100))

    def test_calc_dng_output_type(self):
        result = pyrf.calc_dng(generate_ts(64.0, 100, "tensor"))

        # Output must be a xarray
        self.assertIsInstance(result, xr.DataArray)

    def test_calc_dng_output_shape(self):
        result = pyrf.calc_dng(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.ndim, 1)
        self.assertEqual(len(result), 100)

    def test_calc_dng_dims(self):
        result = pyrf.calc_dng(generate_ts(64.0, 100, "tensor"))
        self.assertListEqual(list(result.dims), ["time"])

    def test_calc_dng_meta(self):
        result = pyrf.calc_dng(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.attrs["TENSOR_ORDER"], 0)


class CalcSqrtQTestCase(unittest.TestCase):
    def test_calc_sqrtq_input_type(self):
        self.assertIsNotNone(pyrf.calc_sqrtq(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            # Raises error if input is not a xarray
            pyrf.calc_sqrtq(0.0)
            pyrf.calc_sqrtq(generate_data(100))

    def test_calc_sqrtq_output_type(self):
        result = pyrf.calc_sqrtq(generate_ts(64.0, 100, "tensor"))

        # Output must be a xarray
        self.assertIsInstance(result, xr.DataArray)

    def test_calc_sqrtq_output_shape(self):
        result = pyrf.calc_sqrtq(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.ndim, 1)
        self.assertEqual(len(result), 100)

    def test_calc_sqrtq_dims(self):
        result = pyrf.calc_sqrtq(generate_ts(64.0, 100, "tensor"))
        self.assertListEqual(list(result.dims), ["time"])

    def test_calc_sqrtq_meta(self):
        result = pyrf.calc_sqrtq(generate_ts(64.0, 100, "tensor"))
        self.assertEqual(result.attrs["TENSOR_ORDER"], 0)


class CdfEpoch2Datetime64TestCase(unittest.TestCase):
    def test_cdfepoch2datetime64_input_type(self):
        ref_time = 599572869184000000
        self.assertIsNotNone(pyrf.cdfepoch2datetime64(ref_time))
        time_line = np.arange(ref_time, int(ref_time + 100))
        self.assertIsNotNone(pyrf.cdfepoch2datetime64(time_line))
        self.assertIsNotNone(pyrf.cdfepoch2datetime64(list(time_line)))

    def test_cdfepoch2datetime64_output_type(self):
        ref_time = 599572869184000000
        self.assertIsInstance(pyrf.cdfepoch2datetime64(ref_time), np.ndarray)
        time_line = np.arange(ref_time, int(ref_time + 100))
        self.assertIsInstance(pyrf.cdfepoch2datetime64(time_line), np.ndarray)
        self.assertIsInstance(pyrf.cdfepoch2datetime64(list(time_line)), np.ndarray)

    def test_cdfepoch2datetime64_output_shape(self):
        ref_time = 599572869184000000
        self.assertEqual(len(pyrf.cdfepoch2datetime64(ref_time)), 1)
        time_line = np.arange(ref_time, int(ref_time + 100))
        self.assertEqual(len(pyrf.cdfepoch2datetime64(time_line)), 100)
        self.assertEqual(len(pyrf.cdfepoch2datetime64(list(time_line))), 100)


class Datetime2Iso8601TestCase(unittest.TestCase):
    def test_datetime2iso8601_input_type(self):
        ref_time = datetime.datetime(2019, 1, 1, 0, 0, 0, 0)
        time_line = [ref_time + datetime.timedelta(seconds=i) for i in range(10)]
        self.assertIsNotNone(pyrf.datetime2iso8601(ref_time))
        self.assertIsNotNone(pyrf.datetime2iso8601(time_line))

    def test_datetime2iso8601_output_type(self):
        ref_time = datetime.datetime(2019, 1, 1, 0, 0, 0, 0)
        time_line = [ref_time + datetime.timedelta(seconds=i) for i in range(10)]
        self.assertIsInstance(pyrf.datetime2iso8601(ref_time), str)
        self.assertIsInstance(pyrf.datetime2iso8601(time_line), list)

    def test_datetime2iso8601_output_shape(self):
        ref_time = datetime.datetime(2019, 1, 1, 0, 0, 0, 0)
        time_line = [ref_time + datetime.timedelta(seconds=i) for i in range(10)]

        # ISO8601 contains 29 characters (nanosecond precision)
        self.assertEqual(len(pyrf.datetime2iso8601(ref_time)), 29)
        self.assertEqual(len(pyrf.datetime2iso8601(time_line)), 10)


class TraceTestCase(unittest.TestCase):
    def test_trace_input(self):
        self.assertIsNotNone(pyrf.trace(generate_ts(64.0, 100, "tensor")))

        with self.assertRaises(AssertionError):
            pyrf.trace(generate_data(100, "tensor"))
            pyrf.trace(generate_ts(64.0, 100, "scalar"))
            pyrf.trace(generate_ts(64.0, 100, "vector"))

    def test_trace_output(self):
        result = pyrf.trace(generate_ts(64.0, 100, "tensor"))
        self.assertIsInstance(result, xr.DataArray)
        self.assertListEqual(
            list(result.shape),
            [
                100,
            ],
        )


class Avg4SCTestCase(unittest.TestCase):
    def test_avg_4sc_input(self):
        self.assertIsNotNone(
            pyrf.avg_4sc(
                [
                    generate_ts(64.0, 100, "scalar"),
                    generate_ts(64.0, 100, "scalar"),
                    generate_ts(64.0, 100, "scalar"),
                    generate_ts(64.0, 100, "scalar"),
                ]
            )
        )
        self.assertIsNotNone(
            pyrf.avg_4sc(
                [
                    generate_ts(64.0, 100, "vector"),
                    generate_ts(64.0, 100, "vector"),
                    generate_ts(64.0, 100, "vector"),
                    generate_ts(64.0, 100, "vector"),
                ]
            )
        )
        self.assertIsNotNone(
            pyrf.avg_4sc(
                [
                    generate_ts(64.0, 100, "tensor"),
                    generate_ts(64.0, 100, "tensor"),
                    generate_ts(64.0, 100, "tensor"),
                    generate_ts(64.0, 100, "tensor"),
                ]
            )
        )

        with self.assertRaises(TypeError):
            pyrf.avg_4sc(
                [
                    generate_data(100, "tensor"),
                    generate_data(100, "tensor"),
                    generate_data(100, "tensor"),
                    generate_data(100, "tensor"),
                ]
            )

    def test_avg_4sc_output(self):
        result = pyrf.avg_4sc(
            [
                generate_ts(64.0, 100, "tensor"),
                generate_ts(64.0, 100, "tensor"),
                generate_ts(64.0, 100, "tensor"),
                generate_ts(64.0, 100, "tensor"),
            ]
        )

        self.assertIsInstance(result, xr.DataArray)
        self.assertListEqual(list(result.shape), [100, 3, 3])


if __name__ == "__main__":
    unittest.main()
