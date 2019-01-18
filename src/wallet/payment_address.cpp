#include <string.h>
#include <stdlib.h>

#include <node.h>
#include <nan.h>

#include <bitprim/nodecint/wallet/payment_address.h>

#include <bitprim/js-api/wallet/payment_address.h>

namespace bitprim_ns {

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Handle;
using v8::Global;

using v8::Object;
using v8::String;
using v8::Boolean;
using v8::Value;
using v8::External;
using v8::Exception;
using v8::Number;
using v8::Persistent;
using v8::Function;
using v8::Uint8Array;
using v8::ArrayBuffer;


void bitprim_wallet_payment_address_construct_from_string(v8::FunctionCallbackInfo<v8::Value> const& args) {
    Isolate* isolate = args.GetIsolate();
    
    if (args.Length() != 1) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong number of arguments")));
        return;
    }

    if ( ! args[0]->IsString()) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong arguments")));
        return;
    }

    v8::String::Utf8Value str(isolate, args[0]->ToString(Nan::GetCurrentContext()).FromMaybe(v8::Local<v8::String>()));

    payment_address_t res = wallet_payment_address_construct_from_string(*str);
    args.GetReturnValue().Set(External::New(isolate, res));
}

void bitprim_wallet_payment_address_destruct(v8::FunctionCallbackInfo<v8::Value> const& args) {
    Isolate* isolate = args.GetIsolate();

    if (args.Length() != 1) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong number of arguments")));
        return;
    }

    if ( ! args[0]->IsExternal()) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong arguments")));
        return;
    }

    void* vptr = v8::External::Cast(*args[0])->Value();
    payment_address_t payment_address = (payment_address_t)vptr;

    wallet_payment_address_destruct(payment_address);
}

void bitprim_wallet_payment_address_encoded(v8::FunctionCallbackInfo<v8::Value> const& args) {
    Isolate* isolate = args.GetIsolate();

    if (args.Length() != 1) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong number of arguments")));
        return;
    }

    if ( ! args[0]->IsExternal()) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong arguments")));
        return;
    }

    void* vptr = v8::External::Cast(*args[0])->Value();
    payment_address_t payment_address = (payment_address_t)vptr;

    char const* res = wallet_payment_address_encoded(payment_address);
    args.GetReturnValue().Set(String::NewFromUtf8(isolate, res));
}

void bitprim_wallet_payment_address_version(v8::FunctionCallbackInfo<v8::Value> const& args) {
    Isolate* isolate = args.GetIsolate();

    if (args.Length() != 1) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong number of arguments")));
        return;
    }

    if ( ! args[0]->IsExternal()) {
        isolate->ThrowException(Exception::TypeError(String::NewFromUtf8(isolate, "Wrong arguments")));
        return;
    }

    void* vptr = v8::External::Cast(*args[0])->Value();
    payment_address_t payment_address = (payment_address_t)vptr;

    uint8_t res = wallet_payment_address_version(payment_address);
    args.GetReturnValue().Set(Number::New(isolate, res));
}

}  // namespace bitprim_ns