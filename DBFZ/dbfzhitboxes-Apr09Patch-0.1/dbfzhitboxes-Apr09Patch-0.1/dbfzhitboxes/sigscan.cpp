#include "sigscan.h"
#include <stdexcept>
#include <Windows.h>
#include <Psapi.h>

sigscan::sigscan(const char *name)
{
	const auto module = GetModuleHandle(name);
	if (module == nullptr)
		throw std::runtime_error("Module not found");

	MODULEINFO info;
	GetModuleInformation(GetCurrentProcess(), module, &info, sizeof(info));
	start = (uintptr_t)(info.lpBaseOfDll);
	end = start + info.SizeOfImage;
}

uintptr_t sigscan::sig(const char *sig, const char *mask)
{
	const auto last_scan = end - strlen(mask) + 1;
	for (auto addr = start; addr < last_scan; addr++) {
		for (size_t i = 0;; i++) {
			if (mask[i] == '\0')
				return addr;
			if (mask[i] != '?' && sig[i] != *(char*)(addr + i))
				break;
		}
	}
	throw std::runtime_error("Sigscan failed");
}
