// -----------------------------------------------------------
//
//   Copyright (c) 2001-2002 Chuck Allison and Jeremy Siek
//   Copyright (c) 2003-2006, 2008 Gennaro Prota
//   Copyright (c) 2014 Glen Joseph Fernandes
//       (glenjofe@gmail.com)
//   Copyright (c) 2018 Evgeny Shulgin
//   Copyright (c) 2019 Andrey Semashev
//
// Distributed under the Boost Software License, Version 1.0.
//    (See accompanying file LICENSE_1_0.txt or copy at
//          http://www.boost.org/LICENSE_1_0.txt)
//
// -----------------------------------------------------------

#ifndef BOOST_DETAIL_DYNAMIC_BITSET_HPP
#define BOOST_DETAIL_DYNAMIC_BITSET_HPP

#include <memory>
#include <cstddef>
#include "boost/config.hpp"
#include "boost/detail/workaround.hpp"
#include <boost/core/allocator_access.hpp>

#if ((defined(BOOST_MSVC) && (BOOST_MSVC >= 1600)) || (defined(__clang__) && defined(__c2__)) || (defined(BOOST_INTEL) && defined(_MSC_VER))) && (defined(_M_IX86) || defined(_M_X64))
#include <intrin.h>
#endif

namespace boost {

  namespace detail {
  namespace dynamic_bitset_impl {

    template<class T>
    struct max_limit {
        BOOST_STATIC_CONSTEXPR T value = static_cast<T>(-1);
    };

    template<class T>
    BOOST_CONSTEXPR_OR_CONST T max_limit<T>::value;

    // Gives (read-)access to the object representation
    // of an object of type T (3.9p4). CANNOT be used
    // on a base sub-object
    //
    template <typename T>
    inline const unsigned char * object_representation (T* p)
    {
        return static_cast<const unsigned char *>(static_cast<const void *>(p));
    }

    template<typename T, int amount, int width /* = default */>
    struct shifter
    {
        static void left_shift(T & v) {
            amount >= width ? (v = 0)
                : (v >>= BOOST_DYNAMIC_BITSET_WRAP_CONSTANT(amount));
        }
    };

    // ------- count function implementation --------------

    typedef unsigned char byte_type;

    // These two entities
    //
    //     enum mode { access_by_bytes, access_by_blocks };
    //     template <mode> struct mode_to_type {};
    //
    // were removed, since the regression logs (as of 24 Aug 2008)
    // showed that several compilers had troubles with recognizing
    //
    //   const mode m = access_by_bytes
    //
    // as a constant expression
    //
    // * So, we'll use bool, instead of enum *.
    //
    template <bool value>
    struct value_to_type
    {
        value_to_type() {}
    };
    const bool access_by_bytes = true;
    const bool access_by_blocks = false;


    // the table: wrapped in a class template, so
    // that it is only instantiated if/when needed
    //
    template <bool dummy_name = true>
    struct count_table { static const byte_type table[]; };

    template <>
    struct count_table<false> { /* no table */ };


    const unsigned int table_width = 8;
    template <bool b>
    const byte_type count_table<b>::table[] =
    {
        // Automatically generated by GPTableGen.exe v.1.0
        //
        0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
    };


    // Some platforms have fast popcount operation, that allow us to implement
    // counting bits much more efficiently
    //
    template <typename ValueType>
    BOOST_FORCEINLINE std::size_t popcount(ValueType value) BOOST_NOEXCEPT
    {
        std::size_t num = 0u;
        while (value) {
            num += count_table<>::table[value & ((1u<<table_width) - 1)];
            value >>= table_width;
        }
        return num;
    }

#if (((defined(BOOST_MSVC) && (BOOST_MSVC >= 1600)) || (defined(__clang__) && defined(__c2__)) || (defined(BOOST_INTEL) && defined(_MSC_VER))) && (defined(_M_IX86) || defined(_M_X64))) \
    && (defined(__POPCNT__) || defined(__AVX__))

    template <>
    BOOST_FORCEINLINE std::size_t popcount<unsigned short>(unsigned short value) BOOST_NOEXCEPT
    {
        return static_cast<std::size_t>(__popcnt16(value));
    }

    template <>
    BOOST_FORCEINLINE std::size_t popcount<unsigned int>(unsigned int value) BOOST_NOEXCEPT
    {
        return static_cast<std::size_t>(__popcnt(value));
    }

    template <>
    BOOST_FORCEINLINE std::size_t popcount<unsigned __int64>(unsigned __int64 value) BOOST_NOEXCEPT
    {
#if defined(_M_X64)
        return static_cast<std::size_t>(__popcnt64(value));
#else
        return static_cast<std::size_t>(__popcnt(static_cast< unsigned int >(value))) + static_cast<std::size_t>(__popcnt(static_cast< unsigned int >(value >> 32)));
#endif
    }

#elif defined(BOOST_GCC) || defined(__clang__) || (defined(BOOST_INTEL) && defined(__GNUC__))

    // Note: gcc builtins are implemented by compiler runtime when the target CPU may not support the necessary instructions
    template <>
    BOOST_FORCEINLINE std::size_t popcount<unsigned short>(unsigned short value) BOOST_NOEXCEPT
    {
        return static_cast<unsigned int>(__builtin_popcount(static_cast<unsigned int>(value)));
    }

    template <>
    BOOST_FORCEINLINE std::size_t popcount<unsigned int>(unsigned int value) BOOST_NOEXCEPT
    {
        return static_cast<unsigned int>(__builtin_popcount(value));
    }

    template <>
    BOOST_FORCEINLINE std::size_t popcount<unsigned long>(unsigned long value) BOOST_NOEXCEPT
    {
        return static_cast<unsigned int>(__builtin_popcountl(value));
    }

    template <>
    BOOST_FORCEINLINE std::size_t popcount<boost::ulong_long_type>(boost::ulong_long_type value) BOOST_NOEXCEPT
    {
        return static_cast<unsigned int>(__builtin_popcountll(value));
    }

#endif

    // overload for access by blocks
    //
    template <typename Iterator, typename ValueType>
    inline std::size_t do_count(Iterator first, std::size_t length, ValueType,
                                value_to_type<access_by_blocks>*)
    {
        std::size_t num1 = 0u, num2 = 0u;
        while (length >= 2u) {
            num1 += popcount<ValueType>(*first);
            ++first;
            num2 += popcount<ValueType>(*first);
            ++first;
            length -= 2u;
        }

        if (length > 0u)
            num1 += popcount<ValueType>(*first);

        return num1 + num2;
    }

    // overload for access by bytes
    //
    template <typename Iterator>
    inline std::size_t do_count(Iterator first, std::size_t length,
                                int /*dummy param*/,
                                value_to_type<access_by_bytes>*)
    {
        if (length > 0u) {
            const byte_type* p = object_representation(&*first);
            length *= sizeof(*first);

            return do_count(p, length, static_cast<byte_type>(0u),
                static_cast< value_to_type<access_by_blocks>* >(0));
        }

        return 0u;
    }

    // -------------------------------------------------------


    // Some library implementations simply return a dummy
    // value such as
    //
    //   size_type(-1) / sizeof(T)
    //
    // from vector<>::max_size. This tries to get more
    // meaningful info.
    //
    template <typename T>
    inline typename T::size_type vector_max_size_workaround(const T & v)
        BOOST_NOEXCEPT
    {
        typedef typename T::allocator_type allocator_type;

        const allocator_type& alloc = v.get_allocator();

        typename boost::allocator_size_type<allocator_type>::type alloc_max =
            boost::allocator_max_size(alloc);

        const typename T::size_type container_max = v.max_size();

        return alloc_max < container_max ? alloc_max : container_max;
    }

    // for static_asserts
    template <typename T>
    struct allowed_block_type {
        enum { value = T(-1) > 0 }; // ensure T has no sign
    };

    template <>
    struct allowed_block_type<bool> {
        enum { value = false };
    };


    template <typename T>
    struct is_numeric {
        enum { value = false };
    };

#   define BOOST_dynamic_bitset_is_numeric(x)       \
                template<>                          \
                struct is_numeric< x > {            \
                    enum { value = true };          \
                }                                /**/

    BOOST_dynamic_bitset_is_numeric(bool);
    BOOST_dynamic_bitset_is_numeric(char);

#if !defined(BOOST_NO_INTRINSIC_WCHAR_T)
    BOOST_dynamic_bitset_is_numeric(wchar_t);
#endif

    BOOST_dynamic_bitset_is_numeric(signed char);
    BOOST_dynamic_bitset_is_numeric(short int);
    BOOST_dynamic_bitset_is_numeric(int);
    BOOST_dynamic_bitset_is_numeric(long int);

    BOOST_dynamic_bitset_is_numeric(unsigned char);
    BOOST_dynamic_bitset_is_numeric(unsigned short);
    BOOST_dynamic_bitset_is_numeric(unsigned int);
    BOOST_dynamic_bitset_is_numeric(unsigned long);

#if defined(BOOST_HAS_LONG_LONG)
    BOOST_dynamic_bitset_is_numeric(::boost::long_long_type);
    BOOST_dynamic_bitset_is_numeric(::boost::ulong_long_type);
#endif

    // intentionally omitted
    //BOOST_dynamic_bitset_is_numeric(float);
    //BOOST_dynamic_bitset_is_numeric(double);
    //BOOST_dynamic_bitset_is_numeric(long double);

#undef BOOST_dynamic_bitset_is_numeric

  } // dynamic_bitset_impl
  } // namespace detail

} // namespace boost

#endif // include guard

