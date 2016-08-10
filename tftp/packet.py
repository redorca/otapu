#!/usr/bin/env python3

'''
    Collect all packet handling in Tftp_packet such as formation of
    the packet.
'''

class TftpPacket(object):
    '''
        empty
    '''

    def __init__(self, size):
        '''
            empty
        '''
        pass

    def dummy(self):
        '''
            empty
        '''
        pass

    def dummy2(self):
        '''
            empty
        '''
        pass


class  TftpPacketHandling(object):
    '''
        empty
    '''


    def __init__(self, options):
        '''
            options is a dictionary of transmission options negotiated
            with the server.  Data such as block size, timeout, file size,
            and foo.
        '''
        self.packet = None
        self.options = options

    def op_encode(self, opcode, pkt):
        '''
            empty
        '''
        pass

    def op_decode(self):
        '''
            empty
        '''
        pkt = self.packet
        opcode = pkt.buf[0:2]
        pkt.data = pkt.buf[2:]
        return opcode
