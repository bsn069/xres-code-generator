
//
// generated by xrescode on 2019-06-10 18:48:31, please don't edit it
//

#include <algorithm>
#include <cstddef>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <tuple>
#include <vector>

// 禁用掉unordered_map，我们要保证mt_core中逻辑有序
#if 0 && defined(__cplusplus) && __cplusplus >= 201103L
#include <unordered_map>
#define LIBXRESLOADER_USING_HASH_MAP 1
#else

#endif

#ifdef _MSC_VER
#include <Windows.h>
#endif

#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/message_lite.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/stubs/common.h>


#include <log/log_wrapper.h>
#include <lock/lock_holder.h>
#include <common/string_oprs.h>

#include "config_manager.h"
#include "config_set_FaTerrainInfo.h"

namespace excel {
namespace FaGame {

    config_set_FaTerrainInfo::config_set_FaTerrainInfo() {
    }

    config_set_FaTerrainInfo::~config_set_FaTerrainInfo(){
    }

    int config_set_FaTerrainInfo::on_inited() {
        ::util::lock::write_lock_holder wlh(load_file_lock_);
        
        file_status_.clear();
        return reload_file_lists();
    }

    int config_set_FaTerrainInfo::load_all() {
        int ret = 0;
        ::util::lock::write_lock_holder wlh(load_file_lock_);
        for (std::unordered_map<std::string, bool>::iterator iter = file_status_.begin(); iter != file_status_.end(); ++ iter) {
            if (!iter->second) {
                int res = load_file(iter->first);
                if (res < 0) {
                    WLOGERROR("load config file %s for %s failed", iter->first.c_str(), "config_set_FaTerrainInfo");
                    ret = res;
                } else if (ret >= 0) {
                    ret += res;
                }
            }
        }

        return ret;
    }

    void config_set_FaTerrainInfo::clear() {
        ::util::lock::write_lock_holder wlh(load_file_lock_);
        id_data_.clear();
        file_status_.clear();
        reload_file_lists();
    }

    int config_set_FaTerrainInfo::load_file(const std::string& file_path) {
        std::unordered_map<std::string, bool>::iterator iter = file_status_.find(file_path);
        if (iter == file_status_.end()) {
            WLOGERROR("load config file %s for %s failed, not exist in any file_list/file_path", file_path.c_str(), "config_set_FaTerrainInfo");
            return -2;
        }

        if (iter->second) {
            return 0;
        }
        iter->second = true;

        std::string content;
        if (!config_manager::me()->load_file_data(content, file_path)) {
            WLOGERROR("load file %s for %s failed", file_path.c_str(), "config_set_FaTerrainInfo");
            return -3;
        }

        ::FaGame::FaTerrainInfo_Tbl outer_data;
        if (!outer_data.ParseFromString(content)) {
            WLOGERROR("parse file %s for %s(message type: %s) failed, msg: %s",
                file_path.c_str(), "config_set_FaTerrainInfo", "::FaGame::FaTerrainInfo_Tbl",
                outer_data.InitializationErrorString().c_str()
            );
            return -4;
        }


        for (int i = 0; i < outer_data.items_size(); ++ i) {
            merge_data(std::make_shared<item_type>(outer_data.items(i)));
        }

        return 1;
    }

    int config_set_FaTerrainInfo::load_list(const char* file_list_path) {
        std::string content;
        if (!config_manager::me()->load_file_data(content, file_list_path)) {
            WLOGERROR("load file %s for %s failed", file_list_path, "config_set_FaTerrainInfo");
            return -1;
        }

        const char* line_start = content.c_str();
        const char* line_end;
        int ret = 0;
        for (; line_start < content.c_str() + content.size() && *line_start; line_start = line_end + 1) {
            line_end = line_start;

            while (*line_end && '\r' != *line_end && '\n' != *line_end) {
                ++ line_end;
            }

            std::pair<const char*, size_t> file_path_trimed = ::util::string::trim(line_start, line_end - line_start);
            if (file_path_trimed.second == 0) {
                continue;
            }

            std::string file_path;
            file_path.assign(file_path_trimed.first, file_path_trimed.second);
            if (file_status_.end() == file_status_.find(file_path)) {
                file_status_[file_path] = false;
            }
        }

        return ret;
    }

    int config_set_FaTerrainInfo::reload_file_lists() {
        file_status_["Terrains/TerrainInfo_0.bytes"] = false;
        return 0;
    }

    void config_set_FaTerrainInfo::merge_data(item_ptr_type item) {
        if (!item) {
            WLOGERROR("merge_data(nullptr) is not allowed for %s", "config_set_FaTerrainInfo");
            return;
        }

        // index: id
        do {
            std::tuple<int32_t> key = std::make_tuple(item->id());
            if (id_data_.end() != id_data_.find(key)) {
                WLOGERROR("merge_data() with key=<%d> for %s is already exists, we will cover it with the newer value", 
                    static_cast<int>(item->id()), "config_set_FaTerrainInfo");
            }
            id_data_[key] = item;
        } while(false);

    }

    config_set_FaTerrainInfo::id_value_type config_set_FaTerrainInfo::get_by_id(int32_t Id) {
        ::util::lock::read_lock_holder rlh(load_file_lock_);
        id_container_type::iterator iter = id_data_.find(std::make_tuple(Id));
        if (iter != id_data_.end()) {
            return iter->second;
        }

        std::string file_path = "Terrains/TerrainInfo_0.bytes";

        int res = load_file(file_path);
        if (res < 0) {
            WLOGERROR("load file %s for %s failed, res: %d", file_path.c_str(), "config_set_FaTerrainInfo", res);
            return nullptr;
        }

        iter = id_data_.find(std::make_tuple(Id));
        if (iter == id_data_.end()) {
            WLOGERROR("load index %s with key=<%d> for %s failed, not found",
                "id", static_cast<int>(Id), "config_set_FaTerrainInfo"
            );
            return nullptr;
        }

        return iter->second;
    }

} /*FaGame*/
}