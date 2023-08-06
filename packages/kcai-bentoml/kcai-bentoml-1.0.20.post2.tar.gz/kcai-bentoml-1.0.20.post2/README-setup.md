### build 방법
```
1. prerequisite
$ python -m pip install --upgrade build
$ python -m pip install --upgrade twine

$ vi pyproject.toml 에서 버전 수정
version = "1.0.20-{seq num}"
ex) "1.0.20-1"

$ vi /src/bentoml/_internal/bento/build_config.py 에서 버전 수정
ex) kcai-bentoml=="$BENTOML_VERSION".post1

2. build
$ python -m build

...
Successfully built kcai-bentoml-1.0.22.tar.gz and kcai_bentoml-1.0.22-py3-none-any.whl

3. deploy (cdpdev 계정)
$ python -m twine upload dist/*

Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: cdpdev
Enter your password: 
Uploading kcai_bentoml-1.0.22-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB • 00:02 • 561.6 kB/s
Uploading kcai-bentoml-1.0.22.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.9/19.9 MB • 00:01 • 14.0 MB/s
```

### setup
```
1. pip upgrade
$ pip install --upgrade pip

2. install
$ pip install kcai-bentoml==1.0.20.post1
```