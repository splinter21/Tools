# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PresetParcelsExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PresetParcelsExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPresetParcelsExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # PresetParcelsExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PresetParcelsExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.PresetParcelsExcel import PresetParcelsExcel
            obj = PresetParcelsExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # PresetParcelsExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PresetParcelsExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def PresetParcelsExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    PresetParcelsExcelTableStart(builder)

def PresetParcelsExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    PresetParcelsExcelTableAddDataList(builder, dataList)

def PresetParcelsExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return PresetParcelsExcelTableStartDataListVector(builder, numElems)

def PresetParcelsExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return PresetParcelsExcelTableEnd(builder)
