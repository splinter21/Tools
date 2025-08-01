# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameDreamVoiceExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameDreamVoiceExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMinigameDreamVoiceExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MinigameDreamVoiceExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MinigameDreamVoiceExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameDreamVoiceExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameDreamVoiceExcel
    def VoiceCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameDreamVoiceExcel
    def VoiceClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def MinigameDreamVoiceExcelStart(builder):
    builder.StartObject(4)

def Start(builder):
    MinigameDreamVoiceExcelStart(builder)

def MinigameDreamVoiceExcelAddEventContentId(builder, eventContentId):
    builder.PrependInt64Slot(0, eventContentId, 0)

def AddEventContentId(builder, eventContentId):
    MinigameDreamVoiceExcelAddEventContentId(builder, eventContentId)

def MinigameDreamVoiceExcelAddUniqueId(builder, uniqueId):
    builder.PrependInt64Slot(1, uniqueId, 0)

def AddUniqueId(builder, uniqueId):
    MinigameDreamVoiceExcelAddUniqueId(builder, uniqueId)

def MinigameDreamVoiceExcelAddVoiceCondition(builder, voiceCondition):
    builder.PrependInt32Slot(2, voiceCondition, 0)

def AddVoiceCondition(builder, voiceCondition):
    MinigameDreamVoiceExcelAddVoiceCondition(builder, voiceCondition)

def MinigameDreamVoiceExcelAddVoiceClip(builder, voiceClip):
    builder.PrependUint32Slot(3, voiceClip, 0)

def AddVoiceClip(builder, voiceClip):
    MinigameDreamVoiceExcelAddVoiceClip(builder, voiceClip)

def MinigameDreamVoiceExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MinigameDreamVoiceExcelEnd(builder)
