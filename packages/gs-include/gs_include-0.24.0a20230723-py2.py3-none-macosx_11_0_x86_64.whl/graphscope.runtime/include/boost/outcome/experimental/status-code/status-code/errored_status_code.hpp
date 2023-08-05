/* Proposed SG14 status_code
(C) 2018-2023 Niall Douglas <http://www.nedproductions.biz/> (5 commits)
File Created: Jun 2018


Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
*/

#ifndef BOOST_OUTCOME_SYSTEM_ERROR2_ERRORED_STATUS_CODE_HPP
#define BOOST_OUTCOME_SYSTEM_ERROR2_ERRORED_STATUS_CODE_HPP

#include "quick_status_code_from_enum.hpp"
#include "status_code_ptr.hpp"

BOOST_OUTCOME_SYSTEM_ERROR2_NAMESPACE_BEGIN

/*! A `status_code` which is always a failure. The closest equivalent to
`std::error_code`, except it cannot be modified, and is templated.

Differences from `status_code`:

- Never successful (this contract is checked on construction, if fails then it
terminates the process).
- Is immutable.
*/
template <class DomainType> class errored_status_code : public status_code<DomainType>
{
  using _base = status_code<DomainType>;
  using _base::clear;
  using _base::success;

  void _check()
  {
    if(_base::success())
    {
      std::terminate();
    }
  }

public:
  //! The type of the domain.
  using typename _base::domain_type;
  //! The type of the error code.
  using typename _base::value_type;
  //! The type of a reference to a message string.
  using typename _base::string_ref;

  //! Default constructor.
  errored_status_code() = default;
  //! Copy constructor.
  errored_status_code(const errored_status_code &) = default;
  //! Move constructor.
  errored_status_code(errored_status_code &&) = default;  // NOLINT
  //! Copy assignment.
  errored_status_code &operator=(const errored_status_code &) = default;
  //! Move assignment.
  errored_status_code &operator=(errored_status_code &&) = default;  // NOLINT
  ~errored_status_code() = default;

  //! Explicitly construct from any similarly erased status code
  explicit errored_status_code(const _base &o) noexcept(std::is_nothrow_copy_constructible<_base>::value)
      : _base(o)
  {
    _check();
  }
  //! Explicitly construct from any similarly erased status code
  explicit errored_status_code(_base &&o) noexcept(std::is_nothrow_move_constructible<_base>::value)
      : _base(static_cast<_base &&>(o))
  {
    _check();
  }

  /***** KEEP THESE IN SYNC WITH STATUS_CODE *****/
  //! Implicit construction from any type where an ADL discovered `make_status_code(T, Args ...)` returns a `status_code`.
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(
  class T, class... Args,  //
  class MakeStatusCodeResult =
  typename detail::safe_get_make_status_code_result<T, Args...>::type)  // Safe ADL lookup of make_status_code(), returns void if not found
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(!std::is_same<typename std::decay<T>::type, errored_status_code>::value       // not copy/move of self
                                              && !std::is_same<typename std::decay<T>::type, in_place_t>::value             // not in_place_t
                                              && is_status_code<MakeStatusCodeResult>::value                                // ADL makes a status code
                                              && std::is_constructible<errored_status_code, MakeStatusCodeResult>::value))  // ADLed status code is compatible
  errored_status_code(T &&v, Args &&...args) noexcept(noexcept(make_status_code(std::declval<T>(), std::declval<Args>()...)))  // NOLINT
      : errored_status_code(make_status_code(static_cast<T &&>(v), static_cast<Args &&>(args)...))
  {
    _check();
  }

  //! Implicit construction from any `quick_status_code_from_enum<Enum>` enumerated type.
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class Enum,                                                                                      //
                         class QuickStatusCodeType = typename quick_status_code_from_enum<Enum>::code_type)               // Enumeration has been activated
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(std::is_constructible<errored_status_code, QuickStatusCodeType>::value))    // Its status code is compatible
  errored_status_code(Enum &&v) noexcept(std::is_nothrow_constructible<errored_status_code, QuickStatusCodeType>::value)  // NOLINT
      : errored_status_code(QuickStatusCodeType(static_cast<Enum &&>(v)))
  {
    _check();
  }
  //! Explicit in-place construction.
  template <class... Args>
  explicit errored_status_code(in_place_t _, Args &&...args) noexcept(std::is_nothrow_constructible<value_type, Args &&...>::value)
      : _base(_, static_cast<Args &&>(args)...)
  {
    _check();
  }
  //! Explicit in-place construction from initialiser list.
  template <class T, class... Args>
  explicit errored_status_code(in_place_t _, std::initializer_list<T> il,
                               Args &&...args) noexcept(std::is_nothrow_constructible<value_type, std::initializer_list<T>, Args &&...>::value)
      : _base(_, il, static_cast<Args &&>(args)...)
  {
    _check();
  }
  //! Explicit copy construction from a `value_type`.
  explicit errored_status_code(const value_type &v) noexcept(std::is_nothrow_copy_constructible<value_type>::value)
      : _base(v)
  {
    _check();
  }
  //! Explicit move construction from a `value_type`.
  explicit errored_status_code(value_type &&v) noexcept(std::is_nothrow_move_constructible<value_type>::value)
      : _base(static_cast<value_type &&>(v))
  {
    _check();
  }
  /*! Explicit construction from an erased status code. Available only if
  `value_type` is trivially copyable or move bitcopying, and `sizeof(status_code) <= sizeof(status_code<erased<>>)`.
  Does not check if domains are equal.
  */
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class ErasedType)  //
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(detail::domain_value_type_erasure_is_safe<domain_type, erased<ErasedType>>::value))
  explicit errored_status_code(const status_code<erased<ErasedType>> &v) noexcept(std::is_nothrow_copy_constructible<value_type>::value)
      : errored_status_code(detail::erasure_cast<value_type>(v.value()))  // NOLINT
  {
    assert(v.domain() == this->domain());  // NOLINT
    _check();
  }

  //! Always false (including at compile time), as errored status codes are never successful.
  constexpr bool success() const noexcept { return false; }
  //! Return a const reference to the `value_type`.
  constexpr const value_type &value() const &noexcept { return this->_value; }
};

namespace traits
{
  template <class DomainType> struct is_move_bitcopying<errored_status_code<DomainType>>
  {
    static constexpr bool value = is_move_bitcopying<typename DomainType::value_type>::value;
  };
}  // namespace traits

template <class ErasedType> class errored_status_code<erased<ErasedType>> : public status_code<erased<ErasedType>>
{
  using _base = status_code<erased<ErasedType>>;
  using _base::success;

  void _check()
  {
    if(_base::success())
    {
      std::terminate();
    }
  }

public:
  using domain_type = typename _base::domain_type;
  using value_type = typename _base::value_type;
  using string_ref = typename _base::string_ref;

  //! Default construction to empty
  errored_status_code() = default;
  //! Copy constructor
  errored_status_code(const errored_status_code &) = default;
  //! Move constructor
  errored_status_code(errored_status_code &&) = default;  // NOLINT
                                                          //! Copy assignment
  errored_status_code &operator=(const errored_status_code &) = default;
  //! Move assignment
  errored_status_code &operator=(errored_status_code &&) = default;  // NOLINT
  ~errored_status_code() = default;

  //! Explicitly construct from any similarly erased status code
  explicit errored_status_code(const _base &o) noexcept(std::is_nothrow_copy_constructible<_base>::value)
      : _base(o)
  {
    _check();
  }
  //! Explicitly construct from any similarly erased status code
  explicit errored_status_code(_base &&o) noexcept(std::is_nothrow_move_constructible<_base>::value)
      : _base(static_cast<_base &&>(o))
  {
    _check();
  }

  /***** KEEP THESE IN SYNC WITH STATUS_CODE *****/
  //! Implicit copy construction from any other status code if its value type is trivially copyable, it would fit into our storage, and it is not an erased
  //! status code.
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class DomainType)  //
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(detail::domain_value_type_erasure_is_safe<erased<ErasedType>, DomainType>::value),
                          BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(!detail::is_erased_status_code<status_code<typename std::decay<DomainType>::type>>::value))
  errored_status_code(const status_code<DomainType> &v) noexcept
      : _base(v)  // NOLINT
  {
    _check();
  }
  //! Implicit copy construction from any other status code if its value type is trivially copyable and it would fit into our storage, and it is not an erased
  //! status code.
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class DomainType)  //
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(detail::domain_value_type_erasure_is_safe<erased<ErasedType>, DomainType>::value),
                          BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(!detail::is_erased_status_code<status_code<typename std::decay<DomainType>::type>>::value))
  errored_status_code(const errored_status_code<DomainType> &v) noexcept
      : _base(static_cast<const status_code<DomainType> &>(v))  // NOLINT
  {
    _check();
  }
  //! Implicit move construction from any other status code if its value type is trivially copyable or move bitcopying and it would fit into our storage
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class DomainType)  //
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(detail::domain_value_type_erasure_is_safe<erased<ErasedType>, DomainType>::value))
  errored_status_code(status_code<DomainType> &&v) noexcept
      : _base(static_cast<status_code<DomainType> &&>(v))  // NOLINT
  {
    _check();
  }
  //! Implicit move construction from any other status code if its value type is trivially copyable or move bitcopying and it would fit into our storage
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class DomainType)  //
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(detail::domain_value_type_erasure_is_safe<erased<ErasedType>, DomainType>::value))
  errored_status_code(errored_status_code<DomainType> &&v) noexcept
      : _base(static_cast<status_code<DomainType> &&>(v))  // NOLINT
  {
    _check();
  }
  //! Implicit construction from any type where an ADL discovered `make_status_code(T, Args ...)` returns a `status_code`.
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(
  class T, class... Args,  //
  class MakeStatusCodeResult =
  typename detail::safe_get_make_status_code_result<T, Args...>::type)  // Safe ADL lookup of make_status_code(), returns void if not found
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(!std::is_same<typename std::decay<T>::type, errored_status_code>::value       // not copy/move of self
                                              && !std::is_same<typename std::decay<T>::type, value_type>::value             // not copy/move of value type
                                              && is_status_code<MakeStatusCodeResult>::value                                // ADL makes a status code
                                              && std::is_constructible<errored_status_code, MakeStatusCodeResult>::value))  // ADLed status code is compatible
  errored_status_code(T &&v, Args &&...args) noexcept(noexcept(make_status_code(std::declval<T>(), std::declval<Args>()...)))  // NOLINT
      : errored_status_code(make_status_code(static_cast<T &&>(v), static_cast<Args &&>(args)...))
  {
    _check();
  }
  //! Implicit construction from any `quick_status_code_from_enum<Enum>` enumerated type.
  BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class Enum,                                                                                      //
                         class QuickStatusCodeType = typename quick_status_code_from_enum<Enum>::code_type)               // Enumeration has been activated
  BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(std::is_constructible<errored_status_code, QuickStatusCodeType>::value))    // Its status code is compatible
  errored_status_code(Enum &&v) noexcept(std::is_nothrow_constructible<errored_status_code, QuickStatusCodeType>::value)  // NOLINT
      : errored_status_code(QuickStatusCodeType(static_cast<Enum &&>(v)))
  {
    _check();
  }
#if defined(_CPPUNWIND) || defined(__EXCEPTIONS) || defined(BOOST_OUTCOME_STANDARDESE_IS_IN_THE_HOUSE)
  //! Explicit copy construction from an unknown status code. Note that this will be empty if its value type is not trivially copyable or would not fit into our
  //! storage or the source domain's `_do_erased_copy()` refused the copy.
  explicit errored_status_code(const status_code<void> &v)  // NOLINT
      : _base(v)
  {
    _check();
  }
#endif

  //! Always false (including at compile time), as errored status codes are never successful.
  constexpr bool success() const noexcept { return false; }
  //! Return the erased `value_type` by value.
  constexpr value_type value() const noexcept { return this->_value; }
};

namespace traits
{
  template <class ErasedType> struct is_move_bitcopying<errored_status_code<erased<ErasedType>>>
  {
    static constexpr bool value = true;
  };
}  // namespace traits


//! True if the status code's are semantically equal via `equivalent()`.
template <class DomainType1, class DomainType2>
inline bool operator==(const errored_status_code<DomainType1> &a, const errored_status_code<DomainType2> &b) noexcept
{
  return a.equivalent(static_cast<const status_code<DomainType2> &>(b));
}
//! True if the status code's are semantically equal via `equivalent()`.
template <class DomainType1, class DomainType2> inline bool operator==(const status_code<DomainType1> &a, const errored_status_code<DomainType2> &b) noexcept
{
  return a.equivalent(static_cast<const status_code<DomainType2> &>(b));
}
//! True if the status code's are semantically equal via `equivalent()`.
template <class DomainType1, class DomainType2> inline bool operator==(const errored_status_code<DomainType1> &a, const status_code<DomainType2> &b) noexcept
{
  return static_cast<const status_code<DomainType1> &>(a).equivalent(b);
}
//! True if the status code's are not semantically equal via `equivalent()`.
template <class DomainType1, class DomainType2>
inline bool operator!=(const errored_status_code<DomainType1> &a, const errored_status_code<DomainType2> &b) noexcept
{
  return !a.equivalent(static_cast<const status_code<DomainType2> &>(b));
}
//! True if the status code's are not semantically equal via `equivalent()`.
template <class DomainType1, class DomainType2> inline bool operator!=(const status_code<DomainType1> &a, const errored_status_code<DomainType2> &b) noexcept
{
  return !a.equivalent(static_cast<const status_code<DomainType2> &>(b));
}
//! True if the status code's are not semantically equal via `equivalent()`.
template <class DomainType1, class DomainType2> inline bool operator!=(const errored_status_code<DomainType1> &a, const status_code<DomainType2> &b) noexcept
{
  return !static_cast<const status_code<DomainType1> &>(a).equivalent(b);
}
//! True if the status code's are semantically equal via `equivalent()` to `make_status_code(T)`.
BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class DomainType1, class T,  //
                       class MakeStatusCodeResult =
                       typename detail::safe_get_make_status_code_result<const T &>::type)  // Safe ADL lookup of make_status_code(), returns void if not found
BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(is_status_code<MakeStatusCodeResult>::value))   // ADL makes a status code
inline bool operator==(const errored_status_code<DomainType1> &a, const T &b)
{
  return a.equivalent(make_status_code(b));
}
//! True if the status code's are semantically equal via `equivalent()` to `make_status_code(T)`.
BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class T, class DomainType1,  //
                       class MakeStatusCodeResult =
                       typename detail::safe_get_make_status_code_result<const T &>::type)  // Safe ADL lookup of make_status_code(), returns void if not found
BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(is_status_code<MakeStatusCodeResult>::value))   // ADL makes a status code
inline bool operator==(const T &a, const errored_status_code<DomainType1> &b)
{
  return b.equivalent(make_status_code(a));
}
//! True if the status code's are not semantically equal via `equivalent()` to `make_status_code(T)`.
BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class DomainType1, class T,  //
                       class MakeStatusCodeResult =
                       typename detail::safe_get_make_status_code_result<const T &>::type)  // Safe ADL lookup of make_status_code(), returns void if not found
BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(is_status_code<MakeStatusCodeResult>::value))   // ADL makes a status code
inline bool operator!=(const errored_status_code<DomainType1> &a, const T &b)
{
  return !a.equivalent(make_status_code(b));
}
//! True if the status code's are semantically equal via `equivalent()` to `make_status_code(T)`.
BOOST_OUTCOME_SYSTEM_ERROR2_TEMPLATE(class T, class DomainType1,  //
                       class MakeStatusCodeResult =
                       typename detail::safe_get_make_status_code_result<const T &>::type)  // Safe ADL lookup of make_status_code(), returns void if not found
BOOST_OUTCOME_SYSTEM_ERROR2_TREQUIRES(BOOST_OUTCOME_SYSTEM_ERROR2_TPRED(is_status_code<MakeStatusCodeResult>::value))   // ADL makes a status code
inline bool operator!=(const T &a, const errored_status_code<DomainType1> &b)
{
  return !b.equivalent(make_status_code(a));
}
//! True if the status code's are semantically equal via `equivalent()` to `quick_status_code_from_enum<T>::code_type(b)`.
template <class DomainType1, class T,                                                     //
          class QuickStatusCodeType = typename quick_status_code_from_enum<T>::code_type  // Enumeration has been activated
          >
inline bool operator==(const errored_status_code<DomainType1> &a, const T &b)
{
  return a.equivalent(QuickStatusCodeType(b));
}
//! True if the status code's are semantically equal via `equivalent()` to `quick_status_code_from_enum<T>::code_type(a)`.
template <class T, class DomainType1,                                                     //
          class QuickStatusCodeType = typename quick_status_code_from_enum<T>::code_type  // Enumeration has been activated
          >
inline bool operator==(const T &a, const errored_status_code<DomainType1> &b)
{
  return b.equivalent(QuickStatusCodeType(a));
}
//! True if the status code's are not semantically equal via `equivalent()` to `quick_status_code_from_enum<T>::code_type(b)`.
template <class DomainType1, class T,                                                     //
          class QuickStatusCodeType = typename quick_status_code_from_enum<T>::code_type  // Enumeration has been activated
          >
inline bool operator!=(const errored_status_code<DomainType1> &a, const T &b)
{
  return !a.equivalent(QuickStatusCodeType(b));
}
//! True if the status code's are not semantically equal via `equivalent()` to `quick_status_code_from_enum<T>::code_type(a)`.
template <class T, class DomainType1,                                                     //
          class QuickStatusCodeType = typename quick_status_code_from_enum<T>::code_type  // Enumeration has been activated
          >
inline bool operator!=(const T &a, const errored_status_code<DomainType1> &b)
{
  return !b.equivalent(QuickStatusCodeType(a));
}


namespace detail
{
  template <class T> struct is_errored_status_code
  {
    static constexpr bool value = false;
  };
  template <class T> struct is_errored_status_code<errored_status_code<T>>
  {
    static constexpr bool value = true;
  };
  template <class T> struct is_erased_errored_status_code
  {
    static constexpr bool value = false;
  };
  template <class T> struct is_erased_errored_status_code<errored_status_code<erased<T>>>
  {
    static constexpr bool value = true;
  };
}  // namespace detail

//! Trait returning true if the type is an errored status code.
template <class T> struct is_errored_status_code
{
  static constexpr bool value =
  detail::is_errored_status_code<typename std::decay<T>::type>::value || detail::is_erased_errored_status_code<typename std::decay<T>::type>::value;
};


BOOST_OUTCOME_SYSTEM_ERROR2_NAMESPACE_END

#endif
