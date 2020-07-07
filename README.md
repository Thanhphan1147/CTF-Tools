### Blind SQL injection
Blind SQL injection is used when a web application is vulnerable to an SQL injection but the results of the injection are not visible to the attacker.
The page with the vulnerability may not be one that displays data but will display differently depending on the results of a logical statement injected into the legitimate SQL statement called for that page. 
This type of attack has traditionally been considered time-intensive because a new statement needed to be crafted for each bit recovered, and depending on its structure, the attack may consist of many unsuccessful requests.

### SQL injection with SLEEP()

In totally blinds you need to use some waiting functions and analyze response times. For this you can use WAITFOR DELAY '0:0:10' in SQL Server, BENCHMARK() and sleep(10) in MySQL, pg_sleep(10) in PostgreSQL, and some PL/SQL tricks in ORACLE.

### XOR known plain-text attack
The known-plaintext attack (KPA) is an attack model for cryptanalysis where the attacker has access to both the plaintext (called a crib), and its encrypted version (ciphertext). 
These can be used to reveal further secret information such as secret keys and code books.
```
crib ^ secret = ciphertext
crib ^ ciphertext = secret
```

### Session hijacking

Session Hijacking / Cookie hijacking is the exploitation of a valid computer session—sometimes also called a session key—to gain unauthorized access to information or services in a computer system. 
In particular, it is used to refer to the theft of a magic cookie used to authenticate a user to a remote server. If the serverside cookies are not generated randomly, it can be hijacked using various brute-forcing techniques.
