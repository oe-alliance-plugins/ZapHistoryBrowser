from setuptools import setup
import setup_translate

pkg = 'Extensions.ZapHistoryBrowser'
setup(name='enigma2-plugin-extensions-zaphistorybrowser',
       version='3.0',
       description='Shows a list containing the zapping-history and allows user to zap to the entries or to modify them',
       package_dir={pkg: 'ZapHistoryBrowser'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', '*.info', '*.txt']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
