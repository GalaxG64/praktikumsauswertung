#!/usr/bin/python

###############################################################################
# Use:  This file is a objectifying the code allready written. It uses Objects
#       to make using the software easieer
# Author: Alexander Becker
###############################################################################

import json
import numpy as np
import matplotlib.pyplot as plt
import collections as col

class messung:
   """Represents a messreihe and its associated data such as statisticaly relevant data. It also provides Funktions to output that data and transform it into appropriate formats"""
    @staticmethod
    def calculate_gaussian_data(messreihe):
        """Calculates the mean, variance and std. deviation of a list of numbers"""
        std_dev = np.std(messreihe,ddof=1)
        var = np.var(messreihe)
        mean = np.mean(messreihe)
        return std_dev, var, mean

    @staticmethod
    def graph_width(measurement,overshute=0.2):
        """Determines the Interval generated to plot over from the given data"""
        span = max(measurement) - min(measurement)
        minimum = min(measurement) - overshute*span
        maximum = max(measurement) + overshute*span
        return np.linspace(minimum,maximum,2000)

    @staticmethod
    def gauss_funktion(x_werte,mittelwert,standardabweichung):
        """calculates the values of a gauss curve characterized by the deviation and mean for every value given in x_werte. returns an array"""
        return (1/(standardabweichung*2*np.pi)*np.exp(-(1/2)*((x_werte-mittelwert)/standardabweichung)**2))

    def __init__(self, messgroesse, messreihe, Formelzeichen, messgeraet=None, messfehler=None)
        """Constructor; besides taking given arguments, it allso builds all the necessary stuff for a plotting and a table"""
        self.messreihe = messreihe
        self.messgroesse = messgroesse
        self.Formelzeichen = Formelzeichen
        self.messgeraet = messgeraet
        self.messfehler = messfehler
        self.std_dev, self.var, self.mean = calculate_gaussian_data(self.messreihe)
        self.plot = col.namedtuple(plot, 'x_values, gauss, hist)
        self.plot.x_values = graph_width(self.messreihe)
        self.plot.gauss = col.namedtuple(gauss ,'function, color, label, linestyle')
        self.plot.gauss.function= gauss_funktion(self.x_values, self.mean, self.std_dev)
        self.plot.hist = col.namedtuple(hist, 'bins, align, log, color, label')
        self.plot.hist.bins = 20
        self.plot.hist.align = 'mid'
        self.plot.hist.log = False
        self.plot.hist.color = 'green'
        if type(messgroesse) == str:
            self.plot.hist.label = messgroesse
            self.plpt.gauss.label = 'Gaussian curve of '+messgroesse
        else:
            self.plot.hist.label = None
            self.plot.gauss.label = None

    @classmethod
    def set_hist_parameter(bins=10,align='mid',log=False,color='green',label=None)
        self.plot.hist = self.messreihe,bins=bins,color=color,align=align,log=log,label=label)