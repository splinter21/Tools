# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GroundNodeFlat(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GroundNodeFlat()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGroundNodeFlat(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GroundNodeFlat
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GroundNodeFlat
    def X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundNodeFlat
    def Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundNodeFlat
    def IsCanNotUseSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GroundNodeFlat
    def PositionOffset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Global.GroundVector3 import GroundVector3
            obj = GroundVector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GroundNodeFlat
    def NodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundNodeFlat
    def OriginalNodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def GroundNodeFlatStart(builder):
    builder.StartObject(6)

def Start(builder):
    GroundNodeFlatStart(builder)

def GroundNodeFlatAddX(builder, x):
    builder.PrependInt32Slot(0, x, 0)

def AddX(builder, x):
    GroundNodeFlatAddX(builder, x)

def GroundNodeFlatAddY(builder, y):
    builder.PrependInt32Slot(1, y, 0)

def AddY(builder, y):
    GroundNodeFlatAddY(builder, y)

def GroundNodeFlatAddIsCanNotUseSkill(builder, isCanNotUseSkill):
    builder.PrependBoolSlot(2, isCanNotUseSkill, 0)

def AddIsCanNotUseSkill(builder, isCanNotUseSkill):
    GroundNodeFlatAddIsCanNotUseSkill(builder, isCanNotUseSkill)

def GroundNodeFlatAddPositionOffset(builder, positionOffset):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(positionOffset), 0)

def AddPositionOffset(builder, positionOffset):
    GroundNodeFlatAddPositionOffset(builder, positionOffset)

def GroundNodeFlatAddNodeType(builder, nodeType):
    builder.PrependInt32Slot(4, nodeType, 0)

def AddNodeType(builder, nodeType):
    GroundNodeFlatAddNodeType(builder, nodeType)

def GroundNodeFlatAddOriginalNodeType(builder, originalNodeType):
    builder.PrependInt32Slot(5, originalNodeType, 0)

def AddOriginalNodeType(builder, originalNodeType):
    GroundNodeFlatAddOriginalNodeType(builder, originalNodeType)

def GroundNodeFlatEnd(builder):
    return builder.EndObject()

def End(builder):
    return GroundNodeFlatEnd(builder)
