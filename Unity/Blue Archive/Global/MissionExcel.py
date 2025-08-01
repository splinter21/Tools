# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MissionExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MissionExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMissionExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MissionExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MissionExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def ResetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def ToastDisplayType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def ToastImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MissionExcel
    def ViewFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MissionExcel
    def Limit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MissionExcel
    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MissionExcel
    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MissionExcel
    def EndDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def StartableEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MissionExcel
    def DateAutoRefer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def PreMissionId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # MissionExcel
    def PreMissionIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # MissionExcel
    def PreMissionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def PreMissionIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # MissionExcel
    def AccountType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def AccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def ContentTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MissionExcel
    def ContentTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MissionExcel
    def ContentTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def ContentTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

    # MissionExcel
    def ShortcutUi(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # MissionExcel
    def ShortcutUiLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def ShortcutUiIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0

    # MissionExcel
    def ChallengeStageShortcut(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def CompleteConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def CompleteConditionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MissionExcel
    def CompleteConditionParameter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # MissionExcel
    def CompleteConditionParameterAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # MissionExcel
    def CompleteConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def CompleteConditionParameterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        return o == 0

    # MissionExcel
    def CompleteConditionParameterTag(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MissionExcel
    def CompleteConditionParameterTagAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MissionExcel
    def CompleteConditionParameterTagLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def CompleteConditionParameterTagIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        return o == 0

    # MissionExcel
    def RewardIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MissionExcel
    def MissionRewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MissionExcel
    def MissionRewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MissionExcel
    def MissionRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def MissionRewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        return o == 0

    # MissionExcel
    def MissionRewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # MissionExcel
    def MissionRewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # MissionExcel
    def MissionRewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def MissionRewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        return o == 0

    # MissionExcel
    def MissionRewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MissionExcel
    def MissionRewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # MissionExcel
    def MissionRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MissionExcel
    def MissionRewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        return o == 0

def MissionExcelStart(builder):
    builder.StartObject(28)

def Start(builder):
    MissionExcelStart(builder)

def MissionExcelAddId(builder, id):
    builder.PrependInt64Slot(0, id, 0)

def AddId(builder, id):
    MissionExcelAddId(builder, id)

def MissionExcelAddCategory(builder, category):
    builder.PrependInt32Slot(1, category, 0)

def AddCategory(builder, category):
    MissionExcelAddCategory(builder, category)

def MissionExcelAddDescription(builder, description):
    builder.PrependUint32Slot(2, description, 0)

def AddDescription(builder, description):
    MissionExcelAddDescription(builder, description)

def MissionExcelAddResetType(builder, resetType):
    builder.PrependInt32Slot(3, resetType, 0)

def AddResetType(builder, resetType):
    MissionExcelAddResetType(builder, resetType)

def MissionExcelAddToastDisplayType(builder, toastDisplayType):
    builder.PrependInt32Slot(4, toastDisplayType, 0)

def AddToastDisplayType(builder, toastDisplayType):
    MissionExcelAddToastDisplayType(builder, toastDisplayType)

def MissionExcelAddToastImagePath(builder, toastImagePath):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(toastImagePath), 0)

def AddToastImagePath(builder, toastImagePath):
    MissionExcelAddToastImagePath(builder, toastImagePath)

def MissionExcelAddViewFlag(builder, viewFlag):
    builder.PrependBoolSlot(6, viewFlag, 0)

def AddViewFlag(builder, viewFlag):
    MissionExcelAddViewFlag(builder, viewFlag)

def MissionExcelAddLimit(builder, limit):
    builder.PrependBoolSlot(7, limit, 0)

def AddLimit(builder, limit):
    MissionExcelAddLimit(builder, limit)

def MissionExcelAddStartDate(builder, startDate):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(startDate), 0)

def AddStartDate(builder, startDate):
    MissionExcelAddStartDate(builder, startDate)

def MissionExcelAddEndDate(builder, endDate):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(endDate), 0)

def AddEndDate(builder, endDate):
    MissionExcelAddEndDate(builder, endDate)

def MissionExcelAddEndDay(builder, endDay):
    builder.PrependInt64Slot(10, endDay, 0)

def AddEndDay(builder, endDay):
    MissionExcelAddEndDay(builder, endDay)

def MissionExcelAddStartableEndDate(builder, startableEndDate):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(startableEndDate), 0)

def AddStartableEndDate(builder, startableEndDate):
    MissionExcelAddStartableEndDate(builder, startableEndDate)

def MissionExcelAddDateAutoRefer(builder, dateAutoRefer):
    builder.PrependInt32Slot(12, dateAutoRefer, 0)

def AddDateAutoRefer(builder, dateAutoRefer):
    MissionExcelAddDateAutoRefer(builder, dateAutoRefer)

def MissionExcelAddDisplayOrder(builder, displayOrder):
    builder.PrependInt64Slot(13, displayOrder, 0)

def AddDisplayOrder(builder, displayOrder):
    MissionExcelAddDisplayOrder(builder, displayOrder)

def MissionExcelAddPreMissionId(builder, preMissionId):
    builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(preMissionId), 0)

def AddPreMissionId(builder, preMissionId):
    MissionExcelAddPreMissionId(builder, preMissionId)

def MissionExcelStartPreMissionIdVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartPreMissionIdVector(builder, numElems):
    return MissionExcelStartPreMissionIdVector(builder, numElems)

def MissionExcelAddAccountType(builder, accountType):
    builder.PrependInt32Slot(15, accountType, 0)

def AddAccountType(builder, accountType):
    MissionExcelAddAccountType(builder, accountType)

def MissionExcelAddAccountLevel(builder, accountLevel):
    builder.PrependInt64Slot(16, accountLevel, 0)

def AddAccountLevel(builder, accountLevel):
    MissionExcelAddAccountLevel(builder, accountLevel)

def MissionExcelAddContentTags(builder, contentTags):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(contentTags), 0)

def AddContentTags(builder, contentTags):
    MissionExcelAddContentTags(builder, contentTags)

def MissionExcelStartContentTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartContentTagsVector(builder, numElems):
    return MissionExcelStartContentTagsVector(builder, numElems)

def MissionExcelAddShortcutUi(builder, shortcutUi):
    builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(shortcutUi), 0)

def AddShortcutUi(builder, shortcutUi):
    MissionExcelAddShortcutUi(builder, shortcutUi)

def MissionExcelStartShortcutUiVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartShortcutUiVector(builder, numElems):
    return MissionExcelStartShortcutUiVector(builder, numElems)

def MissionExcelAddChallengeStageShortcut(builder, challengeStageShortcut):
    builder.PrependInt64Slot(19, challengeStageShortcut, 0)

def AddChallengeStageShortcut(builder, challengeStageShortcut):
    MissionExcelAddChallengeStageShortcut(builder, challengeStageShortcut)

def MissionExcelAddCompleteConditionType(builder, completeConditionType):
    builder.PrependInt32Slot(20, completeConditionType, 0)

def AddCompleteConditionType(builder, completeConditionType):
    MissionExcelAddCompleteConditionType(builder, completeConditionType)

def MissionExcelAddCompleteConditionCount(builder, completeConditionCount):
    builder.PrependInt64Slot(21, completeConditionCount, 0)

def AddCompleteConditionCount(builder, completeConditionCount):
    MissionExcelAddCompleteConditionCount(builder, completeConditionCount)

def MissionExcelAddCompleteConditionParameter(builder, completeConditionParameter):
    builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(completeConditionParameter), 0)

def AddCompleteConditionParameter(builder, completeConditionParameter):
    MissionExcelAddCompleteConditionParameter(builder, completeConditionParameter)

def MissionExcelStartCompleteConditionParameterVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartCompleteConditionParameterVector(builder, numElems):
    return MissionExcelStartCompleteConditionParameterVector(builder, numElems)

def MissionExcelAddCompleteConditionParameterTag(builder, completeConditionParameterTag):
    builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(completeConditionParameterTag), 0)

def AddCompleteConditionParameterTag(builder, completeConditionParameterTag):
    MissionExcelAddCompleteConditionParameterTag(builder, completeConditionParameterTag)

def MissionExcelStartCompleteConditionParameterTagVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartCompleteConditionParameterTagVector(builder, numElems):
    return MissionExcelStartCompleteConditionParameterTagVector(builder, numElems)

def MissionExcelAddRewardIcon(builder, rewardIcon):
    builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(rewardIcon), 0)

def AddRewardIcon(builder, rewardIcon):
    MissionExcelAddRewardIcon(builder, rewardIcon)

def MissionExcelAddMissionRewardParcelType(builder, missionRewardParcelType):
    builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(missionRewardParcelType), 0)

def AddMissionRewardParcelType(builder, missionRewardParcelType):
    MissionExcelAddMissionRewardParcelType(builder, missionRewardParcelType)

def MissionExcelStartMissionRewardParcelTypeVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMissionRewardParcelTypeVector(builder, numElems):
    return MissionExcelStartMissionRewardParcelTypeVector(builder, numElems)

def MissionExcelAddMissionRewardParcelId(builder, missionRewardParcelId):
    builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(missionRewardParcelId), 0)

def AddMissionRewardParcelId(builder, missionRewardParcelId):
    MissionExcelAddMissionRewardParcelId(builder, missionRewardParcelId)

def MissionExcelStartMissionRewardParcelIdVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartMissionRewardParcelIdVector(builder, numElems):
    return MissionExcelStartMissionRewardParcelIdVector(builder, numElems)

def MissionExcelAddMissionRewardAmount(builder, missionRewardAmount):
    builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(missionRewardAmount), 0)

def AddMissionRewardAmount(builder, missionRewardAmount):
    MissionExcelAddMissionRewardAmount(builder, missionRewardAmount)

def MissionExcelStartMissionRewardAmountVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMissionRewardAmountVector(builder, numElems):
    return MissionExcelStartMissionRewardAmountVector(builder, numElems)

def MissionExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MissionExcelEnd(builder)
