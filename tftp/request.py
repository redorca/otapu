#!/usr/bin/python3

'''
    empty
'''

class Request(object):
    '''
        empty
    '''
    def __init__(self):
        '''
            empty
        '''
# Figure out the source hosts ip addr, create the socket, done.
#
        self.req_type = None
        self.filename = None
# Reserve these settings for the Read and Write sub classes
#       if rtype == 'write':
#           self.req_type = 'wb'
#       else:
#           self.req_type = 'rb'

    def transfer(self):
        '''
            empty
        '''
        pass

    def open(self, filename, filemode):
        '''
            empty
        '''
        self.filename = filename
        assert self.req_type == filemode

    def read(self, ):
        '''
            empty
        '''
        pass

    def write(self):
        '''
            empty
        '''
        pass

    def close(self):
        '''
            empty
        '''
        pass

    def __enter__(self):
        self.open(self.filename, self.req_type)

    def __exit__(self, exc_type, exc_mode, exc_tb):
        self.close()


class Read(Request):
    '''
        empty
    '''
    def __init__(self, ipaddr):
        self.target = ipaddr
        self.host = None
        self.req_type = 'r'
        Request.__init__(self)


class Write(Request):
    '''
        empty
    '''
    def __init__(self, ipaddr):
        self.target = ipaddr
        self.host = None
        self.req_type = 'w'
        Request.__init__(self)
