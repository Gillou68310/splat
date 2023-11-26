from segtypes.common import bss

class CommonSegCommon(bss.CommonSegBss):
    def get_linker_section(self) -> str:
        return ".bss"