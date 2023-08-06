import numpy as np
import scipy as sp
import argparse

import pint
units = pint.UnitRegistry(system='SI')

def bw_wl_to_bw_f(bw_wl, central_wl):
    wl_min = central_wl - (bw_wl/2)
    wl_max = central_wl + (bw_wl/2)
    f_min = units.speed_of_light / wl_max
    f_max = units.speed_of_light / wl_min
    bw_f = f_max - f_min
    return bw_f

def bw_f_to_bw_wl(bw_f, central_f):
    f_min = central_f - (bw_f/2)
    f_max = central_f + (bw_f/2)
    wl_min = units.speed_of_light / f_max
    wl_max = units.speed_of_light / f_min
    bw_wl = wl_max - wl_min
    return bw_wl


def wavelength_to_frequency(wl):
    c = units.speed_of_light
    f = c / wl
    return f
def frequency_to_wavelength(f):
    c = units.speed_of_light
    wl = c / f
    return wl
def wavelength_to_energy(wl):
    h = units.planck_constant
    f = wavelength_to_frequency(wl)
    e = h * f
    return e
def energy_to_wavelength(e):
    h = units.planck_constant
    f = e / h
    wl = frequency_to_wavelength(f)
    return wl
def frequency_to_energy(f):
    h = units.planck_constant
    e = h * f
    return e
def energy_to_frequency(e):
    h = units.planck_constant
    f = e / h
    return f

def convert_wavelength(input_string):
    input = units(input_string)
    print('Input:', input.to_compact())

    if not (input.dimensionality == units.meter.dimensionality):
        print('Wrong input dimension, should be length')
        print(units.meter.dimensionality)
        print('Input dimesions:', input.dimensionality)
        return None
    
    wavelength = input
    frequency = wavelength_to_frequency(wavelength)
    energy = frequency_to_energy(frequency)
    print('Equals:', wavelength.to('m').to_compact(),',', frequency.to('Hz').to_compact(),',', energy.to('electron_volt').to_compact())
    return

def convert_frequency(input_string):
    input = units(input_string)
    print('Input:', input.to_compact())

    if not (input.dimensionality == units.hertz.dimensionality):
        print('Wrong input dimension, should be', units.hertz.dimensionality)
        print('Input dimesions:', input.dimensionality)
        return None
    
    frequency = input
    wavelength = frequency_to_wavelength(frequency)
    energy = frequency_to_energy(frequency)
    print('Equals:', wavelength.to('m').to_compact(),',', frequency.to('Hz').to_compact(),',', energy.to('electron_volt').to_compact())
    return

def convert_energy(input_string):
    input = units(input_string)
    print('Input:', input.to_compact())

    if not (input.dimensionality == units.joules.dimensionality):
        print('Wrong input dimension, should be', units.joules.dimensionality)
        print('Input dimesions:', input.dimensionality)
        return None
    
    energy = input
    frequency = energy_to_frequency(energy)
    wavelength = frequency_to_wavelength(frequency)
    print('Equals:', wavelength.to('m').to_compact(),',', frequency.to('Hz').to_compact(),',', energy.to('electron_volt').to_compact())
    return


def convert_any(input_string):
    input = units(input_string)

    match input.dimensionality:
        case units.meter.dimensionality:
            convert_wavelength(input_string)

        case units.hertz.dimensionality:
            convert_frequency(input_string)

        case units.joule.dimensionality:
            convert_energy(input_string)
        
        case _:
            print("Your dimesions of", input.dimensionality, 'is not supported.')


def print_wl_f_e(wavelength, frequency, energy):
    print('Equals:', wavelength.to('m').to_compact(),',', frequency.to('Hz').to_compact(),',', energy.to('electron_volt').to_compact())

def check_dimensions(input, dim_string):

    if not (input.dimensionality == units(dim_string).dimensionality):
        print('Wrong input dimension, should be', units.joules.dimensionality)
        print('Input dimesions:', input.dimensionality)
        return False

    return True

def convert_wavelength_bw(wl_bw, wl_centre):
    f_bw = bw_wl_to_bw_f(wl_bw, wl_centre)
    e_bw = frequency_to_energy(f_bw)
    print_wl_f_e(wl_bw, f_bw, e_bw)

def convert_frequency_bw(f_bw, f_centre):
    wl_bw = bw_f_to_bw_wl(f_bw, f_centre)
    e_bw = frequency_to_energy(f_bw)
    print_wl_f_e(wl_bw, f_bw, e_bw)

def convert_energy_bw(e_bw, e_centre):
    f_bw = energy_to_frequency(e_bw)
    f_centre = energy_to_frequency(e_centre)
    wl_bw = bw_f_to_bw_wl(f_bw, f_centre)
    print_wl_f_e(wl_bw, f_bw, e_bw)
    
def convert_any_bw(bw_string, centre_string):

    bw = units(bw_string)
    centre = units(centre_string)

    if not (bw.dimensionality == centre.dimensionality):
        print('Units of centre and bw must be the same')
        return

    
    match bw.dimensionality:
        case units.meter.dimensionality:
            convert_wavelength_bw(bw, centre)

        case units.hertz.dimensionality:
            convert_frequency_bw(bw, centre)

        case units.joule.dimensionality:
            convert_energy_bw(bw, centre)
        
        case _:
            print("Your dimesions of", bw.dimensionality, 'is not supported.')


def transform_limit(dt, function_string):
    dt = units(dt)
    match function_string:
        case 'lorentz':
            tbwp = 0.142

        case 'gauss':
            tbwp = 0.441

        case 'sech':
            tbwp = 0.315
        
        case _:
            print("Your function of", function_string, 'is not supported.')

    df = tbwp / dt

    if dt.dimensionality == units.second.dimensionality:
        print(df.to('hertz').to_compact())
    elif dt.dimensionality == units.hertz.dimensionality:
        print(df.to('seconds').to_compact())
    
    return df



# Parse runtime arguments
parser = argparse.ArgumentParser(
                    prog='optics-calc.py',
                    description='handy calculator for optics conversions')



parser.add_argument('c', help='c (convert), tl (transorm limit), bw (bandwidth convert)', nargs='?', choices=('c', 'tl', 'bw'))

args = parser.parse_args()
args_str = str()
for i, arg in enumerate(vars(args)):
    if i>0:
        value = getattr(args, arg)
        args_str += ('--')
        args_str += (str(arg[:3]))
        args_str += (str(value))

option = args.c

match option:
        case 'c':
            input_string = input('Enter quantity: ')
            convert_any(input_string)

        case 'tl':
            dx = input('Enter fwhm: ')
            function_string = input('Enter function (lorentz, gauss, sech): ')
            transform_limit(dx, function_string)

        case 'bw':
            bw_string = input('Enter bandwidth: ')
            centre_string = input('Enter centre: ')
            convert_any_bw(bw_string, centre_string)
        
        case _:
            print("Your calculation option of ", option, 'is not supported.')
