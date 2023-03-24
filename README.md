# blank lambda for terraform

Terraform で AWS Lambda を管理する時、コード自体は Terraform の外で管理したい。
ただし、Terraform で最初に関数を定義する必要があるので、その関数をここで用意する。

参考にしたサイトは[こちら](https://blog.nijohando.jp/post/2020/partially-managing-lambda-with-terraform/)

## 準備

`./deploy` 以下にある `dot.env`, `dot.envrc` をそれぞれ `.env`, `.envrc` とし、`AWS_PROFILE` を `.env` に書き込む。
下記コマンドを実行し、`.envrc` を有効にする。

```bash
direnv allow
```

## 使い方

Terraform で定義した名称に従って、[`config.json`](./deploy/config.json) の内容を修正し、下記を実行。

```bash
python update.py
```

下記にファイルが出来上がる。

```text
s3://{bucket}/{module}/{function_name}/lambda.zip"
```
