# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopCashScenarioResourceInfoExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopCashScenarioResourceInfoExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsShopCashScenarioResourceInfoExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ShopCashScenarioResourceInfoExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShopCashScenarioResourceInfoExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.ShopCashScenarioResourceInfoExcel import ShopCashScenarioResourceInfoExcel
            obj = ShopCashScenarioResourceInfoExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ShopCashScenarioResourceInfoExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ShopCashScenarioResourceInfoExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def ShopCashScenarioResourceInfoExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    ShopCashScenarioResourceInfoExcelTableStart(builder)

def ShopCashScenarioResourceInfoExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    ShopCashScenarioResourceInfoExcelTableAddDataList(builder, dataList)

def ShopCashScenarioResourceInfoExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return ShopCashScenarioResourceInfoExcelTableStartDataListVector(builder, numElems)

def ShopCashScenarioResourceInfoExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return ShopCashScenarioResourceInfoExcelTableEnd(builder)
