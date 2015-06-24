# Test

{
    'variables': {
    },
    'targets': [
        {
            'target_name': 'electron-jitterbuffer-<@(target_arch)',
            'dependencies': [
                'deps/binding.gyp:libspeexdsp'
            ],
            'cflags': [
                '-pthread',
                '-fno-exceptions',
                '-fno-strict-aliasing',
                '-Wall',
                '-Wno-unused-parameter',
                '-Wno-missing-field-initializers',
                '-Wextra',
                '-pipe',
                '-fno-ident',
                '-fdata-sections',
                '-ffunction-sections',
                '-fPIC'
            ],
            'defines': [
                'LARGEFILE_SOURCE',
                '_FILE_OFFSET_BITS=64',
                'WEBRTC_TARGET_PC',
                'WEBRTC_LINUX',
                'WEBRTC_THREAD_RR',
                'EXPAT_RELATIVE_PATH',
                'GTEST_RELATIVE_PATH',
                'JSONCPP_RELATIVE_PATH',
                'WEBRTC_RELATIVE_PATH',
                'POSIX',
                '__STDC_FORMAT_MACROS',
                'DYNAMIC_ANNOTATIONS_ENABLED=0'
            ],
            'include_dirs': [
                'deps/speex-1.2rc1/include',
                'deps/config/speex-1.2rc1/<(OS)/<(target_arch)',
                "<!(node -e \"require('nan')\")",
                "<!(node -e \"require('electron-updater-tools')\")"
            ],
            'sources': [
                'src/node-jitterbuffer.cc',
            ],
            'link_settings': {
                'ldflags': [
                ],
                'libraries': [
                ]
            },
            'target_conditions': [
                [ 'OS=="win"', {
                    'msvs_settings': {
                        'VCLinkerTool': {
                            'DelayLoadDLLs': [ 'node.dll', 'iojs.exe', 'node.exe' ],
                            # Don't print a linker warning when no imports from either .exe
                            # are used.
                            'AdditionalOptions': [ '/ignore:4199' ],
                        },
                    },
                }],
            ]
        }
    ]
}
