# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameAudioAnimatorExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameAudioAnimatorExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameAudioAnimatorExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameAudioAnimatorExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameAudioAnimatorExcel
    def ControllerNameHash(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MiniGameAudioAnimatorExcel
    def VoiceNamePrefix(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameAudioAnimatorExcel
    def StateNameHash(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MiniGameAudioAnimatorExcel
    def StateName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameAudioAnimatorExcel
    def IgnoreInterruptDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameAudioAnimatorExcel
    def IgnoreInterruptPlay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameAudioAnimatorExcel
    def Volume(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MiniGameAudioAnimatorExcel
    def Delay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MiniGameAudioAnimatorExcel
    def AudioPriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MiniGameAudioAnimatorExcel
    def AudioClipPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # MiniGameAudioAnimatorExcel
    def AudioClipPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameAudioAnimatorExcel
    def AudioClipPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # MiniGameAudioAnimatorExcel
    def VoiceHash(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MiniGameAudioAnimatorExcel
    def VoiceHashAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # MiniGameAudioAnimatorExcel
    def VoiceHashLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameAudioAnimatorExcel
    def VoiceHashIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

def MiniGameAudioAnimatorExcelStart(builder):
    builder.StartObject(11)

def Start(builder):
    MiniGameAudioAnimatorExcelStart(builder)

def MiniGameAudioAnimatorExcelAddControllerNameHash(builder, controllerNameHash):
    builder.PrependUint32Slot(0, controllerNameHash, 0)

def AddControllerNameHash(builder, controllerNameHash):
    MiniGameAudioAnimatorExcelAddControllerNameHash(builder, controllerNameHash)

def MiniGameAudioAnimatorExcelAddVoiceNamePrefix(builder, voiceNamePrefix):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(voiceNamePrefix), 0)

def AddVoiceNamePrefix(builder, voiceNamePrefix):
    MiniGameAudioAnimatorExcelAddVoiceNamePrefix(builder, voiceNamePrefix)

def MiniGameAudioAnimatorExcelAddStateNameHash(builder, stateNameHash):
    builder.PrependUint32Slot(2, stateNameHash, 0)

def AddStateNameHash(builder, stateNameHash):
    MiniGameAudioAnimatorExcelAddStateNameHash(builder, stateNameHash)

def MiniGameAudioAnimatorExcelAddStateName(builder, stateName):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(stateName), 0)

def AddStateName(builder, stateName):
    MiniGameAudioAnimatorExcelAddStateName(builder, stateName)

def MiniGameAudioAnimatorExcelAddIgnoreInterruptDelay(builder, ignoreInterruptDelay):
    builder.PrependBoolSlot(4, ignoreInterruptDelay, 0)

def AddIgnoreInterruptDelay(builder, ignoreInterruptDelay):
    MiniGameAudioAnimatorExcelAddIgnoreInterruptDelay(builder, ignoreInterruptDelay)

def MiniGameAudioAnimatorExcelAddIgnoreInterruptPlay(builder, ignoreInterruptPlay):
    builder.PrependBoolSlot(5, ignoreInterruptPlay, 0)

def AddIgnoreInterruptPlay(builder, ignoreInterruptPlay):
    MiniGameAudioAnimatorExcelAddIgnoreInterruptPlay(builder, ignoreInterruptPlay)

def MiniGameAudioAnimatorExcelAddVolume(builder, volume):
    builder.PrependFloat32Slot(6, volume, 0.0)

def AddVolume(builder, volume):
    MiniGameAudioAnimatorExcelAddVolume(builder, volume)

def MiniGameAudioAnimatorExcelAddDelay(builder, delay):
    builder.PrependFloat32Slot(7, delay, 0.0)

def AddDelay(builder, delay):
    MiniGameAudioAnimatorExcelAddDelay(builder, delay)

def MiniGameAudioAnimatorExcelAddAudioPriority(builder, audioPriority):
    builder.PrependInt32Slot(8, audioPriority, 0)

def AddAudioPriority(builder, audioPriority):
    MiniGameAudioAnimatorExcelAddAudioPriority(builder, audioPriority)

def MiniGameAudioAnimatorExcelAddAudioClipPath(builder, audioClipPath):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(audioClipPath), 0)

def AddAudioClipPath(builder, audioClipPath):
    MiniGameAudioAnimatorExcelAddAudioClipPath(builder, audioClipPath)

def MiniGameAudioAnimatorExcelStartAudioClipPathVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartAudioClipPathVector(builder, numElems):
    return MiniGameAudioAnimatorExcelStartAudioClipPathVector(builder, numElems)

def MiniGameAudioAnimatorExcelAddVoiceHash(builder, voiceHash):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(voiceHash), 0)

def AddVoiceHash(builder, voiceHash):
    MiniGameAudioAnimatorExcelAddVoiceHash(builder, voiceHash)

def MiniGameAudioAnimatorExcelStartVoiceHashVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartVoiceHashVector(builder, numElems):
    return MiniGameAudioAnimatorExcelStartVoiceHashVector(builder, numElems)

def MiniGameAudioAnimatorExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MiniGameAudioAnimatorExcelEnd(builder)
