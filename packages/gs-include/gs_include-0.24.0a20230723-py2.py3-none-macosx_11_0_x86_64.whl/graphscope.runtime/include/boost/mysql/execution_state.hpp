//
// Copyright (c) 2019-2023 Ruben Perez Hidalgo (rubenperez038 at gmail dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//

#ifndef BOOST_MYSQL_EXECUTION_STATE_HPP
#define BOOST_MYSQL_EXECUTION_STATE_HPP

#include <boost/mysql/metadata.hpp>
#include <boost/mysql/metadata_collection_view.hpp>
#include <boost/mysql/string_view.hpp>

#include <boost/mysql/detail/auxiliar/access_fwd.hpp>
#include <boost/mysql/detail/protocol/common_messages.hpp>
#include <boost/mysql/detail/protocol/resultset_encoding.hpp>

#include <cassert>
#include <cstddef>
#include <cstdint>
#include <vector>

namespace boost {
namespace mysql {

/**
 * \brief Holds state for multi-function SQL execution operations.
 * \par Thread safety
 * Distinct objects: safe. \n
 * Shared objects: unsafe.
 */
class execution_state
{
public:
    /**
     * \brief Default constructor.
     * \details The constructed object is guaranteed to have `meta().empty()` and
     * `!complete()`.
     *
     * \par Exception safety
     * No-throw guarantee.
     */
    execution_state() = default;

    /**
     * \brief Returns whether all the messages generated by this operation have been read.
     * \details
     * Once `complete`, you may access extra information about the operation, like
     * \ref affected_rows or \ref last_insert_id.
     *
     * \par Exception safety
     * No-throw guarantee.
     */
    bool complete() const noexcept { return eof_received_; }

    /**
     * \brief Returns metadata about the columns in the query.
     * \details
     * The returned collection will have as many \ref metadata objects as columns retrieved by
     * the SQL query, and in the same order.
     *
     * \par Exception safety
     * No-throw guarantee.
     *
     * \par Object lifetimes
     * This function returns a view object, with reference semantics. The returned view points into
     * memory owned by `*this`, and will be valid as long as `*this` or an object move-constructed
     * from `*this` are alive.
     */
    metadata_collection_view meta() const noexcept
    {
        return metadata_collection_view(meta_.data(), meta_.size());
    }

    /**
     * \brief Returns the number of rows affected by the executed SQL statement.
     * \par Exception safety
     * No-throw guarantee.
     *
     * \par Preconditions
     * `this->complete() == true`
     */
    std::uint64_t affected_rows() const noexcept
    {
        assert(complete());
        return affected_rows_;
    }

    /**
     * \brief Returns the last insert ID produced by the executed SQL statement.
     * \par Exception safety
     * No-throw guarantee.
     *
     * \par Preconditions
     * `this->complete() == true`
     */
    std::uint64_t last_insert_id() const noexcept
    {
        assert(complete());
        return last_insert_id_;
    }

    /**
     * \brief Returns the number of warnings produced by the executed SQL statement.
     * \par Exception safety
     * No-throw guarantee.
     *
     * \par Preconditions
     * `this->complete() == true`
     */
    unsigned warning_count() const noexcept
    {
        assert(complete());
        return warnings_;
    }

    /**
     * \brief Returns additionat text information about the execution of the SQL statement.
     * \details
     * The format of this information is documented by MySQL <a
     * href="https://dev.mysql.com/doc/c-api/8.0/en/mysql-info.html">here</a>.
     * \n
     * The returned string always uses ASCII encoding, regardless of the connection's character set.
     *
     * \par Exception safety
     * No-throw guarantee.
     *
     * \par Preconditions
     * `this->complete() == true`
     *
     * \par Object lifetimes
     * This function returns a view object, with reference semantics. The returned view points into
     * memory owned by `*this`, and will be valid as long as `*this` or an object move-constructed
     * from `*this` are alive.
     */
    string_view info() const noexcept
    {
        assert(complete());
        return string_view(info_.data(), info_.size());
    }

private:
    bool eof_received_{false};
    std::uint8_t seqnum_{};
    detail::resultset_encoding encoding_{detail::resultset_encoding::text};
    std::vector<metadata> meta_;
    std::uint64_t affected_rows_{};
    std::uint64_t last_insert_id_{};
    std::uint16_t warnings_{};
    std::vector<char> info_;  // guarantee that no SBO is used

#ifndef BOOST_MYSQL_DOXYGEN
    friend struct detail::execution_state_access;
#endif
};

}  // namespace mysql
}  // namespace boost

#include <boost/mysql/impl/execution_state.hpp>

#endif
