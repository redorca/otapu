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
        return "Error %: %", self.code, self.msg

class Undefined(TftpException):
    '''
        Error code 0:  no such error.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class FileNotFound(TftpException):
    '''
        File referenced by request action is not found.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class AccessViolation(TftpException):
    '''
        Insufficient privileges to access resource.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class IllegalOp(TftpException):
    '''
        Illegal Tftp opcode.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class OutOfSpace(TftpException):
    '''
        No more space for transfer.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class UnknownTID(TftpException):
    '''
        Transfer ID from target is unrecognized.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class FileExists(TftpException):
    '''
        File to write already exists on the server or on this host.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"

class NoSuchUser(TftpException):
    '''
        No uid found for transfer.
    '''
    def __init__(self, pkt):
        TftpException.__init__(self, pkt)
        self.code = 0
        self.msg = "No such error"
