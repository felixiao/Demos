# -*- coding: utf-8 -*-
# Deployment settings for Demo_4_TileCollision_AdvAudio_UI.
# This file is autogenerated by the mkb system and used by the s3e deployment
# tool during the build process.

config = {}
cmdline = ['C:/Marmalade/6.2/s3e/makefile_builder/mkb.py', 'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/Demo_4_TileCollision_AdvAudio_UI.mkb', '--default-buildenv=vc10', '--msvc-project', '--deploy-only']
mkb = 'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/Demo_4_TileCollision_AdvAudio_UI.mkb'
mkf = ['c:\\marmalade\\6.2\\modules\\iw2d\\iw2d.mkf', 'c:\\marmalade\\6.2\\modules\\iwgx\\iwgx.mkf', 'c:\\marmalade\\6.2\\modules\\iwgeom\\iwgeom.mkf', 'c:\\marmalade\\6.2\\modules\\iwutil\\iwutil.mkf', u'c:\\users\\0900391\\appdata\\roaming\\marmalade\\packages\\6.2.2\\libjpeg_6b\\libjpeg.mkf', u'c:\\users\\0900391\\appdata\\roaming\\marmalade\\packages\\6.2.2\\libpng_1.2.34\\libpng.mkf', u'c:\\users\\0900391\\appdata\\roaming\\marmalade\\packages\\6.2.2\\zlib_1.2.4\\zlib.mkf', 'c:\\marmalade\\6.2\\modules\\iwresmanager\\iwresmanager.mkf', 'c:\\marmalade\\6.2\\modules\\iwgl\\iwgl.mkf', 'c:\\marmalade\\6.2\\modules\\iwgxfont\\iwgxfont.mkf', u'c:\\users\\0900391\\appdata\\roaming\\marmalade\\packages\\6.2.2\\tiniconv_1.0.1\\tiniconv.mkf', 'c:\\users\\0900391\\dropbox\\project impact\\code\\demos\\demo_4_tilecollision_advaudio_ui\\demo_4_tilecollision_advaudio_ui.mkf', 'c:\\users\\0900391\\dropbox\\project impact\\code\\demos\\demo_4_tilecollision_advaudio_ui\\libs\\cjson-for-marmalade\\cjson.mkf', 'c:\\users\\0900391\\dropbox\\project impact\\code\\demos\\demo_4_tilecollision_advaudio_ui\\libs\\soundengine\\soundengine.mkf']

class DeployConfig(object):
    pass

######### ASSET GROUPS #############

assets = {}

assets['Default'] = [
    ('c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI\data', '.', 0),
]

assets['default'] = [
    ('c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data/splashscreen.jpg', 'splashscreen.jpg', 0),
    ('c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data/audios/music_placeholder.mp3', 'audios/music_placeholder.mp3', 0),
    ('c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data-ram/data-gles1/Level_1.group.bin,c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data/Level_1.group.bin', 'Level_1.group.bin', 0),
    ('c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data/audios/music_placeholder.mp3', 'music_placeholder.mp3', 0),
    ('c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data/audios/test_footstep_left_01.wav', 'test_footstep_left_01.wav', 0),
]

assets['artbuild'] = [
    ('c:/users/0900391/dropbox/project impact/code/demos/demo_4_tilecollision_advaudio_ui/data', '.', 0),
]

######### DEFAULT CONFIG #############

class DefaultConfig(DeployConfig):
    embed_icf = -1
    name = 'Demo_4_TileCollision_AdvAudio_UI'
    pub_sign_key = 0
    priv_sign_key = 0
    caption = 'Demo_4_TileCollision_AdvAudio_UI'
    long_caption = 'Demo_4_TileCollision_AdvAudio_UI'
    version = [0, 0, 1]
    config = ['c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/data/app.icf']
    data_dir = 'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/data'
    iphone_link_lib = []
    linux_ext_lib = []
    iphone_link_libdir = []
    iphone_link_opts = []
    osx_ext_dll = []
    android_external_jars = []
    android_external_res = []
    android_supports_gl_texture = []
    android_extra_manifest = []
    iphone_link_libdirs = []
    android_extra_application_manifest = []
    win32_ext_dll = []
    android_so = []
    iphone_link_libs = []
    target = {
         'arm' : {
                   'debug'   : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Debug_Demo_4_TileCollision_AdvAudio_UI_VC10_arm/Demo_4_TileCollision_AdvAudio_UI.s3e',
                   'release' : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Release_Demo_4_TileCollision_AdvAudio_UI_VC10_arm/Demo_4_TileCollision_AdvAudio_UI.s3e',
                 },
         'mips_gcc' : {
                   'debug'   : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Debug_Demo_4_TileCollision_AdvAudio_UI_VC10_gcc_mips/Demo_4_TileCollision_AdvAudio_UI.so',
                   'release' : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Release_Demo_4_TileCollision_AdvAudio_UI_VC10_gcc_mips/Demo_4_TileCollision_AdvAudio_UI.so',
                 },
         'x86' : {
                   'debug'   : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Debug_Demo_4_TileCollision_AdvAudio_UI_VC10_x86/Demo_4_TileCollision_AdvAudio_UI.s86',
                   'release' : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Release_Demo_4_TileCollision_AdvAudio_UI_VC10_x86/Demo_4_TileCollision_AdvAudio_UI.s86',
                 },
         'arm_gcc' : {
                   'debug'   : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Debug_Demo_4_TileCollision_AdvAudio_UI_VC10_gcc_arm/Demo_4_TileCollision_AdvAudio_UI.s3e',
                   'release' : r'c:/Users/0900391/Dropbox/Project Impact/Code/Demos/Demo_4_TileCollision_AdvAudio_UI/build_demo_4_tilecollision_advaudio_ui_vc10/Release_Demo_4_TileCollision_AdvAudio_UI_VC10_gcc_arm/Demo_4_TileCollision_AdvAudio_UI.s3e',
                 },
        }
    assets = assets['Default']

default = DefaultConfig()
