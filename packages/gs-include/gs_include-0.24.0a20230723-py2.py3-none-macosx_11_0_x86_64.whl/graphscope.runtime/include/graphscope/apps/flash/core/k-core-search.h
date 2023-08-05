/** Copyright 2020 Alibaba Group Holding Limited.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

#ifndef ANALYTICAL_ENGINE_APPS_FLASH_CORE_K_CORE_SEARCH_H_
#define ANALYTICAL_ENGINE_APPS_FLASH_CORE_K_CORE_SEARCH_H_

#include <memory>

#include "grape/grape.h"

#include "apps/flash/api.h"
#include "apps/flash/flash_app_base.h"
#include "apps/flash/flash_context.h"
#include "apps/flash/flash_worker.h"
#include "apps/flash/value_type.h"

namespace gs {

template <typename FRAG_T>
class KCoreSearchFlash : public FlashAppBase<FRAG_T, K_CORE_TYPE> {
 public:
  INSTALL_FLASH_WORKER(KCoreSearchFlash<FRAG_T>, K_CORE_TYPE, FRAG_T)
  using context_t = FlashGlobalDataContext<FRAG_T, K_CORE_TYPE, int>;

  bool sync_all_ = false;
  int s;

  int GlobalRes() { return s; }

  void Run(const fragment_t& graph, const std::shared_ptr<fw_t> fw, int k) {
    int n_vertex = graph.GetTotalVerticesNum();
    LOG(INFO) << "Run K-core search with Flash, total vertices: " << n_vertex
              << ", k: " << k << std::endl;

    DefineMapV(init) { v.d = Deg(id); };
    vset_t A = VertexMap(All, CTrueV, init);

    DefineFV(filter) { return v.d < k; };

    DefineFV(check) { return v.d >= k; };
    DefineMapE(update) { d.d--; };

    for (int len = VSize(A), i = 0; len > 0; len = VSize(A), ++i) {
      LOG(INFO) << "Round " << i << ": size=" << len << std::endl;
      A = VertexMap(A, filter);
      A = EdgeMapDense(A, EU, CTrueE, update, check);
    }

    A = VertexMap(All, check);
    s = VSize(A);
    LOG(INFO) << "k-core size=" << s << std::endl;
  }
};

}  // namespace gs

#endif  // ANALYTICAL_ENGINE_APPS_FLASH_CORE_K_CORE_SEARCH_H_
