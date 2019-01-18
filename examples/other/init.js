const bitprim = require('bitprim-native');
// var bitprim = require('bindings')('binding.node')

const executor = bitprim.executor_construct("", process.stdout, process.stderr);
// const executor = bitprim.executor_construct("", null, null)
bitprim.executor_initchain(executor)
bitprim.executor_run_wait(executor)