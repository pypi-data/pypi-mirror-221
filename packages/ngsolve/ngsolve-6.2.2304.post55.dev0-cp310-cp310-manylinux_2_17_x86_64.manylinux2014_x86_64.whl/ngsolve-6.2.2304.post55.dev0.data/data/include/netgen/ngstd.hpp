#ifndef FILE_NGSTD
#define FILE_NGSTD

/*********************************************************************/
/* File:   ngstd.hpp                                                 */
/* Author: Joachim Schoeberl                                         */
/* Date:   25. Mar. 2000                                             */
/*********************************************************************/

/* 
   ng-standard classes
*/

#include <ngs_stdcpp_include.hpp>

/*
inline void * operator new (size_t cnt)
{
  static int cnt_new = 0;
  cnt_new++;
  std::cout << "private new called, cnt = " << cnt_new << ", bytes = " << cnt << std::endl;
  return operator new(cnt, std::nothrow);
}

inline void * operator new[] (size_t cnt)
{
  static int cnt_new = 0;
  cnt_new++;
  std::cout << "private new[] called, cnt = " << cnt_new << ", bytes = " << cnt << std::endl;
  return operator new[](cnt, std::nothrow);
}
*/





// #include "dynamicmem.hpp"


namespace ngstd
{
  // NGS_DLL_HEADER extern int printmessage_importance;
  NGS_DLL_HEADER extern const std::string ngsolve_version;
}



/*
namespace ngstd
{
  using netgen::DynamicMem;
}
*/


/**
   namespace for standard data types and algorithms.

   Generic container classes: FlatArray, Array, ArrayMem

Specific data types Exception, BlockAllocator, AutoPtr, EvalFunction, AutoDiff, AutoDiffDiff
*/


#include <ngs_defines.hpp>

// #include "mycomplex.hpp"  
#include <core/ngcore.hpp>
namespace ngstd
{
  using namespace ngcore;
  using ngcore::INT;
} // namespace ngstd

#include "ngs_utils.hpp"
// #include "ngsstream.hpp"  
// #include "templates.hpp" // nothing in anymore

// #include "simd_complex.hpp"

#include "blockalloc.hpp"
// #include "autoptr.hpp"
#include "memusage.hpp"

#include "evalfunc.hpp"
#include "sample_sort.hpp"

#include "autodiff.hpp"
#include "autodiffdiff.hpp"
#include "polorder.hpp"
#include "stringops.hpp"
#include "statushandler.hpp"

#ifndef WIN32
#include "sockets.hpp"
#endif

namespace ngstd
{
#ifdef WIN32
  const char dirslash = '\\';
#else
  const char dirslash = '/';
#endif

  
  using ngcore::NgMPI_Comm;
  enum { MPI_TAG_CMD = 110 };
  enum { MPI_TAG_SOLVE = 1110 };
}


inline void NOOP_Deleter(void *) { ; }

#endif
