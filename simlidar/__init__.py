#!/usr/bin/env python

'''
    xvlidar.py - Python class for reading from GetSurreal's XV Lidar Controller.  
    Author: Karel De Coster (k.decoster94@gmail.com)
    Github: http://github.com/kareldecoster/RPLidar
    Date: 2016-4-7

    Adapted from lidar.py downloaded from 

      http://www.getsurreal.com/products/xv-lidar-controller/xv-lidar-controller-visual-test

    Copyright (C) 2016 Simon D. Levy

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as 
    published by the Free Software Foundation, either version 3 of the 
    License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
'''

class simLidar(object):

    def __init__(self, com_port):
        '''
        Opens a serial connection to the XV Lidar on the specifiec com port (e.g.,
        'COM5', '/dev/ttyACM0').  Connection will run on its own thread.
        '''
        self.values = [()]*360
        return
        
    def getScan(self):
        '''
        Returns 360 (distance, quality) tuples.
        '''
        i = 0
        while i<360:
            self.values[i] = (100, 10)
            i+=1
        return [pair if len(pair) == 2 else (0,0) for pair in self.values]

