{
  'conditions': [
    ['OS=="win"', {
      'variables': {
        'with_jpeg%': '<!(node ./util/has_lib.js jpeg)',
        'with_gif%': '<!(node ./util/has_lib.js gif)',
        'with_rsvg%': '<!(node ./util/has_lib.js rsvg)'
      }
    }, { # 'OS!="win"'
      'variables': {
        'with_jpeg%': '<!(node ./util/has_lib.js jpeg)',
        'with_gif%': '<!(node ./util/has_lib.js gif)',
        'with_rsvg%': '<!(node ./util/has_lib.js rsvg)'
      }
    }]
  ],
  'targets': [
    {
      'target_name': 'canvas-postbuild',
      'dependencies': ['canvas'],
      'conditions': [
        ['OS=="win"', {
          'copies': [] # Remove copies section, as we don't need to copy DLLs
        }]
      ]
    },
    {
      'target_name': 'canvas',
      'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS', 'NODE_ADDON_API_ENABLE_MAYBE' ],
      'sources': [
        'src/backend/Backend.cc',
        'src/backend/ImageBackend.cc',
        'src/backend/PdfBackend.cc',
        'src/backend/SvgBackend.cc',
        'src/bmp/BMPParser.cc',
        'src/Backends.cc',
        'src/Canvas.cc',
        'src/CanvasGradient.cc',
        'src/CanvasPattern.cc',
        'src/CanvasRenderingContext2d.cc',
        'src/closure.cc',
        'src/color.cc',
        'src/Image.cc',
        'src/ImageData.cc',
        'src/init.cc',
        'src/register_font.cc',
        'src/FontParser.cc'
      ],
      'conditions': [
        ['OS=="win"', {
          'libraries': [
            '<!@(pkg-config cairo --libs)',
            '<!@(pkg-config libpng16 --libs)',
            '<!@(pkg-config pangocairo --libs)',
            '<!@(pkg-config pango --libs)',
            '<!@(pkg-config freetype2 --libs)',
            '<!@(pkg-config glib-2.0 --libs)',
            '<!@(pkg-config gobject-2.0 --libs)'
          ],
          'include_dirs': [
            '<!@(pkg-config cairo --cflags)',
            '<!@(pkg-config libpng16 --cflags)',
            '<!@(pkg-config pango --cflags)',
            '<!@(pkg-config pangocairo --cflags)',
            '<!@(pkg-config freetype2 --cflags)',
            '<!@(pkg-config glib-2.0 --cflags)'
          ],
          'defines': [
            '_USE_MATH_DEFINES',
            'NOMINMAX'
          ],
          'configurations': {
            'Debug': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'WarningLevel': 4,
                  'ExceptionHandling': 1,
                  'DisableSpecificWarnings': [
                    4100, 4611
                  ]
                }
              }
            },
            'Release': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'WarningLevel': 4,
                  'ExceptionHandling': 1,
                  'DisableSpecificWarnings': [
                    4100, 4611
                  ]
                }
              }
            }
          }
        }, { # 'OS!="win"'
          'libraries': [
            '<!@(pkg-config pixman-1 --libs)',
            '<!@(pkg-config cairo --libs)',
            '<!@(pkg-config libpng --libs)',
            '<!@(pkg-config pangocairo --libs)',
            '<!@(pkg-config freetype2 --libs)'
          ],
          'include_dirs': [
            '<!@(pkg-config cairo --cflags)',
            '<!@(pkg-config libpng --cflags)',
            '<!@(pkg-config pangocairo --cflags)',
            '<!@(pkg-config freetype2 --cflags)'
          ],
          'cflags': ['-Wno-cast-function-type'],
          'cflags!': ['-fno-exceptions'],
          'cflags_cc!': ['-fno-exceptions']
        }],
        ['OS=="mac"', {
          'cflags+': ['-fvisibility=hidden'],
          'xcode_settings': {
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }],
        ['with_jpeg=="true"', {
          'defines': [
            'HAVE_JPEG'
          ],
          'conditions': [
            ['OS=="win"', {
              'copies': [], # Remove copies section
              'include_dirs': [
                '<!@(pkg-config libjpeg --cflags)'
              ],
              'libraries': [
                '<!@(pkg-config libjpeg --libs)'
              ]
            }, {
              'include_dirs': [
                '<!@(pkg-config libjpeg --cflags)'
              ],
              'libraries': [
                '<!@(pkg-config libjpeg --libs)'
              ]
            }]
          ]
        }],
        ['with_gif=="true"', {
          'defines': [
            'HAVE_GIF'
          ],
          'conditions': [
            ['OS=="win"', {
              'libraries': [
                '<!@(pkg-config giflib --libs)'
              ]
            }, {
              'libraries': [
                '<!@(pkg-config giflib --libs)'
              ]
            }]
          ]
        }],
        ['with_rsvg=="true"', {
          'defines': [
            'HAVE_RSVG'
          ],
          'conditions': [
            ['OS=="win"', {
              'copies': [], # Remove copies section
              'include_dirs': [
                '<!@(pkg-config librsvg-2.0 --cflags)'
              ],
              'libraries': [
                '<!@(pkg-config librsvg-2.0 --libs)'
              ]
            }, {
              'include_dirs': [
                '<!@(pkg-config librsvg-2.0 --cflags)'
              ],
              'libraries': [
                '<!@(pkg-config librsvg-2.0 --libs)'
              ]
            }]
          ]
        }]
      ]
    }
  ]
}{
  'conditions': [
    ['OS=="win"', {
      'variables': {
        'with_jpeg%': '<!(node ./util/has_lib.js jpeg)',
        'with_gif%': '<!(node ./util/has_lib.js gif)',
        'with_rsvg%': '<!(node ./util/has_lib.js rsvg)'
      }
    }, { # 'OS!="win"'
      'variables': {
        'with_jpeg%': '<!(node ./util/has_lib.js jpeg)',
        'with_gif%': '<!(node ./util/has_lib.js gif)',
        'with_rsvg%': '<!(node ./util/has_lib.js rsvg)'
      }
    }]
  ],
  'targets': [
    {
      'target_name': 'canvas-postbuild',
      'dependencies': ['canvas'],
      'conditions': [
        ['OS=="win"', {
          'copies': [] # Remove copies section, as we don't need to copy DLLs
        }]
      ]
    },
    {
      'target_name': 'canvas',
      'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS', 'NODE_ADDON_API_ENABLE_MAYBE' ],
      'sources': [
        'src/backend/Backend.cc',
        'src/backend/ImageBackend.cc',
        'src/backend/PdfBackend.cc',
        'src/backend/SvgBackend.cc',
        'src/bmp/BMPParser.cc',
        'src/Backends.cc',
        'src/Canvas.cc',
        'src/CanvasGradient.cc',
        'src/CanvasPattern.cc',
        'src/CanvasRenderingContext2d.cc',
        'src/closure.cc',
        'src/color.cc',
        'src/Image.cc',
        'src/ImageData.cc',
        'src/init.cc',
        'src/register_font.cc',
        'src/FontParser.cc'
      ],
      'conditions': [
        ['OS=="win"', {
          'libraries': [
            '<!@(pkg-config cairo --libs)',
            '<!@(pkg-config libpng16 --libs)',
            '<!@(pkg-config pangocairo --libs)',
            '<!@(pkg-config pango --libs)',
            '<!@(pkg-config freetype2 --libs)',
            '<!@(pkg-config glib-2.0 --libs)',
            '<!@(pkg-config gobject-2.0 --libs)'
          ],
          'include_dirs': [
            '<!@(pkg-config cairo --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config libpng16 --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config pango --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config pangocairo --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config freetype2 --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config glib-2.0 --cflags-only-I | sed s/-I//g)'
          ],
          'defines': [
            '_USE_MATH_DEFINES',
            'NOMINMAX'
          ],
          'configurations': {
            'Debug': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'WarningLevel': 4,
                  'ExceptionHandling': 1,
                  'DisableSpecificWarnings': [
                    4100, 4611
                  ]
                }
              }
            },
            'Release': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'WarningLevel': 4,
                  'ExceptionHandling': 1,
                  'DisableSpecificWarnings': [
                    4100, 4611
                  ]
                }
              }
            }
          }
        }, { # 'OS!="win"'
          'libraries': [
            '<!@(pkg-config pixman-1 --libs)',
            '<!@(pkg-config cairo --libs)',
            '<!@(pkg-config libpng --libs)',
            '<!@(pkg-config pangocairo --libs)',
            '<!@(pkg-config freetype2 --libs)'
          ],
          'include_dirs': [
            '<!@(pkg-config cairo --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config libpng --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config pangocairo --cflags-only-I | sed s/-I//g)',
            '<!@(pkg-config freetype2 --cflags-only-I | sed s/-I//g)'
          ],
          'cflags': ['-Wno-cast-function-type'],
          'cflags!': ['-fno-exceptions'],
          'cflags_cc!': ['-fno-exceptions']
        }],
        ['OS=="mac"', {
          'cflags+': ['-fvisibility=hidden'],
          'xcode_settings': {
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }],
        ['with_jpeg=="true"', {
          'defines': [
            'HAVE_JPEG'
          ],
          'conditions': [
            ['OS=="win"', {
              'copies': [], # Remove copies section
              'include_dirs': [
                '<!@(pkg-config libjpeg --cflags-only-I | sed s/-I//g)'
              ],
              'libraries': [
                '<!@(pkg-config libjpeg --libs)'
              ]
            }, {
              'include_dirs': [
                '<!@(pkg-config libjpeg --cflags-only-I | sed s/-I//g)'
              ],
              'libraries': [
                '<!@(pkg-config libjpeg --libs)'
              ]
            }]
          ]
        }],
        ['with_gif=="true"', {
          'defines': [
            'HAVE_GIF'
          ],
          'conditions': [
            ['OS=="win"', {
              'libraries': [
                '<!@(pkg-config giflib --libs)'
              ]
            }, {
              'libraries': [
                '<!@(pkg-config giflib --libs)'
              ]
            }]
          ]
        }],
        ['with_rsvg=="true"', {
          'defines': [
            'HAVE_RSVG'
          ],
          'conditions': [
            ['OS=="win"', {
              'copies': [], # Remove copies section
              'include_dirs': [
                '<!@(pkg-config librsvg-2.0 --cflags-only-I | sed s/-I//g)'
              ],
              'libraries': [
                '<!@(pkg-config librsvg-2.0 --libs)'
              ]
            }, {
              'include_dirs': [
                '<!@(pkg-config librsvg-2.0 --cflags-only-I | sed s/-I//g)'
              ],
              'libraries': [
                '<!@(pkg-config librsvg-2.0 --libs)'
              ]
            }]
          ]
        }]
      ]
    }
  ]
}
