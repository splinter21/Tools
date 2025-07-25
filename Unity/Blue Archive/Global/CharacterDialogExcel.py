# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterDialogExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterDialogExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterDialogExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterDialogExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterDialogExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def CostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def DialogCategory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def DialogCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def Anniversary(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def DialogType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def ActionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def DurationKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def AnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def LocalizeKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def LocalizeJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def LocalizeTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def LocalizeTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def LocalizeEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def VoiceId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterDialogExcel
    def VoiceIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # CharacterDialogExcel
    def VoiceIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterDialogExcel
    def VoiceIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0

    # CharacterDialogExcel
    def ApplyPosition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterDialogExcel
    def PosX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # CharacterDialogExcel
    def PosY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # CharacterDialogExcel
    def CollectionVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterDialogExcel
    def CvcollectionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def UnlockFavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterDialogExcel
    def UnlockEquipWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterDialogExcel
    def LocalizeCvgroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterDialogExcel
    def TeenMode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def CharacterDialogExcelStart(builder):
    builder.StartObject(30)

def Start(builder):
    CharacterDialogExcelStart(builder)

def CharacterDialogExcelAddCharacterId(builder, characterId):
    builder.PrependInt64Slot(0, characterId, 0)

def AddCharacterId(builder, characterId):
    CharacterDialogExcelAddCharacterId(builder, characterId)

def CharacterDialogExcelAddCostumeUniqueId(builder, costumeUniqueId):
    builder.PrependInt64Slot(1, costumeUniqueId, 0)

def AddCostumeUniqueId(builder, costumeUniqueId):
    CharacterDialogExcelAddCostumeUniqueId(builder, costumeUniqueId)

def CharacterDialogExcelAddDisplayOrder(builder, displayOrder):
    builder.PrependInt64Slot(2, displayOrder, 0)

def AddDisplayOrder(builder, displayOrder):
    CharacterDialogExcelAddDisplayOrder(builder, displayOrder)

def CharacterDialogExcelAddProductionStep(builder, productionStep):
    builder.PrependInt32Slot(3, productionStep, 0)

def AddProductionStep(builder, productionStep):
    CharacterDialogExcelAddProductionStep(builder, productionStep)

def CharacterDialogExcelAddDialogCategory(builder, dialogCategory):
    builder.PrependInt32Slot(4, dialogCategory, 0)

def AddDialogCategory(builder, dialogCategory):
    CharacterDialogExcelAddDialogCategory(builder, dialogCategory)

def CharacterDialogExcelAddDialogCondition(builder, dialogCondition):
    builder.PrependInt32Slot(5, dialogCondition, 0)

def AddDialogCondition(builder, dialogCondition):
    CharacterDialogExcelAddDialogCondition(builder, dialogCondition)

def CharacterDialogExcelAddAnniversary(builder, anniversary):
    builder.PrependInt32Slot(6, anniversary, 0)

def AddAnniversary(builder, anniversary):
    CharacterDialogExcelAddAnniversary(builder, anniversary)

def CharacterDialogExcelAddStartDate(builder, startDate):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(startDate), 0)

def AddStartDate(builder, startDate):
    CharacterDialogExcelAddStartDate(builder, startDate)

def CharacterDialogExcelAddEndDate(builder, endDate):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(endDate), 0)

def AddEndDate(builder, endDate):
    CharacterDialogExcelAddEndDate(builder, endDate)

def CharacterDialogExcelAddGroupId(builder, groupId):
    builder.PrependInt64Slot(9, groupId, 0)

def AddGroupId(builder, groupId):
    CharacterDialogExcelAddGroupId(builder, groupId)

def CharacterDialogExcelAddDialogType(builder, dialogType):
    builder.PrependInt32Slot(10, dialogType, 0)

def AddDialogType(builder, dialogType):
    CharacterDialogExcelAddDialogType(builder, dialogType)

def CharacterDialogExcelAddActionName(builder, actionName):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(actionName), 0)

def AddActionName(builder, actionName):
    CharacterDialogExcelAddActionName(builder, actionName)

def CharacterDialogExcelAddDuration(builder, duration):
    builder.PrependInt64Slot(12, duration, 0)

def AddDuration(builder, duration):
    CharacterDialogExcelAddDuration(builder, duration)

def CharacterDialogExcelAddDurationKr(builder, durationKr):
    builder.PrependInt64Slot(13, durationKr, 0)

def AddDurationKr(builder, durationKr):
    CharacterDialogExcelAddDurationKr(builder, durationKr)

def CharacterDialogExcelAddAnimationName(builder, animationName):
    builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(animationName), 0)

def AddAnimationName(builder, animationName):
    CharacterDialogExcelAddAnimationName(builder, animationName)

def CharacterDialogExcelAddLocalizeKr(builder, localizeKr):
    builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(localizeKr), 0)

def AddLocalizeKr(builder, localizeKr):
    CharacterDialogExcelAddLocalizeKr(builder, localizeKr)

def CharacterDialogExcelAddLocalizeJp(builder, localizeJp):
    builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(localizeJp), 0)

def AddLocalizeJp(builder, localizeJp):
    CharacterDialogExcelAddLocalizeJp(builder, localizeJp)

def CharacterDialogExcelAddLocalizeTh(builder, localizeTh):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(localizeTh), 0)

def AddLocalizeTh(builder, localizeTh):
    CharacterDialogExcelAddLocalizeTh(builder, localizeTh)

def CharacterDialogExcelAddLocalizeTw(builder, localizeTw):
    builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(localizeTw), 0)

def AddLocalizeTw(builder, localizeTw):
    CharacterDialogExcelAddLocalizeTw(builder, localizeTw)

def CharacterDialogExcelAddLocalizeEn(builder, localizeEn):
    builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(localizeEn), 0)

def AddLocalizeEn(builder, localizeEn):
    CharacterDialogExcelAddLocalizeEn(builder, localizeEn)

def CharacterDialogExcelAddVoiceId(builder, voiceId):
    builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(voiceId), 0)

def AddVoiceId(builder, voiceId):
    CharacterDialogExcelAddVoiceId(builder, voiceId)

def CharacterDialogExcelStartVoiceIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartVoiceIdVector(builder, numElems):
    return CharacterDialogExcelStartVoiceIdVector(builder, numElems)

def CharacterDialogExcelAddApplyPosition(builder, applyPosition):
    builder.PrependBoolSlot(21, applyPosition, 0)

def AddApplyPosition(builder, applyPosition):
    CharacterDialogExcelAddApplyPosition(builder, applyPosition)

def CharacterDialogExcelAddPosX(builder, posX):
    builder.PrependFloat32Slot(22, posX, 0.0)

def AddPosX(builder, posX):
    CharacterDialogExcelAddPosX(builder, posX)

def CharacterDialogExcelAddPosY(builder, posY):
    builder.PrependFloat32Slot(23, posY, 0.0)

def AddPosY(builder, posY):
    CharacterDialogExcelAddPosY(builder, posY)

def CharacterDialogExcelAddCollectionVisible(builder, collectionVisible):
    builder.PrependBoolSlot(24, collectionVisible, 0)

def AddCollectionVisible(builder, collectionVisible):
    CharacterDialogExcelAddCollectionVisible(builder, collectionVisible)

def CharacterDialogExcelAddCvcollectionType(builder, cvcollectionType):
    builder.PrependInt32Slot(25, cvcollectionType, 0)

def AddCvcollectionType(builder, cvcollectionType):
    CharacterDialogExcelAddCvcollectionType(builder, cvcollectionType)

def CharacterDialogExcelAddUnlockFavorRank(builder, unlockFavorRank):
    builder.PrependInt64Slot(26, unlockFavorRank, 0)

def AddUnlockFavorRank(builder, unlockFavorRank):
    CharacterDialogExcelAddUnlockFavorRank(builder, unlockFavorRank)

def CharacterDialogExcelAddUnlockEquipWeapon(builder, unlockEquipWeapon):
    builder.PrependBoolSlot(27, unlockEquipWeapon, 0)

def AddUnlockEquipWeapon(builder, unlockEquipWeapon):
    CharacterDialogExcelAddUnlockEquipWeapon(builder, unlockEquipWeapon)

def CharacterDialogExcelAddLocalizeCvgroup(builder, localizeCvgroup):
    builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(localizeCvgroup), 0)

def AddLocalizeCvgroup(builder, localizeCvgroup):
    CharacterDialogExcelAddLocalizeCvgroup(builder, localizeCvgroup)

def CharacterDialogExcelAddTeenMode(builder, teenMode):
    builder.PrependBoolSlot(29, teenMode, 0)

def AddTeenMode(builder, teenMode):
    CharacterDialogExcelAddTeenMode(builder, teenMode)

def CharacterDialogExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return CharacterDialogExcelEnd(builder)
