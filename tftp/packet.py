#!/usr/bin/env python3

'''
    Collect all packet handling in Tftp_packet such as formation of
    the packet.
'''

import struct
import itertools

class TftpPacket(object):
    '''
        empty
    '''

    RRQ = 1
    WRQ = 2
    ACK = 3
    DAT = 4
    ERR = 5
    OACK = 6

    encodings = {"options":None, "filename":None, "blknum":None, "error":None,
                 "msg":None, "data":None}

    def __init__(self, options):
        '''
            options is a dictionary of transmission options negotiated
            with the server.  Data such as block size, timeout, file size,
            and foo.
        '''
        self.packet = None
        self.options = options
        self.opcodes = {"RRQ":RRQ, "WRQ":WRQ, "ACK":ACK,
                        "DAT":DAT, "ERR":ERR, "OACK":OACK}
        self.opt_strings = {"0":"INV", "1":"RRQ", "2":"WRQ", "3":"ACK",
                            "4":"DAT", "5":"ERR", "6":"OACK"}

    def op_encode(self, opcode, pkt):
        '''
            empty
        '''
        op_pkt = struct.pack("!H", self.opcodes[opcode])
        return op_pkt + pkt

    def op_decode(self, pkt):
        '''
            empty
        '''
        xfu = pkt[0:2]
#       opcode = str(xfu, "utf-8")
#       opcode = xfu.decode()
        fmt = "!H"
        opcode, = struct.unpack(fmt, xfu)
        print("opcode: ", opcode)
        return self.opt_strings[str(opcode)], pkt[2:0]

    def blknum_decode(self, pkt):
        '''
            empty
        '''
        xfu = pkt[0:2]

        fmt = "!H"
        opcode, = struct.unpack(fmt, xfu)

    def decode_entry(self, data, data_type="byte"):
        '''
            Decode data from a packet based on the data type passed in.
            Valid values for the data type are:
                "byte"
                "half"
                "word"
                "dbl"
                "float"
                "string"

                size has meaning only for data_type "string"
        '''

        if data_type is "byte":
            fmt = "!b"  # Unsigned byte.
            size = 1
        elif data_type is "half":
            fmt = "!H"  # Unsigned short.
            size = 2
        elif data_type  = "word":
            fmt = "!l"  # Unsigned long.
            size = 4
        elif data_type is "dbl":
            fmt = "!d"  # Unsigned double.
            size = 8
        elif data_type is "float":
            fmt = "!f"  # Unsigned float.
            size = 8
        elif data_type is "string":
            fmt = "!%dsx".
            size = 1
        else:
            raise(TypeError)

        argu, = struct.unpack(fmt, xfu)
        return argu, pkt[size:]

    def opts_decode(data):
        '''
            emtpy
        '''
        ixx = kxx = 0
        fmt = ""
        while len(data) > ixx:
            try:
                ixx += 1
                while data[kxx:ixx].isalnum() :
                    if len(data) == ixx:
                        break
                    ixx += 1
                #
                # 
                fmt += "%dsx" % len(data[kxx:ixx - 1])
            except IndexError("ixx is out of range?", ixx):
                if len(data) != ixx:
                    raise
            kxx = ixx
        return fmt

    def pkt_encode(self, opcode, options=None, filename=None,
                   blknum=None, error=None, err_msg=None, data=None):
        '''
            empty
        '''

        #
        # The first entry in a packet is the opcode, everybody gets one:
        fmt = '!H'
        args = [self.opcodes[opcode]]

        if opcode in ["RRQ", "WRQ", "OACK"]:
            if options is None:
                raise ValueError("Request or OACK packets have no options.")
            if opcode is not "OACK":
                assert filename is not None
                start = {filename: "octet"}
            for xxx, yyy in itertools.chain(start.items(), options.items()):
                #
                # Since values of keys may be non strings, convert them
                # to strings where appropriate.
                fmt += "%dsx%dsx" % (len(xxx), len(str(yyy)))
                args.append(bytes(xxx, "ascii"))
                args.append(bytes(str(yyy), "ascii"))
        elif opcode in ["ACK", "DAT"]:
            if blknum is None:
                raise ValueError("blknum is missing.")
            fmt += "H"
            args.append(int(blknum))

        elif opcode == "ERR":
            if error is None:
                raise ValueError("Error code is missing for an error packet.")
            fmt += "Hx"
            args.append(error)
            if err_msg is not None:
                fmt += "%dsx" % len(err_msg)
                args.append(bytes(err_msg, "ascii"))

        pkt = struct.pack(fmt, *args)
        if data is not None:
            if opcode == "DAT":
                raise ValueError("Data packet has no data.")
            pkt += data

        return pkt

    def pkt_decode(self, pkt):
        '''
            Given a packet received over a socket break it down into
            a tuple and return that.
        '''

        opcode, newpkt = TftpPacket.op_decode(self, pkt)
        print("op code: ", opcode)

if __name__ == "__main__":
    OPTS = {"blksize":1432, "tsize":143256, "health":"good"}
    PKT = TftpPacket(OPTS)
    BUF = PKT.pkt_encode("RRQ", options=OPTS, filename="doodaa")
#   BUF = PKT.pkt_encode("ACK", blknum=4589, options=OPTS, filename="doodaa")
    BUF = PKT.pkt_encode("ERR", err_msg="No alarm", error=45, filename="doodaa")
    PKT.pkt_decode(BUF)
