import numpy as np
from numpy.testing import assert_almost_equal as almost
import unittest
import os.path

import MulensModel as mm

dir_1 = os.path.join(mm.DATA_PATH, 'photometry_files', 'OB140939')
dir_2 = os.path.join(mm.DATA_PATH, 'unit_test_files')
dir_3 = os.path.join(mm.DATA_PATH, 'ephemeris_files')

SAMPLE_FILE_02 = os.path.join(dir_1, 'ob140939_OGLE.dat')  # HJD'
SAMPLE_FILE_02_REF = os.path.join(dir_2, 'ob140939_OGLE_ref_v1.dat')  # HJD'
SAMPLE_FILE_03 = os.path.join(dir_1, 'ob140939_Spitzer.dat')  # HJD'
SAMPLE_FILE_03_EPH = os.path.join(dir_3, 'Spitzer_ephemeris_01.dat')  # UTC
SAMPLE_FILE_03_REF = os.path.join(dir_2, 'ob140939_Spitzer_ref_v1.dat')  # HJD'
SAMPLE_FILE_04_WF = os.path.join(mm.DATA_PATH, 'WFIRST_1827.dat')

# Note: default precision for assert_almost_equal (aka almost) is decimal = 7


def generate_model():
    """
    returns a model, time array, and magnification
    """

    # Create a PSPL model
    t_0 = 3583.
    u_0 = 0.3
    t_E = 12.

    t = np.linspace(t_0 - 3. * t_E, t_0 + 3. * t_E, 1000)
    pspl = mm.Model({'t_0': t_0, 'u_0': u_0, 't_E': t_E})
    A = pspl.get_magnification(t)

    return (pspl, t, A)


def generate_binary_model():
    """
    returns a binary source model, time array, and the magnification of
    both sources
    """

    # retrieve model 1
    (model_1, t, A_1) = generate_model()
    t_0_1 = model_1.parameters.t_0
    u_0_1 = model_1.parameters.u_0

    # create second model
    t_0_2 = 3570.
    u_0_2 = 0.25
    t_E = model_1.parameters.t_E

    model_2 = mm.Model({'t_0': t_0_2, 'u_0': u_0_2, 't_E': t_E})

    A_2 = model_2.get_magnification(t)

    # create separate binary model
    params = {'t_0_1': t_0_1, 'u_0_1': u_0_1, 't_0_2': t_0_2, 'u_0_2': u_0_2,
              't_E': t_E}
    binary_model = mm.Model(params)

    return (binary_model, t, A_1, A_2)


def generate_dataset(f_mod, t):
    """
    pass in f_mod and t, returns a MulensData
    """

    # error in measurement
    err = f_mod * 0.01

    my_dataset = mm.MulensData(data_list=[t, f_mod, err], phot_fmt='flux')

    return my_dataset


class TestSingleSourceFluxes(unittest.TestCase):

    def setUp(self):
        self.pspl, self.t, self.magnification = generate_model()

        # secrets
        self.f_s = 1.0
        self.f_b = 0.5
        # generate f_mod
        self.f_mod = self.f_s * self.magnification + self.f_b

        self.my_dataset = generate_dataset(self.f_mod, self.t)

    def _run_true_values_test(
            self, fix_source_flux=False, fix_blend_flux=False):
        my_fit = mm.FitData(
            model=self.pspl, dataset=self.my_dataset,
            fix_blend_flux=fix_blend_flux, fix_source_flux=fix_source_flux)
        my_fit.fit_fluxes()

        almost(my_fit.blend_flux, self.f_b)
        almost(my_fit.source_flux, self.f_s)

        # Test get_model_fluxes() for 1 source
        peak_index = 500
        mod_fluxes = my_fit.get_model_fluxes()
        almost(mod_fluxes[peak_index], self.my_dataset.flux[peak_index])

    def _run_arbitrary_values_test(
            self, fix_source_flux=False, fix_blend_flux=False):
        my_fit = mm.FitData(
            model=self.pspl, dataset=self.my_dataset,
            fix_blend_flux=fix_blend_flux, fix_source_flux=fix_source_flux)
        my_fit.fit_fluxes()

        if fix_blend_flux is not False:
            almost(my_fit.blend_flux, fix_blend_flux)

        if fix_source_flux is not False:
            almost(my_fit.source_flux, fix_source_flux)

    def test_all_free(self):
        self._run_true_values_test()
        self._run_true_values_test(fix_source_flux=False, fix_blend_flux=False)

    def test_fixed_blending(self):
        self._run_true_values_test(fix_blend_flux=0.5)
        self._run_arbitrary_values_test(fix_blend_flux=0.)
        self._run_arbitrary_values_test(fix_blend_flux=0.23)
        self._run_arbitrary_values_test(fix_blend_flux=-0.23)

    def test_fixed_source_flux(self):
        self._run_true_values_test(fix_source_flux=1.0)
        self._run_arbitrary_values_test(fix_source_flux=0.)
        self._run_arbitrary_values_test(fix_source_flux=0.23)
        self._run_arbitrary_values_test(fix_source_flux=-0.23)

    def test_all_fixed(self):
        self._run_true_values_test(fix_source_flux=1.0, fix_blend_flux=0.5)
        self._run_arbitrary_values_test(
            fix_source_flux=1.2, fix_blend_flux=-0.5)
        self._run_arbitrary_values_test(fix_source_flux=1.7, fix_blend_flux=0.)


class TestBinarySourceFluxes(unittest.TestCase):

    def setUp(self):
        self.f_s_1 = 1
        self.f_s_2 = 1.2
        self.f_b = 0.5

        self.model, self.t, self.A_1, self.A_2 = generate_binary_model()
        f_mod = self.f_s_1 * self.A_1 + self.f_s_2 * self.A_2 + self.f_b
        self.dataset = generate_dataset(f_mod, self.t)

    def _run_true_value_test(
            self, fix_source_flux=False, fix_blend_flux=False):
        my_fit = mm.FitData(
            model=self.model, dataset=self.dataset,
            fix_source_flux=fix_source_flux, fix_blend_flux=fix_blend_flux)
        my_fit.update()
        almost(my_fit.blend_flux, self.f_b)
        almost(my_fit.source_fluxes[0], self.f_s_1)
        almost(my_fit.source_fluxes[1], self.f_s_2)

        peak_index = 500
        mod_fluxes = my_fit.get_model_fluxes()
        almost(mod_fluxes[peak_index], self.dataset.flux[peak_index])

        assert (my_fit.chi2_per_point.shape == (self.dataset.n_epochs, ))

    def _run_arbitrary_value_test(
            self, fix_source_flux=False, fix_blend_flux=False):
        my_fit = mm.FitData(
            model=self.model, dataset=self.dataset,
            fix_source_flux=fix_source_flux, fix_blend_flux=fix_blend_flux)
        my_fit.fit_fluxes()

        if fix_blend_flux is not False:
            almost(my_fit.blend_flux, fix_blend_flux)

        if fix_source_flux is not False:
            if fix_source_flux[0] is not False:
                almost(my_fit.source_fluxes[0], fix_source_flux[0])

            if fix_source_flux[1] is not False:
                almost(my_fit.source_fluxes[1], fix_source_flux[1])

    def _run_q_flux_test_true(self, fix_q_flux=False, fix_blend_flux=False):
        my_fit = mm.FitData(
            model=self.model, dataset=self.dataset,
            fix_source_flux_ratio=fix_q_flux, fix_blend_flux=fix_blend_flux)
        my_fit.fit_fluxes()

        almost(my_fit.blend_flux, self.f_b)
        almost(my_fit.source_fluxes[0], self.f_s_1)
        almost(my_fit.source_fluxes[1], self.f_s_2)

    def _run_q_flux_test_arbitrary(
            self, fix_q_flux=False, fix_blend_flux=False):
        my_fit = mm.FitData(
            model=self.model, dataset=self.dataset,
            fix_source_flux_ratio=fix_q_flux, fix_blend_flux=fix_blend_flux)
        my_fit.fit_fluxes()

        if fix_blend_flux is not False:
            almost(my_fit.blend_flux, fix_blend_flux)

        almost(
            my_fit.source_fluxes[1]/my_fit.source_fluxes[0],
            fix_q_flux)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self._run_true_value_test(fix_source_flux=1.0)

    def test_all_free(self):
        self._run_true_value_test()
        self._run_true_value_test(
            fix_source_flux=[False, False], fix_blend_flux=False)

    def test_fixed_source_true(self):
        self._run_true_value_test(
            fix_source_flux=[1., False], fix_blend_flux=False)
        self._run_true_value_test(
            fix_source_flux=[False, 1.2], fix_blend_flux=False)
        self._run_true_value_test(
            fix_source_flux=[1., 1.2], fix_blend_flux=False)

    def test_fixed_blend_true(self):
        self._run_true_value_test(fix_blend_flux=0.5)
        self._run_true_value_test(
            fix_source_flux=[1., False], fix_blend_flux=0.5)
        self._run_true_value_test(
            fix_source_flux=[False, 1.2], fix_blend_flux=0.5)

    def test_all_fixed_true(self):
        self._run_true_value_test(
            fix_source_flux=[1., 1.2], fix_blend_flux=0.5)

    def test_fixed_source_arbitrary(self):
        self._run_arbitrary_value_test(
            fix_source_flux=[1.2, False], fix_blend_flux=False)
        self._run_arbitrary_value_test(
            fix_source_flux=[False, 0.53], fix_blend_flux=False)
        self._run_arbitrary_value_test(
            fix_source_flux=[4.5, 0.67], fix_blend_flux=False)

    def test_fixed_blend_arbitrary(self):
        self._run_arbitrary_value_test(fix_blend_flux=0.)
        self._run_arbitrary_value_test(fix_blend_flux=2.3)
        self._run_arbitrary_value_test(fix_blend_flux=-0.5)
        self._run_arbitrary_value_test(
            fix_source_flux=[1.2, False], fix_blend_flux=0.78)
        self._run_arbitrary_value_test(
            fix_source_flux=[False, 0.53], fix_blend_flux=0.23)

    def test_all_fixed_arbitrary(self):
        self._run_arbitrary_value_test(
            fix_source_flux=[2.3, 0.45], fix_blend_flux=0.67)
        self._run_arbitrary_value_test(
            fix_source_flux=[2.3, 0.45], fix_blend_flux=0.)

    def test_q_flux_fixed(self):
        self._run_q_flux_test_true()
        self._run_q_flux_test_true(fix_q_flux=1.2)
        self._run_q_flux_test_true(fix_q_flux=1.2, fix_blend_flux=0.5)
        self._run_q_flux_test_arbitrary(fix_q_flux=2.1)
        self._run_q_flux_test_arbitrary(fix_q_flux=1.4, fix_blend_flux=0.25)
        self._run_q_flux_test_arbitrary(fix_q_flux=1.4, fix_blend_flux=0.)


def test_fit_fluxes():
    """
    test that when the model is updated, and fit fluxes is re-run, the fluxes
    actually change.
    """

    pspl, t, A = generate_model()

    # secret blend flux, set source flux
    f_s = 1.0
    f_b = 0.5
    f_mod = f_s * A + f_b

    my_dataset = generate_dataset(f_mod, t)
    my_fit = mm.FitData(
        model=pspl, dataset=my_dataset, fix_blend_flux=False,
        fix_source_flux=False)
    #   Before update or fit_fluxes is run, chi2_per_point should be None
    assert(my_fit.chi2_per_point is None)
    my_fit.update()
    #   After update is run, chi2_per_point should have some values
    assert (len(my_fit.chi2_per_point) == 1000)
    f_s_1 = my_fit.source_flux
    chi2_1 = my_fit.chi2

    t_E_2 = pspl.parameters.t_E / (f_s + f_b)
    u_0_2 = pspl.parameters.u_0 / (f_s + f_b)
    new_model = mm.Model(
        {'t_0': pspl.parameters.t_0, 'u_0': u_0_2, 't_E': t_E_2})
    my_fit.model = new_model
    my_fit.fix_blend_flux = 0.
    my_fit.fit_fluxes()

    assert(f_s_1 != my_fit.source_flux)
    assert(chi2_1 == my_fit.chi2)

    my_fit.update()
    assert(chi2_1 != my_fit.chi2)


def create_0939_parallax_model():
    """Create Model instance with parallax"""
    model_parameters = {
        't_0': 2456836.22, 'u_0': 0.922, 't_E': 22.87,
        'pi_E_N': -0.248, 'pi_E_E': 0.234, 't_0_par': 2456836.2}
    coords = "17:47:12.25 -21:22:58.2"
    model_with_par = mm.Model(model_parameters, coords=coords)
    model_with_par.parallax(satellite=True, earth_orbital=True,
                            topocentric=False)
    return model_with_par


def test_satellite_and_annual_parallax_calculation():
    """
    test that data magnifications are correctly retrieved for Spitzer data.
    """
    model_with_par = create_0939_parallax_model()

    # Load Spitzer data and answers
    data_Spitzer = mm.MulensData(
        file_name=SAMPLE_FILE_03, ephemerides_file=SAMPLE_FILE_03_EPH)
    ref_Spitzer = np.loadtxt(SAMPLE_FILE_03_REF, unpack=True, usecols=[5])

    # Test FitData.data_magnification()
    my_fit = mm.FitData(dataset=data_Spitzer, model=model_with_par)
    ratio = my_fit.get_data_magnification() / ref_Spitzer
    np.testing.assert_almost_equal(ratio, [1.]*len(ratio), decimal=4)


def test_get_d_u_d_params():
    """
    Test that calculating derivatives with an ephemeris file is different from
    without an ephemeris file.
    """
    parameters = ['pi_E_N', 'pi_E_E']
    model_with_par = create_0939_parallax_model()

    data_ephm = mm.MulensData(
        file_name=SAMPLE_FILE_03, ephemerides_file=SAMPLE_FILE_03_EPH)
    fit_ephm = mm.FitData(dataset=data_ephm, model=model_with_par)
    derivs_ephm = fit_ephm._get_d_u_d_params(parameters)

    data_no_ephm = mm.MulensData(file_name=SAMPLE_FILE_03)
    fit_no_ephm = mm.FitData(dataset=data_no_ephm, model=model_with_par)
    derivs_no_ephm = fit_no_ephm._get_d_u_d_params(parameters)

    for param in parameters:
        ratio = derivs_ephm[param] / derivs_no_ephm[param]
        assert (np.abs(ratio - 1.) > 0.001).all()


def test_bad_data():
    """
    test how chi2 and chi2_per_point are affected if some datapoints are set
    to bad.

    Effectively tests
        update()
        fit_fluxes()
        get_data_magnification()
        get_model_fluxes()
        chi2
        chi2_per_point

    """

    # test that chi2 changes when using all data points vs. eliminating the
    # planet.
    (t_planet_start, t_planet_stop) = (2460982., 2460985.)
    data = mm.MulensData(file_name=SAMPLE_FILE_04_WF)
    flag_planet = (data.time > t_planet_start) & (
        data.time < t_planet_stop) | np.isnan(data.err_mag)
    data_bad = mm.MulensData(file_name=SAMPLE_FILE_04_WF, bad=flag_planet)

    (t_0, u_0, t_E) = (2460962.36458, 0.411823, 22.8092)
    point_lens_model = mm.Model({'t_0': t_0, 'u_0': u_0, 't_E': t_E})
    fit_all = mm.FitData(dataset=data, model=point_lens_model)
    fit_bad = mm.FitData(dataset=data_bad, model=point_lens_model)
    assert(fit_all.chi2 is None)
    fit_all.update()
    fit_bad.update()
    chi2_all = fit_all.chi2
    chi2_bad = fit_bad.chi2
    assert(chi2_all > chi2_bad)

    # test whether chi2_per_point is calculated for bad points.
    # not calculated --> magnification = 0, model_flux --> f_blend, dchi2=large
    # update: bad not specified --> not calculated
    # Likewise, do these tests for get_model_magnitudes
    # points:
    #   during anomaly 13055
    #   before anomaly, but excluded: 12915
    #   before anomaly, but included: 12900
    good_pt = 12900
    bad_pt = 12915
    assert (fit_bad.chi2_per_point[bad_pt] / fit_bad.chi2_per_point[good_pt] >
            100.)
    expected_mag = mm.Utils.get_mag_from_flux(fit_bad.blend_flux)
    almost(fit_bad.get_model_magnitudes()[bad_pt], expected_mag)

    # update: bad=True --> calculated
    fit_bad.update(bad=True)
    assert (fit_bad.chi2_per_point[bad_pt] / fit_bad.chi2_per_point[good_pt] <
            10.)
    almost(fit_bad.get_model_magnitudes()[bad_pt], 19.27, decimal=1)

    # update: bad=False --> not calculated
    fit_bad.update(bad=False)
    assert (fit_bad.chi2_per_point[bad_pt] / fit_bad.chi2_per_point[good_pt] >
            100.)
    almost(fit_bad.get_model_magnitudes()[bad_pt], expected_mag)

    # Test fitted fluxes are different with and without bad data points.
    assert (fit_all.source_flux > fit_bad.source_flux)


def test_scale_fluxes():
    """Specify a source_flux, blend_flux and make sure it works"""

    # Original Flux values
    f_s = 1.0
    f_b = 0.5

    # Generate fake data from a fake model
    pspl, t, A = generate_model()
    f_mod = f_s * A + f_b
    data = generate_dataset(f_mod, t)

    fit = mm.FitData(dataset=data, model=pspl)
    fit.fit_fluxes()

    num = 100
    # Test the same
    (new_flux, new_err) = fit.scale_fluxes(source_flux=f_s, blend_flux=f_b)
    almost(data.flux[num], new_flux[num])

    # Test Different
    (f_s_new, f_b_new) = (0.1, 0.)
    exp_flux = (data.flux - f_b) * f_s_new / f_s + f_b_new
    exp_err = data.err_flux * f_s_new / f_s
    (new_flux, new_err) = fit.scale_fluxes(
        source_flux=f_s_new, blend_flux=f_b_new)
    assert np.abs(data.flux[num] - new_flux[num]) > 0.5
    almost(exp_flux / new_flux, 1.)
    almost(exp_err / new_err, 1.)


class TestGetResiduals(unittest.TestCase):
    """
    test get_residuals():
    Test all keywords:
        phot_fmt: 'mag', 'flux'
        phot_fmt: 'scaled' and source_flux, blend_flux specified
        bad: True, False
    test values of residuals and errorbars
    """

    def setUp(self):
        self.model = mm.Model(
            {'t_0': 8000., 'u_0': 0.3, 't_E': 25.})
        self.generate_fake_dataset()
        self.fit = mm.FitData(model=self.model, dataset=self.dataset)
        self.fit.fit_fluxes()

    def generate_fake_dataset(self):
        """
        create a fake, perfect dataset, but with a few known outliers and
        errorbar variations.
        """
        self.dataset_properties = {
            'f_source': 10, 'f_blend': 3.5, 'errorbar': 1.}

        # Generate perfect data
        n = 3
        dt = 1.0
        times = np.arange(
            self.model.parameters.t_0 - n * self.model.parameters.t_E,
            self.model.parameters.t_0 + n * self.model.parameters.t_E,
            dt)
        flux = (self.dataset_properties['f_source'] *
                self.model.get_magnification(times) +
                self.dataset_properties['f_blend'])
        err = np.zeros(len(times)) + self.dataset_properties['errorbar']
        bad = np.zeros(len(times), dtype=bool)

        # Add outliers
        self.outliers = {'index': np.arange(0, len(times)-5, 10)+3}
        self.outliers['values'] = 10 + np.zeros(len(self.outliers['index']))
        for i in np.arange(len(self.outliers['index'])):
            if i % 5 == 0:
                self.outliers['values'][i] *= -1

            flux[self.outliers['index'][i]] += self.outliers['values'][i]
            bad[self.outliers['index'][i]] = True

        # Add errorbar variations
        self.big_errors = {'index': np.arange(0, len(times)-6, 21) + 4}
        self.big_errors['values'] = 5. + np.zeros(
            len(self.big_errors['index']))
        for i in np.arange(len(self.big_errors['index'])):
            err[self.big_errors['index'][i]] = self.big_errors['values'][i]

        assert np.sum(err) > len(err) * self.dataset_properties['errorbar']

        # Create final dataset
        self.dataset = mm.MulensData(
            [times, flux, err], phot_fmt='flux', bad=bad)

    def test_bad_keyword(self):
        """
        If bad = False, the magnification should be zero. Therefore, the flux
        calculated for the bad data points should be f_blend. If bad=True,
        the values should be the true values of the residuals.
        """
        # Bad = False
        (residuals, res_errors) = self.fit.get_residuals(
            phot_fmt='flux', bad=False)

        for index in self.outliers['index']:
            exp_residual = (self.dataset.flux[index] -
                            self.dataset_properties['f_blend'])
            almost(residuals[index], exp_residual)

        # Check errorbars
        almost(res_errors, self.dataset.err_flux)

        # Bad = True
        (residuals, res_errors) = self.fit.get_residuals(
            phot_fmt='flux', bad=True)

        for i, index in enumerate(self.outliers['index']):
            exp_residual = self.outliers['values'][i]
            almost(residuals[index], exp_residual)

        # Check errorbars
        almost(res_errors, self.dataset.err_flux)

    def test_photfmt_mag(self):
        """ check phot_fmt = 'mag' ."""
        # Bad = True
        (residuals, res_errors) = self.fit.get_residuals(
            phot_fmt='mag', bad=True)

        # Simple sign check
        for i, index in enumerate(self.outliers['index']):
            if self.outliers['values'][i] > 0:
                assert residuals[index] < 0
            else:
                assert residuals[index] > 0

        # Value check
        for i in np.arange(len(self.dataset.time)):
            if i in self.outliers['index']:
                index = np.where(self.outliers['index'] == i)
                f_0 = self.dataset.flux[i] - self.outliers['values'][index]
                f_obs = self.dataset.flux[i]
                delta_mag = -2.5*np.log10(f_obs / f_0)
                almost(delta_mag, residuals[i])
            else:
                # Non-outliers should have zero residual
                almost(residuals[i], 0)

        # Check errorbars
        almost(res_errors, self.dataset.err_mag)

    def test_photfmt_scaled_1(self):
        """ check phot_fmt='scaled' """
        f_source_0 = 1.0
        f_blend_0 = 0.1

        # Bad = True
        (residuals, res_errors) = self.fit.get_residuals(
            phot_fmt='scaled', source_flux=f_source_0, blend_flux=f_blend_0,
            bad=True)

        model_flux = (f_source_0 *
                      self.model.get_magnification(self.dataset.time) +
                      f_blend_0)
        model_mag = mm.Utils.get_mag_from_flux(model_flux)
        for i in np.arange(len(self.dataset.time)):
            exp_flux = (f_source_0 *
                        (self.dataset.flux[i] -
                         self.dataset_properties['f_blend']) /
                        self.dataset_properties['f_source'] + f_blend_0)
            if i in self.outliers['index']:
                exp_mag = mm.Utils.get_mag_from_flux(exp_flux)
                exp_delta_mag = exp_mag - model_mag[i]
                almost(exp_delta_mag, residuals[i])
            else:
                # Non-outliers should have zero residual
                almost(residuals[i], 0)

            # Check errorbars
            exp_err_flux = (f_source_0 * self.dataset.err_flux[i] /
                            self.dataset_properties['f_source'])
            exp_err_mag = 2.5 * exp_err_flux / exp_flux / np.log(10.)
            almost(exp_err_mag, res_errors[i])
            assert self.dataset.err_mag[i] != res_errors[i]

    def test_photfmt_scaled_2(self):
        """ check phot_fmt='scaled'; true values of f_source, f_blend should
        yield errorbars identical to the true values."""
        f_source_0 = self.dataset_properties['f_source']
        f_blend_0 = self.dataset_properties['f_blend']

        # Bad = True
        (residuals, res_errors) = self.fit.get_residuals(
            phot_fmt='scaled', source_flux=f_source_0, blend_flux=f_blend_0,
            bad=True)
        almost(res_errors, self.dataset.err_mag)


class TestGradient(unittest.TestCase):
    def test_no_gradient_for_xallarap(self):
        """
        Make sure that gradient for xallarap models in not implemented.
        """
        data = mm.MulensData(file_name=SAMPLE_FILE_02)
        model = mm.Model({
            't_0': 2456836.22, 'u_0': 0.922, 't_E': 22.87,
            'xi_period': 100., 'xi_semimajor_axis': 0.5, 'xi_Omega_node': 90.,
            'xi_inclination': 90., 'xi_argument_of_latitude_reference': 90.})
        fit = mm.FitData(model, data)

        with self.assertRaises(NotImplementedError):
            fit.get_chi2_gradient(['t_0', 'u_0', 't_E'])


# Tests to add:
#
# test get_chi2_gradient(), chi2_gradient:
#   Effectively covered by unit tests in event.py
#
# properties:
#   chi2, chi2_per_point, source_flux, source_fluxes, blend_flux, q_flux,
#   dataset, model
