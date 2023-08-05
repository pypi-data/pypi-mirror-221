/**
 * atax.h: This file is part of the PolyBench/C 3.2 test suite.
 *
 *
 * Contact: Louis-Noel Pouchet <pouchet@cse.ohio-state.edu>
 * Web address: http://polybench.sourceforge.net
 */
#ifndef ATAX_H
# define ATAX_H

/* Default to STANDARD_DATASET. */
# if !defined(MINI_DATASET) && !defined(SMALL_DATASET) && !defined(LARGE_DATASET) && !defined(EXTRALARGE_DATASET)
#  define STANDARD_DATASET
# endif

/* Do not define anything if the user manually defines the size. */
# if !defined(NX) && !defined(NY)
/* Define the possible dataset sizes. */
#  ifdef MINI_DATASET
#   define NX 32
#   define NY 32
#  endif

#  ifdef SMALL_DATASET
#   define NX 500
#   define NY 500
#  endif

#  ifdef STANDARD_DATASET /* Default if unspecified. */
#   define NX 4000
#   define NY 4000
#  endif

#  ifdef LARGE_DATASET
#   define NX 8000
#   define NY 8000
#  endif

#  ifdef EXTRALARGE_DATASET
#   define NX 100000
#   define NY 100000
#  endif
# endif /* !N */

# define _PB_NX POLYBENCH_LOOP_BOUND(NX,nx)
# define _PB_NY POLYBENCH_LOOP_BOUND(NY,ny)

# ifndef DATA_TYPE
#  define DATA_TYPE double
# endif

# if DATA_TYPE == double
#  define DATA_PRINTF_MODIFIER "%0.2lf "
# elif DATA_TYPE == float
#  define DATA_PRINTF_MODIFIER "%0.2f "
# elif DATA_TYPE == long
#  define DATA_PRINTF_MODIFIER "%0.2u "
# elif DATA_TYPE == int
#  define DATA_PRINTF_MODIFIER "%0.2u "
# endif

#define M_PI 3.14159265358979323846 

#endif /* !ATAX */
