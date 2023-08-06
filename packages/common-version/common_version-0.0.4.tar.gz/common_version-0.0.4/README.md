# common_version

基于包管理器以及漏洞网站的版本表达式统一化

. code-block:: bash

    git clone https://github.com/hsc1102/common_version.git
    cd common_version
    pip install "flake8<3.8" bumpversion pep8-naming
    flake8 --install-hook git
    git config --bool flake8.strict true

版本发布
--------

. code-block:: bash

    bumpversion patch
    git push origin master --tags
    git pull && bumpversion patch && git push origin master --tags


. code-block:: bash

    pip install twine whell
    python setup.py sdist bdist_wheel
    twine upload dist/*
