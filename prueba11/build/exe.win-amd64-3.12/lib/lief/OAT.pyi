from typing import Any, ClassVar, Optional, Union

from typing import overload
import io
import lief.Android # type: ignore
import lief.DEX # type: ignore
import lief.ELF # type: ignore
import lief.OAT # type: ignore
import lief.OAT.Binary # type: ignore
import lief.OAT.Class # type: ignore
import lief.OAT.Header # type: ignore
import os

class Binary(lief.ELF.Binary):
    class it_classes:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg: int, /) -> lief.OAT.Class: ...
        def __iter__(self) -> lief.OAT.Binary.it_classes: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Class: ...

    class it_dex_files:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg: int, /) -> lief.DEX.File: ...
        def __iter__(self) -> lief.OAT.Binary.it_dex_files: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.DEX.File: ...

    class it_methods:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg: int, /) -> lief.OAT.Method: ...
        def __iter__(self) -> lief.OAT.Binary.it_methods: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Method: ...

    class it_oat_dex_files:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg: int, /) -> lief.OAT.DexFile: ...
        def __iter__(self) -> lief.OAT.Binary.it_oat_dex_files: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.DexFile: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def get_class(self, class_name: str) -> lief.OAT.Class: ...
    @overload
    def get_class(self, class_index: int) -> lief.OAT.Class: ...
    @property
    def classes(self) -> lief.OAT.Binary.it_classes: ...
    @property
    def dex2dex_json_info(self) -> str: ...
    @property
    def dex_files(self) -> lief.OAT.Binary.it_dex_files: ...
    @property
    def has_class(self) -> bool: ...
    @property
    def header(self) -> lief.OAT.Header: ...  # type: ignore
    @property
    def methods(self) -> lief.OAT.Binary.it_methods: ...
    @property
    def oat_dex_files(self) -> lief.OAT.Binary.it_oat_dex_files: ...

class Class(lief.Object):
    class it_methods:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg: int, /) -> lief.OAT.Method: ...
        def __iter__(self) -> lief.OAT.Class.it_methods: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Method: ...
    def __init__(self) -> None: ...
    def has_dex_class(self) -> bool: ...
    @overload
    def is_quickened(self, dex_method: lief.DEX.Method) -> bool: ...
    @overload
    def is_quickened(self, method_index: int) -> bool: ...
    @overload
    def method_offsets_index(self, arg: lief.DEX.Method, /) -> int: ...
    @overload
    def method_offsets_index(self, arg: int, /) -> int: ...
    @property
    def bitmap(self) -> list[int]: ...
    @property
    def fullname(self) -> str: ...
    @property
    def index(self) -> int: ...
    @property
    def methods(self) -> lief.OAT.Class.it_methods: ...
    @property
    def status(self) -> lief.OAT.OAT_CLASS_STATUS: ...
    @property
    def type(self) -> lief.OAT.OAT_CLASS_TYPES: ...

class DexFile(lief.Object):
    checksum: int
    dex_offset: int
    location: str
    def __init__(self) -> None: ...
    @property
    def dex_file(self) -> lief.DEX.File: ...
    @property
    def has_dex_file(self) -> bool: ...

class HEADER_KEYS:
    BOOT_CLASS_PATH: ClassVar[HEADER_KEYS] = ...
    CLASS_PATH: ClassVar[HEADER_KEYS] = ...
    COMPILER_FILTER: ClassVar[HEADER_KEYS] = ...
    CONCURRENT_COPYING: ClassVar[HEADER_KEYS] = ...
    DEBUGGABLE: ClassVar[HEADER_KEYS] = ...
    DEX2OAT_CMD_LINE: ClassVar[HEADER_KEYS] = ...
    DEX2OAT_HOST: ClassVar[HEADER_KEYS] = ...
    HAS_PATCH_INFO: ClassVar[HEADER_KEYS] = ...
    IMAGE_LOCATION: ClassVar[HEADER_KEYS] = ...
    NATIVE_DEBUGGABLE: ClassVar[HEADER_KEYS] = ...
    PIC: ClassVar[HEADER_KEYS] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

class Header(lief.Object):
    class element_t:
        key: lief.OAT.HEADER_KEYS
        value: str
        def __init__(self, *args, **kwargs) -> None: ...

    class it_key_values_t:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg: int, /) -> lief.OAT.Header.element_t: ...
        def __iter__(self) -> lief.OAT.Header.it_key_values_t: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Header.element_t: ...
    def __init__(self) -> None: ...
    def get(self, key: lief.OAT.HEADER_KEYS) -> str: ...
    def set(self, key: lief.OAT.HEADER_KEYS, value: str) -> lief.OAT.Header: ...
    def __getitem__(self, arg: lief.OAT.HEADER_KEYS, /) -> str: ...
    def __setitem__(self, arg0: lief.OAT.HEADER_KEYS, arg1: str, /) -> lief.OAT.Header: ...
    @property
    def checksum(self) -> int: ...
    @property
    def executable_offset(self) -> int: ...
    @property
    def i2c_code_bridge_offset(self) -> int: ...
    @property
    def i2i_bridge_offset(self) -> int: ...
    @property
    def image_file_location_oat_checksum(self) -> int: ...
    @property
    def image_file_location_oat_data_begin(self) -> int: ...
    @property
    def image_patch_delta(self) -> int: ...
    @property
    def instruction_set(self) -> lief.OAT.INSTRUCTION_SETS: ...
    @property
    def jni_dlsym_lookup_offset(self) -> int: ...
    @property
    def key_value_size(self) -> int: ...
    @property
    def key_values(self) -> lief.OAT.Header.it_key_values_t: ...
    @property
    def keys(self) -> list[lief.OAT.HEADER_KEYS]: ...
    @property
    def magic(self) -> list[int]: ...
    @property
    def nb_dex_files(self) -> int: ...
    @property
    def oat_dex_files_offset(self) -> int: ...
    @property
    def quick_generic_jni_trampoline_offset(self) -> int: ...
    @property
    def quick_imt_conflict_trampoline_offset(self) -> int: ...
    @property
    def quick_resolution_trampoline_offset(self) -> int: ...
    @property
    def quick_to_interpreter_bridge_offset(self) -> int: ...
    @property
    def values(self) -> list[str]: ...
    @property
    def version(self) -> int: ...

class INSTRUCTION_SETS:
    ARM: ClassVar[INSTRUCTION_SETS] = ...
    ARM_64: ClassVar[INSTRUCTION_SETS] = ...
    MIPS: ClassVar[INSTRUCTION_SETS] = ...
    MIPS_64: ClassVar[INSTRUCTION_SETS] = ...
    NONE: ClassVar[INSTRUCTION_SETS] = ...
    THUMB2: ClassVar[INSTRUCTION_SETS] = ...
    X86: ClassVar[INSTRUCTION_SETS] = ...
    X86_64: ClassVar[INSTRUCTION_SETS] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

class Method(lief.Object):
    quick_code: list[int]
    def __init__(self) -> None: ...
    @property
    def dex_method(self) -> lief.DEX.Method: ...
    @property
    def has_dex_method(self) -> bool: ...
    @property
    def is_compiled(self) -> bool: ...
    @property
    def is_dex2dex_optimized(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def oat_class(self) -> lief.OAT.Class: ...

class OAT_CLASS_STATUS:
    ERROR: ClassVar[OAT_CLASS_STATUS] = ...
    IDX: ClassVar[OAT_CLASS_STATUS] = ...
    INITIALIZED: ClassVar[OAT_CLASS_STATUS] = ...
    INITIALIZING: ClassVar[OAT_CLASS_STATUS] = ...
    LOADED: ClassVar[OAT_CLASS_STATUS] = ...
    NOTREADY: ClassVar[OAT_CLASS_STATUS] = ...
    RESOLVED: ClassVar[OAT_CLASS_STATUS] = ...
    RESOLVING: ClassVar[OAT_CLASS_STATUS] = ...
    RETIRED: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFICATION_AT_RUNTIME: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFIED: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFYING: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFYING_AT_RUNTIME: ClassVar[OAT_CLASS_STATUS] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

class OAT_CLASS_TYPES:
    ALL_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    NONE_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    SOME_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

def android_version(arg: int, /) -> lief.Android.ANDROID_VERSIONS: ...
@overload
def parse(oat_file: str) -> Optional[lief.OAT.Binary]: ...
@overload
def parse(oat_file: str, vdex_file: str) -> Optional[lief.OAT.Binary]: ...
@overload
def parse(raw: list[int]) -> Optional[lief.OAT.Binary]: ...
@overload
def parse(obj: Union[io.IOBase|os.PathLike]) -> Optional[lief.OAT.Binary]: ...
@overload
def version(binary: lief.ELF.Binary) -> int: ...
@overload
def version(file: str) -> int: ...
@overload
def version(raw: list[int]) -> int: ...