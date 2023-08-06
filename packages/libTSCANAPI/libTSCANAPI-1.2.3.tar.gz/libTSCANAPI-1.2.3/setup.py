'''
Author: seven 865762826@qq.com
Date: 2023-03-24 09:26:29
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-27 13:33:40
FilePath: \VSCode_Pro\Python_Pro\TSMasterApi\setup.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r",encoding="utf-8") as f:
  long_description = f.read()

# 
setup(name='libTSCANAPI',  # 包名
      version='1.2.3',  # 版本号
      description='Use TSMaster hardware',
      long_description=long_description,
      author='seven',
      author_email='865762826@qq.com',
      install_requires=['python-can', 'cantools'],
      license='BSD License',
      # packages=['DataBases','Demo','Demo/icon','libTSCANAPI','libTSCANAPI/windows/x64','libTSCANAPI/windows/x86','libTSCANAPI/linux'],
      packages=['libTSCANAPI','libTSCANAPI/windows/x64','libTSCANAPI/windows/x86','libTSCANAPI/linux'],
      package_data={
        'libTSCANAPI/windows/x64': ['libTSCAN.dll', 'libTSH.dll',],
        'libTSCANAPI/windows/x86': ['libTSCAN.dll', 'libTSH.dll','libLog.dll','binlog.dll',],
        'libTSCANAPI/linux': ['libTSCANApiOnLinux.so','libTSH.so','libASCLog.so'],
      },
      # package_data={
      #   'libTSCANAPI/windows/x64': ['libTSCAN.dll', 'libTSH.dll',],
      #   'libTSCANAPI/windows/x86': ['libTSCAN.dll', 'libTSH.dll','libLog.dll','binlog.dll',],
      #   'libTSCANAPI/linux': ['libTSCANApiOnLinux.so','libTSH.so'],
      #   'DataBases':['CAN_FD_Powertrain.dbc','PowerTrain_v2.xml'],
      #   'Demo':['libTSCAN_PyDemo.ui','Ui_libTSCAN_PyDemo.py','libTSCANAPI_Demo.py'],
      #   'Demo/icon':['058.svg','077.svg','079.svg','092.svg','267.svg','295.svg','318.svg','TOSUN_Pic2.png']
      # },
      platforms=["any"],
      classifiers=[
          'Intended Audience :: Developers',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Topic :: Software Development :: Libraries'
      ],
      )
