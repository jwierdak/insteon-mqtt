#===========================================================================
#
# Tests for: insteont_mqtt/message/OutAllLinkUpdate.py
#
#===========================================================================
import insteon_mqtt.message as Msg
import pytest

#===========================================================================
class Test_OutAllLinkUpdate:
    #-----------------------------------------------------------------------
    def test_basic(self):
        b = bytes([0x02, 0x6f, 0x80, 0x00, 0x00, 0x32, 0xf4, 0x22, 0x00,
                   0x00, 0x00, 0x15])
        obj = Msg.OutAllLinkUpdate.from_bytes(b)

        # TODO: check obj

        str(obj)

    #-----------------------------------------------------------------------


#===========================================================================
