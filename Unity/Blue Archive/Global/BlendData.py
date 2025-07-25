# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BlendData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BlendData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBlendData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BlendData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BlendData
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # BlendData
    def InfoList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.BlendInfo import BlendInfo
            obj = BlendInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BlendData
    def InfoListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # BlendData
    def InfoListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def BlendDataStart(builder):
    builder.StartObject(2)

def Start(builder):
    BlendDataStart(builder)

def BlendDataAddType(builder, type):
    builder.PrependInt32Slot(0, type, 0)

def AddType(builder, type):
    BlendDataAddType(builder, type)

def BlendDataAddInfoList(builder, infoList):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(infoList), 0)

def AddInfoList(builder, infoList):
    BlendDataAddInfoList(builder, infoList)

def BlendDataStartInfoListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartInfoListVector(builder, numElems):
    return BlendDataStartInfoListVector(builder, numElems)

def BlendDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return BlendDataEnd(builder)
