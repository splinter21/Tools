# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AnimationBlendTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AnimationBlendTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAnimationBlendTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AnimationBlendTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AnimationBlendTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.BlendData import BlendData
            obj = BlendData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AnimationBlendTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AnimationBlendTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def AnimationBlendTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    AnimationBlendTableStart(builder)

def AnimationBlendTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    AnimationBlendTableAddDataList(builder, dataList)

def AnimationBlendTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return AnimationBlendTableStartDataListVector(builder, numElems)

def AnimationBlendTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return AnimationBlendTableEnd(builder)
