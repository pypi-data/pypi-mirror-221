// Copyright (c) 2006, 2007 Julio M. Merino Vidal
// Copyright (c) 2008 Ilya Sokolov, Boris Schaeling
// Copyright (c) 2009 Boris Schaeling
// Copyright (c) 2010 Felipe Tanus, Boris Schaeling
// Copyright (c) 2011, 2012 Jeff Flinn, Boris Schaeling
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

#ifndef BOOST_PROCESS_POSIX_SEARCH_PATH_HPP
#define BOOST_PROCESS_POSIX_SEARCH_PATH_HPP

#include <boost/process/detail/config.hpp>
#include <boost/process/filesystem.hpp>
#include <boost/tokenizer.hpp>
#include <string>
#include <stdexcept>
#include <stdlib.h>
#include <unistd.h>

namespace boost { namespace process { namespace detail { namespace posix {

inline boost::process::filesystem::path search_path(
        const boost::process::filesystem::path &filename,
        const std::vector<boost::process::filesystem::path> &path)
{
    for (const boost::process::filesystem::path & pp : path)
    {
        auto p = pp / filename;
#if defined(BOOST_PROCESS_USE_STD_FS)
        std::error_code ec;
#else
        boost::system::error_code ec;
#endif
        bool file = boost::process::filesystem::is_regular_file(p, ec);
        if (!ec && file && ::access(p.c_str(), X_OK) == 0)
            return p;
    }
    return "";
}

}}}}

#endif
