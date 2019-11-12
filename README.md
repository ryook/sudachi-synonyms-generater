# sudachi-synonyms-generater

WorksApplicationsが公開している[Sudachi同義語辞書](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)をcsv形式に変換するスクリプトです。



# howitworks
コマンドライン引数でファイル名、対象分野を指定

|引数| 型| 説明| |
|--- | ---|---| --- |
|file_name| 文字列 | ファイル名(csv) | 必須(第１引数) |
|fields| list | [分野情報](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md#7--%E5%88%86%E9%87%8E%E6%83%85%E5%A0%B1)。カンマ指定で複数指定. 未定の場合はすべて対象| |




```
> python generater output.csv --fields=企業,組織
```


# example
output/　参照

# Licenses
元になるSudachi同義語辞書に従い[Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html)です。

licensed under the Apache License, Version2.0
