# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UnderCoverStageExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UnderCoverStageExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUnderCoverStageExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UnderCoverStageExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UnderCoverStageExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UnderCoverStageExcel
    def StageNameFile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UnderCoverStageExcel
    def StageTryCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UnderCoverStageExcel
    def ApplySkip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UnderCoverStageExcel
    def SkipCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UnderCoverStageExcel
    def ShowClearScene(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UnderCoverStageExcel
    def StageTips(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UnderCoverStageExcel
    def StageName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UnderCoverStageExcelStart(builder):
    builder.StartObject(8)

def Start(builder):
    UnderCoverStageExcelStart(builder)

def UnderCoverStageExcelAddGroupId(builder, groupId):
    builder.PrependInt64Slot(0, groupId, 0)

def AddGroupId(builder, groupId):
    UnderCoverStageExcelAddGroupId(builder, groupId)

def UnderCoverStageExcelAddStageNameFile(builder, stageNameFile):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(stageNameFile), 0)

def AddStageNameFile(builder, stageNameFile):
    UnderCoverStageExcelAddStageNameFile(builder, stageNameFile)

def UnderCoverStageExcelAddStageTryCount(builder, stageTryCount):
    builder.PrependInt32Slot(2, stageTryCount, 0)

def AddStageTryCount(builder, stageTryCount):
    UnderCoverStageExcelAddStageTryCount(builder, stageTryCount)

def UnderCoverStageExcelAddApplySkip(builder, applySkip):
    builder.PrependBoolSlot(3, applySkip, 0)

def AddApplySkip(builder, applySkip):
    UnderCoverStageExcelAddApplySkip(builder, applySkip)

def UnderCoverStageExcelAddSkipCount(builder, skipCount):
    builder.PrependInt32Slot(4, skipCount, 0)

def AddSkipCount(builder, skipCount):
    UnderCoverStageExcelAddSkipCount(builder, skipCount)

def UnderCoverStageExcelAddShowClearScene(builder, showClearScene):
    builder.PrependBoolSlot(5, showClearScene, 0)

def AddShowClearScene(builder, showClearScene):
    UnderCoverStageExcelAddShowClearScene(builder, showClearScene)

def UnderCoverStageExcelAddStageTips(builder, stageTips):
    builder.PrependUint32Slot(6, stageTips, 0)

def AddStageTips(builder, stageTips):
    UnderCoverStageExcelAddStageTips(builder, stageTips)

def UnderCoverStageExcelAddStageName(builder, stageName):
    builder.PrependUint32Slot(7, stageName, 0)

def AddStageName(builder, stageName):
    UnderCoverStageExcelAddStageName(builder, stageName)

def UnderCoverStageExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return UnderCoverStageExcelEnd(builder)
