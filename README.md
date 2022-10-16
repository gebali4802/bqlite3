# BQLite3
* Better SQLite3
* BQLite3는 SQLite3의 개선판

# How To USE
* 저장
```py
bqlite.insert("database.db", "user", ("gebali4802", "girl")) # database.db파일에서 gebali4802를 girl로 user에다 저장한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 True를 리턴한다.
```
* 수정
```py
bqlite.update("database.db", "user", {"gender":"boy"}, {"name":"gebali4802"}) # database.db파일에서 gebali4802를 boy로 user에서 수정한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 True를 리턴한다.
```
* 삭제
```py
bqlite.delete("database.db", "user", {"name":"gebali4802"}) # database.db파일에서 name이 gebali4802인 사람을 user에서 삭제한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 True를 리턴한다.
```
* 조사
```py
bqlite.selectOne("database.db", "user", {"name":"gebali4802"}, "fetchone") # database.db파일에서 name이 gebali4802를 user에서 fetchon메소드로 조사한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 결과를 리턴한다.
```
```py
bqlite.selectMany("database.db", "user", "fetchall") # database.db파일에서 user을 fetchall메소드로 조사한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 결과를 리턴한다.
```
