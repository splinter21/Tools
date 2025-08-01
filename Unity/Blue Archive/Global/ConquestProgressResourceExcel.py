# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestProgressResourceExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestProgressResourceExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConquestProgressResourceExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConquestProgressResourceExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestProgressResourceExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestProgressResourceExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestProgressResourceExcel
    def Group(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestProgressResourceExcel
    def ProgressResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestProgressResourceExcel
    def VoiceId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConquestProgressResourceExcel
    def VoiceIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # ConquestProgressResourceExcel
    def VoiceIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestProgressResourceExcel
    def VoiceIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # ConquestProgressResourceExcel
    def ProgressLocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ConquestProgressResourceExcelStart(builder):
    builder.StartObject(6)

def Start(builder):
    ConquestProgressResourceExcelStart(builder)

def ConquestProgressResourceExcelAddId(builder, id):
    builder.PrependInt64Slot(0, id, 0)

def AddId(builder, id):
    ConquestProgressResourceExcelAddId(builder, id)

def ConquestProgressResourceExcelAddEventContentId(builder, eventContentId):
    builder.PrependInt64Slot(1, eventContentId, 0)

def AddEventContentId(builder, eventContentId):
    ConquestProgressResourceExcelAddEventContentId(builder, eventContentId)

def ConquestProgressResourceExcelAddGroup(builder, group):
    builder.PrependInt32Slot(2, group, 0)

def AddGroup(builder, group):
    ConquestProgressResourceExcelAddGroup(builder, group)

def ConquestProgressResourceExcelAddProgressResource(builder, progressResource):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(progressResource), 0)

def AddProgressResource(builder, progressResource):
    ConquestProgressResourceExcelAddProgressResource(builder, progressResource)

def ConquestProgressResourceExcelAddVoiceId(builder, voiceId):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(voiceId), 0)

def AddVoiceId(builder, voiceId):
    ConquestProgressResourceExcelAddVoiceId(builder, voiceId)

def ConquestProgressResourceExcelStartVoiceIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartVoiceIdVector(builder, numElems):
    return ConquestProgressResourceExcelStartVoiceIdVector(builder, numElems)

def ConquestProgressResourceExcelAddProgressLocalizeCode(builder, progressLocalizeCode):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(progressLocalizeCode), 0)

def AddProgressLocalizeCode(builder, progressLocalizeCode):
    ConquestProgressResourceExcelAddProgressLocalizeCode(builder, progressLocalizeCode)

def ConquestProgressResourceExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return ConquestProgressResourceExcelEnd(builder)
