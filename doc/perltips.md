# Perlの小技集

### 引数として複数のオプションを指定する方法
```
use Getopt::Long;

my ($tree, $name);

GetOptions(
    "tree=s" => \$file_tree,
    "name=s" => \$file_name
    );
```

### 頭に0をつけて数字を13桁にする
```
$article_id = sprintf("%013d", $pmid)
```

### 配列の各要素で先頭と末尾のスペースを削除する
```
map{ $_ =~ s/^\s+//; $_ =~ s/\s+$//; } @ele; 
```
- map関数を使う
- ついつい結果を別の要素として受けたくなるが、@eleを直接書き換えるので `@arranged = map {...} @ele;` としなくてよい（というか、受けると多分 要素数だけ入る）

### 正規表現でメタ文字をメタ文字として処理しない
  - /マッチさせるもの/ とするが、えてしてマッチさせるものを変数でもってforeachするときなど、この中に Na+ のように * や + などが入っていると`Quantifier follows nothing in regex; marked by <-- HERE in m/+ <-- HERE` などと怒られる
  - `quotemeta`関数を使ってエスケープして使う
```
$match = quotemeta($match);
if ($target =~ /$match/) {
  ...
}
```


### PostgreSQLとの連携
```
use DBI;

my $dbname = "databasename";
my $host = "host.hoge.jp";
my $port = "5432";

my $schema = "schemaname";
my $table = "tablename";

my $dsn = "dbi:Pg:dbname=$dbname;host=$host;port=$port";
my $userid = "username";
my $password = "passwd1234";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 }) or die "接続失敗: $DBI::errstr";

my $sth = $dbh->prepare("SELECT * FROM $schema.$table");
$sth->execute();
#while (my @row = $sth->fetchrow_array()) {
#    print "Column1: $row[0], Column2: $row[1]\n";
#}
my @row = $sth->fetchrow_array();
print join("\t", @row)."\n";

my $hash_ref = $sth->fetchrow_hashref;
my %hash = %$hash_ref;
foreach $key (keys %hash) {
    print join("\t", $key, $hash{$key})."\n";
}
```


