# Perlの小技集

- 頭に0をつけて数字を13桁にする
```
$article_id = sprintf("%013d", $pmid)
```

- 正規表現でメタ文字をメタ文字として処理しない
  - /マッチさせるもの/ とするが、えてしてマッチさせるものを変数でもってforeachするときなど、この中に Na+ のように * や + などが入っていると`Quantifier follows nothing in regex; marked by <-- HERE in m/+ <-- HERE` などと怒られる
  - `quotemeta`関数を使ってエスケープして使う
```
$match = quotemeta($match);
if ($target =~ /$match/) {
  ...
}
```


- PostgreSQLとの連携
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


