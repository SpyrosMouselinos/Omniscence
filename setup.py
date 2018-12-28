from distutils.core import setup
setup(
    name = 'Omniscence',         
    packages = ['Omniscence'],   
    version = '0.1',      
    license='MIT', 
    description = 'A fully automated data-analysis library tool',  
    author = 'Spyridon Mouselinos',                   
    author_email = 'mouselinos.spur.kw@gmail.com',      
    url = 'https://github.com/SpyrosMouselinos/Omniscence.git',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/SpyrosMouselinos/Omniscence/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['Big Data', 'Data Analysis', 'Data Engineering' , 'Machine Learning', 'Neural Networks'],   
  install_requires=[          
          'numpy',
          'pandas',
          'seaborn',
          'matplotlib',
          'sklearn'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)