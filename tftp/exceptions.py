#!/usr/bin/env python3

'''
    Provide mapping between the tftp error codes and exceptions.
'''

class TftpException(Exception):
    '''
        The base exception class suitable for using to catch all tftp
        exceptions raised.
    '''
    def __init__(self, pkt):
        self.packet = pkt
        Exception.__init__(self)

    def __str__(self):
        pass

class Undefined(TftpException):
    '''
        Error code 0:  no such error.
    '''
    pass

class FileNotFound(TftpException):
    '''
        File referenced by request action is not found.
    '''
    pass

class AccessViolation(TftpException):
    '''
        Insufficient privileges to access resource.
    '''
    pass

class IllegalOp(TftpException):
    '''
        Illegal Tftp opcode.
    '''
    pass

class OutOfSpace(TftpException):
    '''
        No more space for transfer.
    '''
    pass

class UnknownTID(TftpException):
    '''
        Transfer ID from target is unrecognized.
    '''
    pass

class FileExists(TftpException):
    '''
        File to write already exists on the server or on this host.
    '''
    pass

class NoSuchUser(TftpException):
    '''
        No uid found for transfer.
    '''
    pass
