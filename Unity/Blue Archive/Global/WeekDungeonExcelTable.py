# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WeekDungeonExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WeekDungeonExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWeekDungeonExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # WeekDungeonExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WeekDungeonExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.WeekDungeonExcel import WeekDungeonExcel
            obj = WeekDungeonExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WeekDungeonExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WeekDungeonExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def WeekDungeonExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    WeekDungeonExcelTableStart(builder)

def WeekDungeonExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    WeekDungeonExcelTableAddDataList(builder, dataList)

def WeekDungeonExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return WeekDungeonExcelTableStartDataListVector(builder, numElems)

def WeekDungeonExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return WeekDungeonExcelTableEnd(builder)
