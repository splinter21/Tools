# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EquipmentLevelExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EquipmentLevelExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEquipmentLevelExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EquipmentLevelExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EquipmentLevelExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.EquipmentLevelExcel import EquipmentLevelExcel
            obj = EquipmentLevelExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # EquipmentLevelExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentLevelExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def EquipmentLevelExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    EquipmentLevelExcelTableStart(builder)

def EquipmentLevelExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    EquipmentLevelExcelTableAddDataList(builder, dataList)

def EquipmentLevelExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return EquipmentLevelExcelTableStartDataListVector(builder, numElems)

def EquipmentLevelExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return EquipmentLevelExcelTableEnd(builder)
