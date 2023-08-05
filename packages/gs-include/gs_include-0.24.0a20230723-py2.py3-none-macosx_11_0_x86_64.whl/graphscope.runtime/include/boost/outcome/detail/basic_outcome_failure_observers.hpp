/* Failure observers for outcome type
(C) 2017-2023 Niall Douglas <http://www.nedproductions.biz/> (7 commits)
File Created: Oct 2017


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

#ifndef BOOST_OUTCOME_BASIC_OUTCOME_FAILURE_OBSERVERS_HPP
#define BOOST_OUTCOME_BASIC_OUTCOME_FAILURE_OBSERVERS_HPP

#include "basic_result_storage.hpp"

#include <exception>

BOOST_OUTCOME_V2_NAMESPACE_EXPORT_BEGIN

namespace detail
{
  namespace adl
  {
    struct search_detail_adl
    {
    };
    // Do NOT use template requirements here!
    template <class S, typename = decltype(basic_outcome_failure_exception_from_error(std::declval<S>()))>
    inline auto _delayed_lookup_basic_outcome_failure_exception_from_error(const S &ec, search_detail_adl /*unused*/)
    {
      // ADL discovered
      return basic_outcome_failure_exception_from_error(ec);
    }
  }                                        // namespace adl
#if defined(_MSC_VER) && _MSC_VER <= 1923  // VS2019
  // VS2017 and VS2019 with /permissive- chokes on the correct form due to over eager early instantiation.
  template <class S, class P> inline void _delayed_lookup_basic_outcome_failure_exception_from_error(...) { static_assert(sizeof(S) == 0, "No specialisation for these error and exception types available!"); }
#else
  template <class S, class P> inline void _delayed_lookup_basic_outcome_failure_exception_from_error(...) = delete;  // NOLINT No specialisation for these error and exception types available!
#endif

  template <class exception_type> inline exception_type current_exception_or_fatal(std::exception_ptr e) { std::rethrow_exception(e); }
  template <> inline std::exception_ptr current_exception_or_fatal<std::exception_ptr>(std::exception_ptr e) { return e; }

  template <class Base, class R, class S, class P, class NoValuePolicy> class basic_outcome_failure_observers : public Base
  {
  public:
    using exception_type = P;
    using Base::Base;

    exception_type failure() const noexcept
    {
#ifndef BOOST_NO_EXCEPTIONS
      try
#endif
      {
        if(this->_state._status.have_exception())
        {
          return this->assume_exception();
        }
        if(this->_state._status.have_error())
        {
          return _delayed_lookup_basic_outcome_failure_exception_from_error(this->assume_error(), adl::search_detail_adl());
        }
        return exception_type();
      }
#ifndef BOOST_NO_EXCEPTIONS
      catch(...)
      {
        // Return the failure if exception_type is std::exception_ptr,
        // otherwise terminate same as throwing an exception inside noexcept
        return current_exception_or_fatal<exception_type>(std::current_exception());
      }
#endif
    }
  };

}  // namespace detail

BOOST_OUTCOME_V2_NAMESPACE_END

#endif
