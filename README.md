# AtCoder
AtCoderのリポジトリ

procon-gardener (https://github.com/togatoga/procon-gardener) を使ってAtCoderの提出から自動的にコードを取得
<hr>

### インストール
```
% go get github.com/togatoga/procon-gardener
```

### 設定ファイルの初期化
```
% procon-gardener init
```

### 設定ファイルの編集
```.procon-gardener/config.json```を開き、`repository_path`、`user_id`、`user_email`を設定

### AtCoderからファイルを取得
```
% procon-gardener archive
```
