# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BlendInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BlendInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBlendInfo(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BlendInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BlendInfo
    def From(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # BlendInfo
    def To(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # BlendInfo
    def Blend(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def BlendInfoStart(builder):
    builder.StartObject(3)

def Start(builder):
    BlendInfoStart(builder)

def BlendInfoAddFrom(builder, from_):
    builder.PrependInt32Slot(0, from_, 0)

def AddFrom(builder, from_):
    BlendInfoAddFrom(builder, from_)

def BlendInfoAddTo(builder, to):
    builder.PrependInt32Slot(1, to, 0)

def AddTo(builder, to):
    BlendInfoAddTo(builder, to)

def BlendInfoAddBlend(builder, blend):
    builder.PrependFloat32Slot(2, blend, 0.0)

def AddBlend(builder, blend):
    BlendInfoAddBlend(builder, blend)

def BlendInfoEnd(builder):
    return builder.EndObject()

def End(builder):
    return BlendInfoEnd(builder)
