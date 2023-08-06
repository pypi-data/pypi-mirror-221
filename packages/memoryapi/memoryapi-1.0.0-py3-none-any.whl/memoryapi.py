import typing
import os
import re

from ctypes import *

# Константы
PAGE_EXECUTE: int = 0x10
PAGE_EXECUTE_READ: int = 0x20
PAGE_EXECUTE_READWRITE: int = 0x40
PAGE_EXECUTE_WRITECOPY: int = 0x80
PAGE_NOACCESS: int = 0x01
PAGE_READONLY: int = 0x02
PAGE_READWRITE: int = 0x04
PAGE_WRITECOPY: int = 0x08
PAGE_TARGETS_INVALID: int = 0x40000000

PAGE_GUARD: int = 0x100
PAGE_NOCACHE: int = 0x200
PAGE_WRITECOMBINE: int = 0x400

MEM_COMMIT: int = 0x00001000
MEM_RESERVE: int = 0x00002000
MEM_RESET: int = 0x00080000
MEM_RESET_UNDO: int = 0x1000000
MEM_LARGE_PAGES: int = 0x20000000
MEM_PHYSICAL: int = 0x00400000
MEM_TOP_DOWN: int = 0x00100000

MEM_DECOMMIT: int = 0x00004000
MEM_RELEASE: int = 0x00008000
MEM_COALESCE_PLACEHOLDERS = 0x00000001
MEM_PRESERVE_PLACEHOLDER = 0x00000002


# Структуры
class MemoryBasicInformation(Structure):

    _fields_ = [
        ("base_address", c_void_p),
        ("allocation_base", c_void_p),
        ("allocation_protect", c_ulong),
        ("partition_id", c_ushort),
        ("region_size", c_size_t),
        ("state", c_ulong),
        ("protect", c_ulong),
        ("allocation_type", c_ulong),
    ]

    @property
    def base_address(self) -> int:

        return self._fields_[0]

    @property
    def allocation_base(self) -> int:

        return self._fields_[1]

    @property
    def allocation_protect(self) -> int:

        return self._fields_[2]

    @property
    def partition_id(self) -> int:

        return self._fields_[3]

    @property
    def region_size(self) -> int:

        return self._fields_[4]

    @property
    def state(self) -> int:

        return self._fields_[5]

    @property
    def protect(self) -> int:

        return self._fields_[6]

    @property
    def allocation_type(self) -> int:

        return self._fields_[7]


class ThreadInfo(Structure):

    _fields_ = [
        ("size", c_ulong),
        ("cnt_usage", c_ulong),
        ("thread_id", c_ulong),
        ("owner_process_id", c_ulong),
        ("base_pri", c_long),
        ("delta_pri", c_long),
        ("flags", c_ulong)
    ]

    def __init__(self) -> None:

        self.handle = 0
        self.start_address = 0

    @property
    def size(self) -> int:

        return self._fields_[0]

    @property
    def cnt_usage(self) -> int:

        return self._fields_[1]

    @property
    def thread_id(self) -> int:

        return self._fields_[2]

    @property
    def owner_process_id(self) -> int:

        return self._fields_[3]

    @property
    def base_pri(self) -> int:

        return self._fields_[4]

    @property
    def delta_pri(self) -> int:

        return self._fields_[5]

    @property
    def flags(self) -> int:

        return self._fields_[6]

    def close(self) -> None:
        """Закрывает дескриптор потока."""

        if not _CloseHandle(self.handle):
            raise Exception("Не удалось закрыть дескриптор потока.")

    def terminate(self, exit_code: int = 0) -> None:
        """Уничтожает поток процесса."""

        if not _TerminateThread(self.handle, exit_code):
            raise Exception("Не удалось уничтожить поток.")

    def suspend(self) -> None:
        """Замораживает поток процесса."""

        if _SuspendThread(self.handle) == -1:
            raise Exception("Не удалось заморозить поток.")

    def resume(self) -> None:
        """Размораживает поток процесса."""

        if _ResumeThread(self.handle) == -1:
            raise Exception("Не удалось разморозить поток.")


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

        return self._fields_[0]

    @property
    def size_of_image(self) -> int:

        return self._fields_[1]

    @property
    def entry_point(self) -> int:

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
_ntdll = windll.ntdll

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
_CreateToolhelp32Snapshot = _kernel32.CreateToolhelp32Snapshot
_Thread32First = _kernel32.Thread32First
_Thread32Next = _kernel32.Thread32Next
_OpenThread = _kernel32.OpenThread
_TerminateThread = _kernel32.TerminateThread
_SuspendThread = _kernel32.SuspendThread
_ResumeThread = _kernel32.ResumeThread
_VirtualQueryEx = _kernel32.VirtualQueryEx
_VirtualAllocEx = _kernel32.VirtualAllocEx
_VirtualFreeEx = _kernel32.VirtualFreeEx
_VirtualProtectEx = _kernel32.VirtualProtectEx
_NtQueryInformationThread = _ntdll.NtQueryInformationThread

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
_CreateToolhelp32Snapshot.argtypes = [c_ulong, c_ulong]
_Thread32First.argtypes = [c_void_p, POINTER(ThreadInfo)]
_Thread32Next.argtypes = [c_void_p, POINTER(ThreadInfo)]
_OpenThread.argtypes = [c_ulong, c_int, c_ulong]
_TerminateThread.argtypes = [c_void_p, c_ulong]
_SuspendThread.argtypes = [c_void_p]
_ResumeThread.argtypes = [c_void_p]
_VirtualQueryEx.argtypes = [c_void_p, c_void_p, POINTER(MemoryBasicInformation), c_size_t]
_VirtualAllocEx.argtypes = [c_void_p, c_void_p, c_size_t, c_ulong, c_ulong]
_VirtualFreeEx.argtypes = [c_void_p, c_void_p, c_size_t, c_ulong]
_VirtualProtectEx.argtypes = [c_void_p, c_void_p, c_size_t, c_ulong, POINTER(c_ulong)]
_NtQueryInformationThread.argtypes = [c_void_p, c_int, c_void_p, c_ulong, POINTER(c_ulong)]

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
_CreateToolhelp32Snapshot.restype = c_void_p
_Thread32First.restype = c_int
_Thread32Next.restype = c_int
_OpenThread.restype = c_void_p
_TerminateThread.restype = c_int
_SuspendThread.restype = c_ulong
_ResumeThread.restype = c_ulong
_VirtualQueryEx.restype = c_size_t
_VirtualAllocEx.restype = c_void_p
_VirtualFreeEx.restype = c_int
_VirtualProtectEx.restype = c_int
_NtQueryInformationThread.restype = c_long


# Классы
class Process:

    @typing.overload
    def __init__(self, process_name: str) -> None:
        """Класс процесса.\n
        Позволяет взаимодействовать с виртуальной памятью и потоками процесса."""

    @typing.overload
    def __init__(self, process_id: int) -> None:
        """Класс процесса.\n
        Позволяет взаимодействовать с виртуальной памятью и потоками процесса."""

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
        """Получает разрядность процесса."""

        is_64_bit_result = c_int()

        if not _IsWow64Process(self.handle, byref(is_64_bit_result)):
            raise Exception("Не удалось получить разрядность процесса.")

        return bool(is_64_bit_result.value)

    def list_modules(self) -> list[Module]:
        """Получает список модулей процесса."""

        modules_buffer = (c_void_p * 4096)()
        bytes_needed = c_ulong()

        if not _EnumProcessModulesEx(self.handle, cast(modules_buffer, POINTER(c_void_p)), sizeof(modules_buffer), byref(bytes_needed), 0x3):
            raise Exception("Не удалось получить список модулей.")

        modules_list = list()

        module_size = sizeof(c_void_p)
        for module_index in range(bytes_needed.value // module_size):
            module_info = Module(self.handle)

            if _GetModuleInformation(self.handle, modules_buffer[module_index], byref(module_info), sizeof(module_info)):
                modules_list.append(module_info)

        return modules_list

    def get_module(self, module_name: str, compare_in_lowercase: bool = True) -> Module:
        """Получает модуль процесса."""

        for module in self.list_modules():

            if compare_in_lowercase:

                if module.name.lower() == module_name.lower().strip():
                    return module

            else:

                if module.name() == module_name.strip():
                    return module

        raise Exception("Модуль с указаным именем не найден.")

    def list_threads(self) -> list[ThreadInfo]:
        """Получает список потоков процесса."""

        snapshot = _CreateToolhelp32Snapshot(0x4, 0)
        if snapshot == -1:
            raise Exception("Не удалось сделать снимок потоков.")

        thread_entry = ThreadInfo()
        thread_entry.size = sizeof(thread_entry)

        first_thread = _Thread32First(snapshot, byref(thread_entry))
        if not first_thread:
            raise Exception("Не получилось получить список потоков.")

        threads_list = list()

        while True:

            if thread_entry.owner_process_id == self.id:
                thread_entry_copy = ThreadInfo()

                for field in thread_entry._fields_:
                    setattr(thread_entry_copy, field[0], getattr(thread_entry, field[0]))

                thread_entry_copy.handle = _OpenThread(0x1F03FF, False, thread_entry.thread_id)

                start_address = c_void_p()
                _NtQueryInformationThread(thread_entry_copy.handle, 9, byref(start_address), sizeof(start_address), None)

                thread_entry_copy.start_address = start_address.value

                threads_list.append(thread_entry_copy)

            if not _Thread32Next(snapshot, byref(thread_entry)):
                break

        return threads_list

    def list_allocations(self) -> list[MemoryBasicInformation]:

        allocations_list = list()

        address = 0
        while True:

            try:
                allocation_info = self.virtual_query_ex(address)
                allocations_list.append(allocation_info)

                address += allocation_info.region_size

            except Exception:
                break

        return allocations_list

    def get_thread(self, thread_id: int) -> ThreadInfo:
        """Получает поток процесса."""

        found_thraed = None
        for thread in self.list_threads():

            if thread.thread_id == thread_id:
                found_thraed = thread

            else:

                try:
                    thread.close()

                except Exception:
                    pass

        if found_thraed:
            return thread

        else:
            raise Exception("Поток с указаным id не найден.")

    def virtual_query_ex(self, address: int) -> MemoryBasicInformation:
        """Получает информацию об указаном участке памяти."""

        memory_information = MemoryBasicInformation()
        if not _VirtualQueryEx(self.handle, address, byref(memory_information), sizeof(memory_information)):
            raise Exception("Не удалось получить информацию о участке памяти.")

        return memory_information

    def virtual_alloc_ex(self, size: int, allocation_type: MEM_COMMIT, protection: int = PAGE_EXECUTE_READWRITE, desired_location: int = None) -> None:
        """Выделяет участок памяти в процессе."""

        if address := _VirtualAllocEx(self.handle, desired_location, size, allocation_type, protection):
            return address

        else:
            raise Exception("Не удалось выделить участок памяти.")

    def virtual_free_ex(self, address: int, free_type: int = MEM_RELEASE, size: int = None) -> None:
        """Освобождает участок памяти в процессе."""

        if free_type == MEM_RELEASE:

            if not _VirtualFreeEx(self.handle, address, 0, free_type):
                raise Exception("Не удалось очистить участок памяти.")

        else:

            if size is None:
                raise Exception("Для очистки памяти необходимо указать размер.")

            if not _VirtualFreeEx(self.handle, address, self.virtual_query_ex(address).region_size, free_type):
                raise Exception("Не удалось очистить участок памяти.")

    def virtual_protect_ex(self, address: int, size: int, new_protection: int) -> None:
        """Устанавливает защиту на участок памяти."""

        if not _VirtualProtectEx(self.handle, address, size, new_protection, byref(c_ulong())):
            raise Exception("Не удалось установить защиту по участок памяти.")

    def read_ctypes_buffer(self, address: int, buffer: object) -> object:
        """Читает память процесса в ctypes буфер."""

        if not _ReadProcessMemory(self.handle, address, byref(buffer), sizeof(buffer), None):
            raise Exception("Не удалось прочитать память процесса.")

        return buffer

    def write_ctypes_buffer(self, address: int, buffer: object) -> None:
        """Записывает память процесса из ctypes буфера."""

        if not _WriteProcessMemory(self.handle, address, byref(buffer), sizeof(buffer), None):
            raise Exception("Не удалось записать память процесса.")

    def close(self) -> None:
        """Закрывает дескриптор процесса."""

        if not _CloseHandle(self.handle):
            raise Exception("Не удалось закрыть дескриптор процесса.")

    def pattern_scan(self, pattern: str, page_filter: list = [PAGE_READWRITE], return_first: bool = False) -> list[int] | int:
        """Сканирует память процесса и возвращает адреса проходящие по AOB сигнатуре.\n
        \"??\" указывает на случайный байт."""

        pattern = pattern.strip().split(" ")
        pattern = b"".join([bytes.fromhex(byte) if byte != "??" else b"." for byte in pattern])

        found_addresses = list()
        allocations = self.list_allocations()

        for allocation in allocations:

            if allocation.protect not in page_filter:
                continue

            allocation.base_address = 0 if allocation.base_address is None else allocation.base_address

            buffer = (c_byte * allocation.region_size)()
            self.read_ctypes_buffer(allocation.base_address, buffer)

            for regular_match in re.finditer(pattern, bytes(buffer), re.DOTALL):

                if return_first:
                    return allocation.base_address + regular_match.span()[0]

                found_addresses.append(allocation.base_address + regular_match.span()[0])

        return found_addresses


# Функции
def list_processes(close_handles_on_finish: bool = False) -> list[tuple[str, int]]:
    """Получает список всех активных процессов."""

    process_ids_buffer = (c_ulong * 4096)()
    bytes_needed = c_ulong()

    if not _EnumProcesses(process_ids_buffer, sizeof(process_ids_buffer), byref(bytes_needed)):
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
