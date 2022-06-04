from segtypes.common.asm import CommonSegAsm
from typing import Optional
from pathlib import Path

from util import options


class Ps2SegAsm(CommonSegAsm):
    @staticmethod
    def get_file_header():
        ret = []

        ret.append("""
.macro .late_rodata
    .section .rodata
.endm

.macro glabel label
    .global \label
    .type \label, @function
    \label:
.endm

.set noat
.set noreorder

""")

        return ret
