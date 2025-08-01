# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterDialogEventExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterDialogEventExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterDialogEventExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterDialogEventExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterDialogEventExcel
    def CostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def OriginalCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def EventId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogCategory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogConditionDetail(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogConditionDetailValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DialogType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def ActionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def DurationKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def AnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def LocalizeEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogEventExcel
    def VoiceId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterDialogEventExcel
    def VoiceIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # CharacterDialogEventExcel
    def VoiceIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogEventExcel
    def VoiceIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0

    # CharacterDialogEventExcel
    def CollectionVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterDialogEventExcel
    def CvcollectionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def CvunlockScenarioType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def UnlockEventSeason(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def ScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogEventExcel
    def LocalizeCvgroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def CharacterDialogEventExcelStart(builder):
    builder.StartObject(27)

def Start(builder):
    CharacterDialogEventExcelStart(builder)

def CharacterDialogEventExcelAddCostumeUniqueId(builder, costumeUniqueId):
    builder.PrependInt64Slot(0, costumeUniqueId, 0)

def AddCostumeUniqueId(builder, costumeUniqueId):
    CharacterDialogEventExcelAddCostumeUniqueId(builder, costumeUniqueId)

def CharacterDialogEventExcelAddOriginalCharacterId(builder, originalCharacterId):
    builder.PrependInt64Slot(1, originalCharacterId, 0)

def AddOriginalCharacterId(builder, originalCharacterId):
    CharacterDialogEventExcelAddOriginalCharacterId(builder, originalCharacterId)

def CharacterDialogEventExcelAddDisplayOrder(builder, displayOrder):
    builder.PrependInt64Slot(2, displayOrder, 0)

def AddDisplayOrder(builder, displayOrder):
    CharacterDialogEventExcelAddDisplayOrder(builder, displayOrder)

def CharacterDialogEventExcelAddEventId(builder, eventId):
    builder.PrependInt64Slot(3, eventId, 0)

def AddEventId(builder, eventId):
    CharacterDialogEventExcelAddEventId(builder, eventId)

def CharacterDialogEventExcelAddProductionStep(builder, productionStep):
    builder.PrependInt32Slot(4, productionStep, 0)

def AddProductionStep(builder, productionStep):
    CharacterDialogEventExcelAddProductionStep(builder, productionStep)

def CharacterDialogEventExcelAddDialogCategory(builder, dialogCategory):
    builder.PrependInt32Slot(5, dialogCategory, 0)

def AddDialogCategory(builder, dialogCategory):
    CharacterDialogEventExcelAddDialogCategory(builder, dialogCategory)

def CharacterDialogEventExcelAddDialogCondition(builder, dialogCondition):
    builder.PrependInt32Slot(6, dialogCondition, 0)

def AddDialogCondition(builder, dialogCondition):
    CharacterDialogEventExcelAddDialogCondition(builder, dialogCondition)

def CharacterDialogEventExcelAddDialogConditionDetail(builder, dialogConditionDetail):
    builder.PrependInt32Slot(7, dialogConditionDetail, 0)

def AddDialogConditionDetail(builder, dialogConditionDetail):
    CharacterDialogEventExcelAddDialogConditionDetail(builder, dialogConditionDetail)

def CharacterDialogEventExcelAddDialogConditionDetailValue(builder, dialogConditionDetailValue):
    builder.PrependInt64Slot(8, dialogConditionDetailValue, 0)

def AddDialogConditionDetailValue(builder, dialogConditionDetailValue):
    CharacterDialogEventExcelAddDialogConditionDetailValue(builder, dialogConditionDetailValue)

def CharacterDialogEventExcelAddGroupId(builder, groupId):
    builder.PrependInt64Slot(9, groupId, 0)

def AddGroupId(builder, groupId):
    CharacterDialogEventExcelAddGroupId(builder, groupId)

def CharacterDialogEventExcelAddDialogType(builder, dialogType):
    builder.PrependInt32Slot(10, dialogType, 0)

def AddDialogType(builder, dialogType):
    CharacterDialogEventExcelAddDialogType(builder, dialogType)

def CharacterDialogEventExcelAddActionName(builder, actionName):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(actionName), 0)

def AddActionName(builder, actionName):
    CharacterDialogEventExcelAddActionName(builder, actionName)

def CharacterDialogEventExcelAddDuration(builder, duration):
    builder.PrependInt64Slot(12, duration, 0)

def AddDuration(builder, duration):
    CharacterDialogEventExcelAddDuration(builder, duration)

def CharacterDialogEventExcelAddDurationKr(builder, durationKr):
    builder.PrependInt64Slot(13, durationKr, 0)

def AddDurationKr(builder, durationKr):
    CharacterDialogEventExcelAddDurationKr(builder, durationKr)

def CharacterDialogEventExcelAddAnimationName(builder, animationName):
    builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(animationName), 0)

def AddAnimationName(builder, animationName):
    CharacterDialogEventExcelAddAnimationName(builder, animationName)

def CharacterDialogEventExcelAddLocalizeKr(builder, localizeKr):
    builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(localizeKr), 0)

def AddLocalizeKr(builder, localizeKr):
    CharacterDialogEventExcelAddLocalizeKr(builder, localizeKr)

def CharacterDialogEventExcelAddLocalizeJp(builder, localizeJp):
    builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(localizeJp), 0)

def AddLocalizeJp(builder, localizeJp):
    CharacterDialogEventExcelAddLocalizeJp(builder, localizeJp)

def CharacterDialogEventExcelAddLocalizeTh(builder, localizeTh):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(localizeTh), 0)

def AddLocalizeTh(builder, localizeTh):
    CharacterDialogEventExcelAddLocalizeTh(builder, localizeTh)

def CharacterDialogEventExcelAddLocalizeTw(builder, localizeTw):
    builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(localizeTw), 0)

def AddLocalizeTw(builder, localizeTw):
    CharacterDialogEventExcelAddLocalizeTw(builder, localizeTw)

def CharacterDialogEventExcelAddLocalizeEn(builder, localizeEn):
    builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(localizeEn), 0)

def AddLocalizeEn(builder, localizeEn):
    CharacterDialogEventExcelAddLocalizeEn(builder, localizeEn)

def CharacterDialogEventExcelAddVoiceId(builder, voiceId):
    builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(voiceId), 0)

def AddVoiceId(builder, voiceId):
    CharacterDialogEventExcelAddVoiceId(builder, voiceId)

def CharacterDialogEventExcelStartVoiceIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartVoiceIdVector(builder, numElems):
    return CharacterDialogEventExcelStartVoiceIdVector(builder, numElems)

def CharacterDialogEventExcelAddCollectionVisible(builder, collectionVisible):
    builder.PrependBoolSlot(21, collectionVisible, 0)

def AddCollectionVisible(builder, collectionVisible):
    CharacterDialogEventExcelAddCollectionVisible(builder, collectionVisible)

def CharacterDialogEventExcelAddCvcollectionType(builder, cvcollectionType):
    builder.PrependInt32Slot(22, cvcollectionType, 0)

def AddCvcollectionType(builder, cvcollectionType):
    CharacterDialogEventExcelAddCvcollectionType(builder, cvcollectionType)

def CharacterDialogEventExcelAddCvunlockScenarioType(builder, cvunlockScenarioType):
    builder.PrependInt32Slot(23, cvunlockScenarioType, 0)

def AddCvunlockScenarioType(builder, cvunlockScenarioType):
    CharacterDialogEventExcelAddCvunlockScenarioType(builder, cvunlockScenarioType)

def CharacterDialogEventExcelAddUnlockEventSeason(builder, unlockEventSeason):
    builder.PrependInt64Slot(24, unlockEventSeason, 0)

def AddUnlockEventSeason(builder, unlockEventSeason):
    CharacterDialogEventExcelAddUnlockEventSeason(builder, unlockEventSeason)

def CharacterDialogEventExcelAddScenarioGroupId(builder, scenarioGroupId):
    builder.PrependInt64Slot(25, scenarioGroupId, 0)

def AddScenarioGroupId(builder, scenarioGroupId):
    CharacterDialogEventExcelAddScenarioGroupId(builder, scenarioGroupId)

def CharacterDialogEventExcelAddLocalizeCvgroup(builder, localizeCvgroup):
    builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(localizeCvgroup), 0)

def AddLocalizeCvgroup(builder, localizeCvgroup):
    CharacterDialogEventExcelAddLocalizeCvgroup(builder, localizeCvgroup)

def CharacterDialogEventExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return CharacterDialogEventExcelEnd(builder)
