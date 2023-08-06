import typing
import os

from ctypes import *


# Структуры
class Module(Structure):

    _fields_ = [
        ("base_address", c_void_p),
        ("size_of_image", c_ulong),
        ("entry_point", c_void_p)
    ]

    def __init__(self, process_handle: int) -> None:

        self.__process_handle = process_handle

    @property
    def base_address(self) -> int:
        """Получает базовый адрес модуля."""

        return self._fields_[0]

    @property
    def size_of_image(self) -> int:
        """Получает размер изображения модуля."""

        return self._fields_[1]

    @property
    def entry_point(self) -> int:
        """Получает точку входа в модуль."""

        return self._fields_[2]

    @property
    def name(self) -> str:
        """Получает имя модуля."""

        name_buffer = (c_wchar * 512)()

        if not _GetModuleFileNameExW(self.__process_handle, c_void_p(self.base_address), name_buffer, sizeof(name_buffer)):
            raise Exception("Не удалось получить имя модуля.")

        return name_buffer.value.strip().split("\\")[-1]

    @property
    def full_name(self) -> str:
        """Получает имя модуля и путь до него."""

        name_buffer = (c_wchar * 512)()

        if not _GetModuleFileNameExW(self.__process_handle, c_void_p(self.base_address), name_buffer, sizeof(name_buffer)):
            raise Exception("Не удалось получить имя модуля.")

        return name_buffer.value.strip()


# Инициализация библиотек и ф-ий
_kernel32 = windll.kernel32
_psapi = windll.psapi

_GetProcessImageFileNameW = _psapi.GetProcessImageFileNameW
_EnumProcesses = _psapi.EnumProcesses
_EnumProcessModulesEx = _psapi.EnumProcessModulesEx
_GetModuleInformation = _psapi.GetModuleInformation
_GetModuleFileNameExW = _psapi.GetModuleFileNameExW
_OpenProcess = _kernel32.OpenProcess
_CloseHandle = _kernel32.CloseHandle
_IsWow64Process = _kernel32.IsWow64Process
_ReadProcessMemory = _kernel32.ReadProcessMemory
_WriteProcessMemory = _kernel32.WriteProcessMemory

# Аргументы ф-ий
_GetProcessImageFileNameW.argtypes = [c_void_p, c_wchar_p, c_ulong]
_EnumProcesses.argtypes = [POINTER(c_ulong), c_ulong, POINTER(c_ulong)]
_EnumProcessModulesEx.argtypes = [c_void_p, POINTER(c_void_p), c_ulong, POINTER(c_ulong), c_ulong]
_GetModuleInformation.argtypes = [c_void_p, c_void_p, POINTER(Module), c_ulong]
_GetModuleFileNameExW.argtypes = [c_void_p, c_void_p, c_wchar_p, c_ulong]
_OpenProcess.argtypes = [c_ulong, c_int, c_ulong]
_CloseHandle.argtypes = [c_void_p]
_IsWow64Process.argtypes = [c_void_p, POINTER(c_int)]
_ReadProcessMemory.argtypes = [c_void_p, c_void_p, c_void_p, c_size_t, POINTER(c_size_t)]
_WriteProcessMemory.argtypes = [c_void_p, c_void_p, c_void_p, c_size_t, POINTER(c_size_t)]

# Возвращаемые типы ф-ий
_GetProcessImageFileNameW.restype = c_ulong
_EnumProcesses.restype = c_int
_EnumProcessModulesEx.restype = c_int
_GetModuleInformation.restype = c_int
_GetModuleFileNameExW.restype = c_ulong
_OpenProcess.restype = c_void_p
_CloseHandle.restype = c_int
_IsWow64Process.restype = c_int
_ReadProcessMemory.restype = c_int


# Классы
class Process:

    @typing.overload
    def __init__(self, process_name: str) -> None:
        """Класс процесса.\n
        Позволяет взаимодействовать с виртуальной памятью и потоками процесса.\n"""

    @typing.overload
    def __init__(self, process_id: int) -> None:
        """Класс процесса.\n
        Позволяет взаимодействовать с виртуальной памятью и потоками процесса.\n"""

    def __init__(self, process_name: str = None, process_id: str = None) -> None:

        # Инициализация при помощи имени
        if isinstance(process_name, str) and process_name:

            process_name = process_name.strip()
            if not process_name.endswith(".exe"):
                process_name += ".exe"

            for process in list_processes(close_handles_on_finish=True):

                if process_name == process[0]:
                    self.name = process_name
                    self.id = process[1]

                    if process_handle := _OpenProcess(0x001F0FFF, False, process[1]):
                        self.handle = process_handle

                    else:
                        raise Exception("Не удалось подключить к указанному процессу.")

                    return

            raise Exception("Процесс с указаным именем не найден.")

        # Инициализация при помощи ID
        elif isinstance(process_id, int) and process_id:

            for process in list_processes(close_handles_on_finish=True):

                if process_id == process[1]:
                    self.name = process[0]
                    self.id = process_id

                    if process_handle := _OpenProcess(0x001F0FFF, False, process_id):
                        self.handle = process_handle

                    else:
                        raise Exception("Не удалось подключить к указанному процессу.")

                    return

            raise Exception("Процесс с указаным id не найден.")

        else:
            raise Exception("В качестве аргумента-инициализаатора должен быть передан id процесса(int) или его имя(str).")

    def __del__(self) -> None:

        _CloseHandle(self.handle)

    # Методы
    def is_64_bit(self) -> bool:
        """Получает разрядность процесса.\n
        Возвращает True если процесс 64-разрядный, иначе возвращает False."""

        is_64_bit_result = c_int()
        wow_64_successed = _IsWow64Process(self.handle, byref(is_64_bit_result))

        if not wow_64_successed:
            raise Exception("Не удалось получить разрядность процесса.")

        return bool(is_64_bit_result.value)

    def list_modules(self) -> list[Module]:
        """Получает список модулей процесса.\n
        Возвращает список содержащий объекты \"Module\"."""

        modules_buffer = (c_void_p * 4096)()
        modules_buffer_size = sizeof(modules_buffer)
        bytes_needed = c_ulong()

        if not _EnumProcessModulesEx(self.handle, cast(modules_buffer, POINTER(c_void_p)), modules_buffer_size, byref(bytes_needed), 0x3):
            raise Exception("Не удалось получить список модулей.")

        modules_list = list()

        module_size = sizeof(c_void_p)
        for module_index in range(bytes_needed.value // module_size):
            module_info = Module(self.handle)

            if _GetModuleInformation(self.handle, modules_buffer[module_index], byref(module_info), sizeof(module_info)):
                modules_list.append(module_info)

        return modules_list

    def get_module(self, module_name: str, compare_in_lowercase: bool = True) -> Module:
        """Получает модуль процесса.\n
        Возвращает объекь \"Module\"."""

        for module in self.list_modules():

            if compare_in_lowercase:

                if module.name().lower() == module_name.lower().strip():
                    return module

            else:

                if module.name() == module_name.strip():
                    return module

        raise Exception("Модуль с указаным именем не найден.")

    def read_ctypes_buffer(self, address: int, buffer: object, unwrap_type: str = None) -> None:

        if not _ReadProcessMemory(self.handle, c_void_p(address), byref(buffer), sizeof(buffer), byref(c_size_t())):
            raise Exception("Не удалось прочитать память процесса.")

        if unwrap_type:
            return eval(f"buffer.{unwrap_type}")

        else:
            return buffer


# Функции
def list_processes(close_handles_on_finish: bool = False) -> list[tuple[str, int]]:
    """Получает список всех активных процессов.\n
    Возращает список содержащий кортежи (имя, id) процесса."""

    process_ids_buffer = (c_ulong * 4096)()
    procces_ids_buffer_size = sizeof(process_ids_buffer)
    bytes_needed = c_ulong()

    if not _EnumProcesses(process_ids_buffer, procces_ids_buffer_size, byref(bytes_needed)):
        raise Exception("Не удалость получить список процессов.")

    processes_list = list()

    process_id_size = sizeof(c_ulong)
    for process_index in range(bytes_needed.value // process_id_size):

        if process_handle := _OpenProcess(0x001F0FFF, False, process_ids_buffer[process_index]):
            file_name_image = (c_wchar * 512)()

            if _GetProcessImageFileNameW(process_handle, file_name_image, 512):
                process_name = os.path.basename(file_name_image.value)
                processes_list.append((process_name, process_ids_buffer[process_index]))

                if close_handles_on_finish:
                    _CloseHandle(process_handle)

    return processes_list
