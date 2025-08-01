# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDefenseCharacterBanExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDefenseCharacterBanExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameDefenseCharacterBanExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameDefenseCharacterBanExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameDefenseCharacterBanExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDefenseCharacterBanExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def MiniGameDefenseCharacterBanExcelStart(builder):
    builder.StartObject(2)

def Start(builder):
    MiniGameDefenseCharacterBanExcelStart(builder)

def MiniGameDefenseCharacterBanExcelAddEventContentId(builder, eventContentId):
    builder.PrependInt64Slot(0, eventContentId, 0)

def AddEventContentId(builder, eventContentId):
    MiniGameDefenseCharacterBanExcelAddEventContentId(builder, eventContentId)

def MiniGameDefenseCharacterBanExcelAddCharacterId(builder, characterId):
    builder.PrependInt64Slot(1, characterId, 0)

def AddCharacterId(builder, characterId):
    MiniGameDefenseCharacterBanExcelAddCharacterId(builder, characterId)

def MiniGameDefenseCharacterBanExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MiniGameDefenseCharacterBanExcelEnd(builder)
