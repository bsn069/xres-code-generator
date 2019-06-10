## -*- coding: utf-8 -*-
<%!
import time
%>
//
// generated by xrescode on ${time.strftime("%Y-%m-%d %H:%M:%S")}, please don't edit it
//

#ifndef CONFIG_EXCEL_CONFIG_SET_${pb_msg.get_cpp_if_guard_name()}_H
#define CONFIG_EXCEL_CONFIG_SET_${pb_msg.get_cpp_if_guard_name()}_H

#pragma once

#include <stdint.h>
#include <cstddef>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>

#include <std/smart_ptr.h>

#include <lock/spin_rw_lock.h>

#include <config/compiler_features.h>
#include <design_pattern/singleton.h>
#include <log/log_wrapper.h>

#include <${pb_set.pb_include_prefix}${pb_msg.get_pb_header_path()}>

namespace excel {
${pb_msg.get_cpp_namespace_decl_begin()}

    class ${pb_msg.get_cpp_class_name()} {
    public:
        typedef ${pb_msg.get_pb_inner_class_name()} item_type;
        typedef ${pb_msg.get_pb_inner_class_name()} proto_type;
        typedef std::shared_ptr<item_type> item_ptr_type;

    public:
        ${pb_msg.get_cpp_class_name()}();
        ~${pb_msg.get_cpp_class_name()}();

        int on_inited();

        int load_all();

        void clear();

    private:
        int load_file(const std::string& file_path);
        int load_list(const char*);
        int reload_file_lists();
        void merge_data(item_ptr_type);

    private:
        ::util::lock::spin_rw_lock            load_file_lock_;
        std::unordered_map<std::string, bool> file_status_; // true: already loaded

% for code_index in pb_msg.code.indexes:
        // ------------------------- index: ${code_index.name} -------------------------
    public:
% if code_index.is_list():
        typedef std::vector<item_ptr_type> ${code_index.name}_value_type;
        const ${code_index.name}_value_type* get_list_by_${code_index.name}(${code_index.get_key_decl()});
        item_ptr_type get_by_${code_index.name}(${code_index.get_key_decl()}, size_t index);
    private:
        const ${code_index.name}_value_type* _get_list_by_${code_index.name}(${code_index.get_key_decl()});
% else:
        typedef item_ptr_type ${code_index.name}_value_type;
        ${code_index.name}_value_type get_by_${code_index.name}(${code_index.get_key_decl()});
% endif

    private:
% if code_index.is_vector():
        typedef std::vector<${code_index.name}_value_type> ${code_index.name}_container_type;
        ${code_index.name}_container_type ${code_index.name}_data_;
% else:
        typedef std::map<std::tuple<${code_index.get_key_type_list()}>, ${code_index.name}_value_type> ${code_index.name}_container_type;
        ${code_index.name}_container_type ${code_index.name}_data_;
% endif

% endfor
    };

${pb_msg.get_cpp_namespace_decl_end()}
}

#endif // CONFIG_EXCEL_CONFIG_SET_${pb_msg.get_cpp_if_guard_name()}_H
