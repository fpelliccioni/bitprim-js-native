#ifndef BITPRIM_JS_CHAIN_STEALTH_COMPACT_H_
#define BITPRIM_JS_CHAIN_STEALTH_COMPACT_H_

#include <node.h>
#include <nan.h>

namespace bitprim_ns {

void bitprim_chain_stealth_compact_get_ephemeral_public_key_hash(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_stealth_compact_get_transaction_hash(v8::FunctionCallbackInfo<v8::Value> const& args);
void bitprim_chain_stealth_compact_get_public_key_hash(v8::FunctionCallbackInfo<v8::Value> const& args);

}  // namespace bitprim_ns

#endif //BITPRIM_JS_CHAIN_STEALTH_COMPACT_H_
