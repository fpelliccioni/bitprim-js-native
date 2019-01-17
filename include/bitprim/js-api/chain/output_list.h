#ifndef BITPRIM_JS_CHAIN_OUTPUT_LIST_H_
#define BITPRIM_JS_CHAIN_OUTPUT_LIST_H_

#include <node.h>
#include <nan.h>

namespace bitprim_ns {

void bitprim_chain_output_list_push_back(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_output_list_count(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_output_list_nth(v8::FunctionCallbackInfo<v8::Value> const& args);

}  // namespace bitprim_ns

#endif //BITPRIM_JS_CHAIN_OUTPUT_LIST_H_
