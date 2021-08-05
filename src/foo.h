#pragma once

#ifdef WIN32
  #define foo_EXPORT __declspec(dllexport)
#else
  #define foo_EXPORT
#endif

foo_EXPORT void foo();
