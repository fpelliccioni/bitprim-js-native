{
  "targets": [
    {
      # "target_name": "bitprim",
      "target_name": "<(module_name)",

      'product_dir': '<(module_path)',

      "sources": [ "src/bitprim_addon.cpp", 
                   "src/executor.cpp", 
                   "src/chain/chain.cpp", 
                   "src/chain/header.cpp", 
                   "src/chain/block.cpp", 
                   "src/chain/merkle_block.cpp", 
                   "src/chain/point.cpp", 
                   "src/chain/transaction.cpp", 
                   "src/chain/input.cpp", 
                   "src/chain/output.cpp", 
                   "src/chain/output_point.cpp", 
                   "src/chain/tools.cpp",
                   "src/chain/script.cpp", 
                   "src/chain/input_list.cpp", 
                   "src/chain/output_list.cpp", 
                   "src/chain/transaction_list.cpp",
                   "src/chain/block_list.cpp",
                   "src/chain/history_compact_list.cpp",
                   "src/chain/history_compact.cpp",
                   "src/chain/stealth_compact.cpp",
                   "src/chain/stealth_compact_list.cpp",
                   "src/wallet/payment_address.cpp",
                   "src/wallet/word_list.cpp",
                ],
      
      'variables': {
        'setup_py': '<(DEPTH)/setup.py',
        'install_py': '<(DEPTH)/install.py',
      },

      # 'actions': [
      #   {
      #       'action_name': 'build_ftgl',
      #       'message': 'Building FTGL...',
      #       'inputs': ['ftgl/src/FTGL/ftgl.h'],
      #       'outputs': ['ftgl/src/.libs/libftgl.a'],
      #       'action': [''eval', 'cd ftgl && ./configure --with-pic && make -C src''],
      #   },
      # ],

      # 'actions': [
      #   {
      #     'variables': {
      #       'core_library_files': [
      #         'src/runtime.js',
      #         'src/v8natives.js',
      #         'src/macros.py',
      #       ],
      #     },
      #     'action_name': 'js2c',
      #     'inputs': [
      #       'tools/js2c.py',
      #       '<@(core_library_files)',
      #     ],
      #     'outputs': [
      #       '<(INTERMEDIATE_DIR)/libraries.cc',
      #       '<(INTERMEDIATE_DIR)/libraries-empty.cc',
      #     ],
      #     'action': ['python', 'tools/js2c.py', '<@(_outputs)', 'CORE', '<@(core_library_files)'],
      #   },
      # ],


      'actions': [
        # {
        #     'action_name': 'installconan',
        #     'message': 'Install Conan',
        #     'inputs': [''],
        #     'outputs': [''],
        #     'action': ['python', '-m pip install conan'],
        #     # 'action': ['python', '--version'],
        # },
        # {
        #     'action_name': 'runconan',
        #     'message': 'run Conan',
        #     'inputs': [''],
        #     'outputs': [''],
        #     'action': ['python', '-m conans.conan', 'install ..'],
        # },
        # {
        #     'action_name': 'movedir',
        #     'message': 'Move Dirs',
        #     'inputs': [''],
        #     'outputs': [''],
        #     # 'action': ['python', '../setup.py'],
        #     'action': ['python', '-c "\\texec(\\"import os \\nprint(os.getcwd()) \\")"'],
        # },

        {
          'action_name': 'Install',
          'inputs': [
            '>(install_py)',
          ],
          # 'outputs': ['>(nmf_pnacl)'],
          'outputs': [''],
          'action': [
            'python',
            '>@(_inputs)', 
          ],
        },
        {
          'action_name': 'Setup',
          'inputs': [
            '>(setup_py)',
          ],
          # 'outputs': ['>(nmf_pnacl)'],
          'outputs': [''],
          'action': [
            'python',
            '>@(_inputs)', 
          ],
        },
      ],


      'defines': [
          'BITPRIM_LIB_STATIC',
          'BITPRIM_DB_NEW_FULL',
      ],
      # # Linux OLD
      # "include_dirs": ["/home/fernando/dev/bitprim/bitprim-node-cint/include"],
      # "libraries": [ "-lbitprim-node-cint", "-L/home/fernando/dev/bitprim/bitprim-node-cint/cmake-build-debug" ]

      # # Windows OLD
      # "include_dirs": ["C:\\development\\bitprim\\bitprim-node-cint\\include", "C:\\development\\bitprim\\bitprim-core\\include"],
      # "libraries": [ "C:\\development\\bitprim\\bitprim-node-cint\\build\\bitprim-node-cint.lib"]
      # # "libraries": [ "-LC:\\development\\bitprim\\bitprim-node-cint\\build", "-lbitprim-node-cint"  ]

      

      'configurations': {
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '3' # /MDd
            },
          },
        },
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'RuntimeLibrary': '2' # /MD
            },
          },
        },
      },

      'conditions': [
        ['OS=="linux"', {


            "cflags": [
            "-Wall",
            "-Wno-implicit-fallthrough",
            "-Wno-uninitialized",
            "-Wno-unused-function",
            "-Wno-unknown-warning-option",
            "-Wno-maybe-uninitialized",
            "-Wno-cast-function-type",
            "-Wno-unused-result",
            "-Wno-nonnull-compare",
            "-Wextra",
            "-O3"
            ],
            "cflags_c": [
            "-std=c99",
            "-Wno-unused-parameter"
            ],
            "cflags_cc+": [
            "-std=c++11",
            "-Wno-maybe-uninitialized",
            "-Wno-cast-function-type",
            "-Wno-unused-parameter",
            "-Wno-unknown-warning-option",
            "-Wno-unused-const-variable",
            "-Wno-undefined-internal"
            ],



          "include_dirs": ["<!(node -e \"require('nan')\")", "./include", "./deps/include", "../deps/include"],
          # "include_dirs": ["/home/fernando/dev/bitprim-node-cint/include"],
          
          'libraries': [
            '-L./deps/lib/', 
            '-L../deps/lib/',
            # '-L/home/fernando/dev/bitprim-node-cint/build/lib', 

            '-lbitprim-node-cint', 
            '-lbitprim-node', 
            '-lbitprim-blockchain', 
            '-lbitprim-network', 
            '-lbitprim-consensus', 
            '-lbitprim-database', 
            '-lbitprim-core',
            '-lboost_atomic', 
            '-lboost_chrono', 
            '-lboost_date_time', 
            '-lboost_filesystem', 
            '-lboost_iostreams', 
            '-lboost_locale', 
            '-lboost_log', 
            '-lboost_log_setup', 
            '-lboost_program_options', 
            '-lboost_random', 
            '-lboost_regex', 
            '-lboost_system', 
            '-lboost_unit_test_framework', 
            '-lboost_prg_exec_monitor', 
            '-lboost_test_exec_monitor', 
            '-lboost_thread', 
            '-lboost_timer', 
            '-lsecp256k1', 
            # '-lbz2', 
            '-lgmp', 
            # '-lz',
          ],
        }],
        ['OS=="mac"', {

          "cflags": [
            "-std=c++11",
          ],
          "include_dirs": ["<!(node -e \"require('nan')\")", "./include", "./deps/include", "../deps/include"],
          # "include_dirs": ["/home/fernando/dev/bitprim-node-cint/include"],
          
          'libraries': [
            '-L./deps/lib/', 
            '-L../deps/lib/',
            # '-L/home/fernando/dev/bitprim-node-cint/build/lib', 

            '-lbitprim-node-cint', 
            '-lbitprim-node', 
            '-lbitprim-blockchain', 
            '-lbitprim-network', 
            '-lbitprim-consensus', 
            '-lbitprim-database', 
            '-lbitprim-core',
            '-lboost_atomic', 
            '-lboost_chrono', 
            '-lboost_date_time', 
            '-lboost_filesystem', 
            '-lboost_iostreams', 
            '-lboost_locale', 
            '-lboost_log', 
            '-lboost_log_setup', 
            '-lboost_program_options', 
            '-lboost_random', 
            '-lboost_regex', 
            '-lboost_system', 
            '-lboost_unit_test_framework', 
            '-lboost_prg_exec_monitor', 
            '-lboost_test_exec_monitor', 
            '-lboost_thread', 
            '-lboost_timer', 
            '-lsecp256k1', 
            '-lbz2', 
            '-lgmp', 
            '-lz',
          ],

        }],
        # ['OS=="linux"', {
        #   'cflags': [
        #     '<!@(pkg-config --cflags QtCore QtGui QtTest)'
        #   ],
        #   'ldflags': [
        #     '<!@(pkg-config --libs-only-L --libs-only-other QtCore QtGui QtTest)'
        #   ],
        #   'libraries': [
        #     '<!@(pkg-config --libs-only-l QtCore QtGui QtTest)'
        #   ]
        # }],
        ['OS=="win"', {
          "include_dirs": ["<!(node -e \"require('nan')\")", "./include", "deps/include"],
          'libraries': [
            '../deps/lib/bitprim-node-cint.lib', 
            '../deps/lib/bitprim-node.lib', 
            '../deps/lib/bitprim-blockchain.lib', 
            '../deps/lib/bitprim-network.lib', 
            '../deps/lib/bitprim-consensus.lib', 
            '../deps/lib/bitprim-database.lib', 
            '../deps/lib/bitprim-core.lib',
            '../deps/lib/libboost_atomic.lib', 
            '../deps/lib/libboost_chrono.lib', 
            '../deps/lib/libboost_date_time.lib', 
            '../deps/lib/libboost_filesystem.lib', 
            '../deps/lib/libboost_iostreams.lib', 
            '../deps/lib/libboost_locale.lib', 
            '../deps/lib/libboost_log.lib', 
            '../deps/lib/libboost_log_setup.lib', 
            '../deps/lib/libboost_program_options.lib', 
            '../deps/lib/libboost_random.lib', 
            '../deps/lib/libboost_regex.lib', 
            '../deps/lib/libboost_system.lib', 
            '../deps/lib/libboost_unit_test_framework.lib', 
            '../deps/lib/libboost_prg_exec_monitor.lib', 
            '../deps/lib/libboost_test_exec_monitor.lib', 
            '../deps/lib/libboost_thread.lib', 
            '../deps/lib/libboost_timer.lib', 
            '../deps/lib/secp256k1.lib', 
            '../deps/lib/mpir.lib', 
            # '../deps/lib/libbz2', 
            # '../deps/lib/libgmp', 
            # '../deps/lib/libz',
          ]
        }]
      ],

    }
  ]
}
