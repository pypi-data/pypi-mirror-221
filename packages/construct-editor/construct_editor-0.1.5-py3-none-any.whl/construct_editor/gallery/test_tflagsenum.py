import construct as cs
import construct_typed as cst
import dataclasses
import typing as t
from . import GalleryItem


class Permission(cst.FlagsEnumBase):
    R = 4
    W = 2
    X = 1
    RWX = 7


class Day(cst.FlagsEnumBase):
    Monday = 1 << 0
    Tuesday = 1 << 1
    Wednesday = 1 << 2
    Thursday = 1 << 3
    Friday = 1 << 4
    Saturday = 1 << 5
    Sunday = 1 << 6


class LongList(cst.FlagsEnumBase):
    Entry0 = 1 << 0
    Entry1 = 1 << 1
    Entry2 = 1 << 2
    Entry3 = 1 << 3
    Entry4 = 1 << 4
    Entry5 = 1 << 5
    Entry6 = 1 << 6
    Entry7 = 1 << 7
    Entry8 = 1 << 8
    Entry9 = 1 << 9
    Entry10 = 1 << 10
    Entry11 = 1 << 11
    Entry12 = 1 << 12
    Entry13 = 1 << 13
    Entry14 = 1 << 14
    Entry15 = 1 << 15
    Entry16 = 1 << 16
    Entry17 = 1 << 17
    Entry18 = 1 << 18
    Entry19 = 1 << 19
    Entry20 = 1 << 20
    Entry21 = 1 << 21
    Entry22 = 1 << 22
    Entry23 = 1 << 23
    Entry24 = 1 << 24
    Entry25 = 1 << 25
    Entry26 = 1 << 26
    Entry27 = 1 << 27
    Entry28 = 1 << 28
    Entry29 = 1 << 29
    Entry30 = 1 << 30
    Entry31 = 1 << 31
    Entry32 = 1 << 32
    Entry33 = 1 << 33
    Entry34 = 1 << 34
    Entry35 = 1 << 35
    Entry36 = 1 << 36
    Entry37 = 1 << 37
    Entry38 = 1 << 38
    Entry39 = 1 << 39
    Entry40 = 1 << 40
    Entry41 = 1 << 41
    Entry42 = 1 << 42
    Entry43 = 1 << 43
    Entry44 = 1 << 44
    Entry45 = 1 << 45
    Entry46 = 1 << 46
    Entry47 = 1 << 47
    Entry48 = 1 << 48
    Entry49 = 1 << 49
    Entry50 = 1 << 50


@dataclasses.dataclass
class FlagsEnumTest(cst.DataclassMixin):
    permissions: Permission = cst.csfield(cst.TFlagsEnum(cs.Int8ul, Permission))
    days: Day = cst.csfield(cst.TFlagsEnum(cs.Int8ul, Day))
    long_list: LongList = cst.csfield(cst.TFlagsEnum(cs.Int64ul, LongList))
    days2: Day = cst.csfield(cst.TFlagsEnum(cs.Int8ul, Day))


constr = cst.DataclassStruct(FlagsEnumTest)

gallery_item = GalleryItem(
    construct=constr,
    example_binarys={
        "2": constr.build(
            FlagsEnumTest(
                permissions=Permission.R | Permission.W,
                days=Day.Monday | Day.Sunday,
                long_list=LongList.Entry49 | LongList.Entry50,
                days2=Day.Monday | Day.Sunday,
            )
        ),
        "1": constr.build(
            FlagsEnumTest(
                permissions=Permission.R,
                days=Day.Monday,
                long_list=LongList.Entry0,
                days2=Day.Monday,
            )
        ),
        "Zeros": constr.build(
            FlagsEnumTest(
                permissions=Permission(0),
                days=Day(0),
                long_list=LongList(0),
                days2=Day(0),
            )
        ),
    },
)
