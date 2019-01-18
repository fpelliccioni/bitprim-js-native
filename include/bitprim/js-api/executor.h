// #include <node.h>
#include <nan.h>

namespace bitprim_ns {

using v8::FunctionCallbackInfo;
using v8::Value;

//void Method(FunctionCallbackInfo<Value> const& args) {
//    Isolate* isolate = args.GetIsolate();
//    args.GetReturnValue().Set(String::NewFromUtf8(isolate, "world"));
//}


void bitprim_executor_construct(FunctionCallbackInfo<Value> const& args);
void bitprim_executor_destruct(FunctionCallbackInfo<Value> const& args);
void bitprim_executor_stop(FunctionCallbackInfo<Value> const& args);
void bitprim_executor_initchain(FunctionCallbackInfo<Value> const& args);
//void bitprim_executor_run(FunctionCallbackInfo<Value> const& args);
void bitprim_executor_run_wait(FunctionCallbackInfo<Value> const& args);
void bitprim_executor_get_chain(FunctionCallbackInfo<Value> const& args);

}  // namespace bitprim_ns
