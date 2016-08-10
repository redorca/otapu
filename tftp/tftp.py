#!/usr/bin/python3

'''
    Present a r/w/o/c interface to transfering files over tftp.
'''

WRQ = 1
RRQ = 2
DAT = 3
ACK = 4
ERR = 5
OACK = 6

class Tftp(object):
    '''
        Create a tftp session.
    '''

    def __init__(self, blocksz="1436", host=None):
        '''
        '''
        self.mode = None
        self.filename = None
        self.blocksz = blocksz
        self.host = host

    def open(self, filename=None, mode='r'):
        '''
            Given a file name, an access mode, issue a transfer
            request from the host passing along the desired values
            for the environment.

            Wait for the ack in either the write() or read() routines.
        '''
        self.mode = mode
        self.filename = filename

    def read(self):
        
