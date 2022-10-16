# BQLite3
* Better SQLite3
* 파이썬의 SQLite3의 개선판입니다.

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

# Precautions
* BQLite3로 조사할때 주의할점
* 메소드를 `fetchone`이나 `fetchall`으로 작성해야합니다.
* 아래의 코드는 `SQLite3`로 작성한 파일이 있을때의 예시입니다.
* 만약에 없다면 파일을 `SQLite3`로 생성하세요.
* 오류가 있다면 `CR9#5759`으로 연락주세요.

# Code
```py
import bqlite3

bqlite = bqlite3.Bqlite3()

bqlite.insert("database.db", "user", ("gebali4802", "girl")) # database.db파일에서 gebali4802를 girl로 user에다 저장한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 True를 리턴한다.

bqlite.update("database.db", "user", {"gender":"boy"}, {"name":"gebali4802"}) # database.db파일에서 gebali4802를 boy로 user에서 수정한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 True를 리턴한다.

bqlite.delete("database.db", "user", {"name":"gebali4802"}) # database.db파일에서 name이 gebali4802인 사람을 user에서 삭제한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 True를 리턴한다.

bqlite.selectOne("database.db", "user", {"name":"gebali4802"}, "fetchone") # database.db파일에서 name이 gebali4802를 user에서 fetchon메소드로 조사한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 결과를 리턴한다.

bqlite.selectMany("database.db", "user", "fetchall") # database.db파일에서 user을 fetchall메소드로 조사한다.
# 오류가 있으면 False를 리턴한다. 오류가 없으면 결과를 리턴한다.
```

###### 대놓고 heist332님의 Fast-Sqlite3를 참고했습니다.
