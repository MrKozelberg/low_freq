#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:40:18 2022

@author: alexander
"""

import numpy as np
from matplotlib import pyplot as plt


def first():
    # loading measurements of the first experiment
    data = np.genfromtxt('data1.txt')

    power = data[:, 0]
    freq = data[:, 1]

    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(power, freq, label='Эксперимент')

    p1 = np.poly1d(np.polyfit(power, freq, 3))
    ax.plot(power, p1(power), color='black',
            linestyle='--', label='Куб. аппроксим.')

    ax.set_ylabel('Частота, мГц')
    ax.set_xlabel('Мощность накачки, мВт')

    ax.legend()


def second():
    data = np.genfromtxt('data2.txt')

    power1 = data[:, 0]
    power2 = data[:, 1]

    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(power1, power2 - power2[-1], label='Эксперимент')

    p1 = np.poly1d(np.polyfit(power1, power2, 1))
    ax.plot(power1, p1(power1), color='black',
            linestyle='--', label='Лин. аппроксим.')

    ax.set_ylabel('Мощность излучения, мВт')
    ax.set_xlabel('Мощность накачки, мВт')

    ax.legend()


if __name__ == "__main__":
    first()
    second()
