#ifndef BITPRIM_JS_CHAIN_POINT_H_
#define BITPRIM_JS_CHAIN_POINT_H_

#include <node.h>

namespace bitprim_ns {

void bitprim_chain_point_get_hash(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_point_is_valid(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_point_get_index(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_point_get_checksum(v8::FunctionCallbackInfo<v8::Value> const& args);

}  // namespace bitprim_ns

#endif //BITPRIM_JS_CHAIN_POINT_H_
