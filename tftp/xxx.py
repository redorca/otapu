#!/usr/bin/python3

import struct
import itertools

def pack_rrq(optA, optB):
    pkt = bytes('', "ascii")
    args = []
    form = ""

    for x, y in itertools.chain(optA.items(), optB.items()):
        bx = bytes(x, "ascii")
        by = bytes(str(y), "ascii")
        form += "%dsb%dsb" % (len(x), len(str(y)))
        args.extend([bx, 0, by, 0])

    return form, args

def pack_datum(datum):
    '''
        emtpy
    '''
    form = "%dsx" % len(datum)
    pkt = struct.pack(form, bytes(datum, "ascii"))

    return pkt

def pack_3rrq(optA, optB):
    '''
        emtpy
    '''
    pkt = bytes('', 'ascii')

    for x, y in itertools.chain(optA.items(), optB.items()):
        pkt += pack_datum(x)
        pkt += pack_datum(str(y))
    return  pkt

def pack_2rrq(optA, optB):
    pkt = bytes('', "ascii")
    args = []
    form = ""

    for x, y in itertools.chain(optA.items(), optB.items()):
        bx = bytes(x, "ascii")
        by = bytes(str(y), "ascii")
        form += "%dsx%dsx" % (len(x), len(str(y)))
        args.extend([bx, by])

    pkt = struct.pack(form, *args)
    return  pkt

def __opts_2decode(data):
        '''
            emtpy
        '''
        ixx = kxx = 0
        xfu = []
        fmt = ""
        ixlen = len(data)
        while ixlen > ixx + 1:
            try:
                #
                # Start a new string by adding a character.
                ixx += 1
                #
                # Since the sequence does not include the ixx'th byte
                # subtract 1 so the exit char is the 
                while data[kxx:ixx + 1].isalnum() :
                    if ixlen == ixx:
                        raise StopIteration
                    ixx += 1
                fmt += "%dsx" % len(data[kxx:ixx])
            except IndexError("ixx is out of range?", ixx):
                if ixlen != ixx:
                    raise
            #
            # Because the sequence a[kxx:ixx] does not include ixx,
            # ixx actually points to the beginning of the next stream
            # when the inner loop exits.  So set kxx to point to the
            # beginning of the next string.
            kxx = ixx + 1
        return fmt

def __find_next_opt_string(data):
    '''
        Given a starting range in a data string find the longest
        ascii string available next.

        If the loop exits before finding an ending null byte then
        raise the StopIteration exception so that the calling func
        will know to skip the fmt calculation.

        returns the loop exit index or raises a StopIteration error.
    '''
    aixx = 1
    aixlen = len(data)
    while data[:aixx].isalnum() :
        if aixlen == aixx:
            raise StopIteration
        aixx += 1
    return aixx

def __opts_3decode(data):
        '''
            Take a bytes object that contains a list of options and
            values in null terminated ascii and create a format state-
            ment suitable for struct.pack()/unpack().

            returns a dictionary of the options and their values.
        '''
        ixx = kxx = 0
        fmt = ""
        ixlen = len(data)
        while ixlen > ixx:
            try:
                #
                # Start a new string by adding a character.
                zzz = __find_next_opt_string(data[ixx:])
                ixx +=  zzz
                #
                # the sequence, data[kxx:ixx] ends with non ascii char.
                fmt += "%dsx" % int(zzz - 1)
            except IndexError("ixx is out of range?", ixx):
                if ixlen != ixx:
                    raise
            except StopIteration:
                pass
        alpha = [x.decode("utf-8") for x in struct.unpack(fmt, pkt)]
        beta = dict(itertools.zip_longest(*[iter(alpha)] * 2, fillvalue=None))
        return beta

def __opts_decode(data):
        '''
            Take a bytes object that contains a list of options and
            values in null terminated ascii and create a format state-
            ment suitable for struct.pack()/unpack().

            returns a dictionary of the options and their values.
        '''
        ixx = kxx = 0
        fmt = ""
        ixlen = len(data)
        while ixlen > ixx:
            try:
                #
                # Start a new string by adding a character.
                zzz = __find_next_opt_string(data[ixx:])
                ixx +=  zzz
                #
                # the sequence, data[kxx:ixx] ends with non ascii char.
                fmt += "%dsx" % len(data[kxx:ixx - 1])
            except IndexError("ixx is out of range?", ixx):
                if ixlen != ixx:
                    raise
            except StopIteration:
                pass
            kxx = ixx

        alpha = [x.decode("utf-8") for x in struct.unpack(fmt, pkt)]
        beta = dict(itertools.zip_longest(*[iter(alpha)] * 2, fillvalue=None))
        return beta

def unpack_rrq(form, data):
    ixx = 0
    kxx = 0
    foo = []
    flag = True
    while flag:
        try:
            while data[ixx] != 0:
                if len(data) == ixx:
                    flag = False
                    break
                ixx += 1
            foo.append(str(data[kxx:ixx]))
        except IndexError:
            flag = False
        ixx += 1
        kxx = ixx
    return foo

header = {"doodaa":"octet"}
options = {"tsize":13445, "blksize":1428, "ts":0}
data = b'010203040506070809ff'

pkt = pack_3rrq(header, options)
# formatting, args = pack_2rrq(header, options)
# pkt = struct.pack(formatting, *args)
print("pkt:  ", pkt)

try:
    beta = __opts_3decode(pkt)
except StopIteration:
    print("=======")

def keycheck(sent_opts, recv_opts):
    for key in sent_opts:
        if key not in recv_opts:
            print("missing key ", key)
            return False
    return True

if keycheck(options, beta):
    print("option Keys check.")

if keycheck(header, beta):
    print("header Keys check.")

# print(breakout[0].decode("utf-8"))
if "doodaa" in beta:
    print("Success!!", beta)
else:
    print("Nope, didn't work.")
