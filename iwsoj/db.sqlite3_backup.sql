BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tasks_io" (
	"id"	INTEGER NOT NULL,
	"input"	TEXT NOT NULL,
	"output"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "submissions_submission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"status"	varchar(12) NOT NULL,
	"sourceCode"	text NOT NULL,
	"language"	varchar(8) NOT NULL,
	"createdate"	datetime NOT NULL,
	"error"	text,
	"task_id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	FOREIGN KEY("task_id") REFERENCES "tasks_task"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "tasks_task" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(255) NOT NULL UNIQUE,
	"statement"	text NOT NULL,
	"createdate"	datetime NOT NULL,
	"complexity"	integer NOT NULL,
	"input"	text NOT NULL,
	"output"	text NOT NULL
);
CREATE TABLE IF NOT EXISTS "authtoken_token" (
	"key"	varchar(40) NOT NULL,
	"created"	datetime NOT NULL,
	"user_id"	integer NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("key")
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag">=0),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "tasks_io" VALUES (1,'21
34
325','8
11
66
');
INSERT INTO "tasks_io" VALUES (2,'10
8
','* 
* * 
* * * 
* 
* * 
* * * 
* * * * 
* * * * * ');
INSERT INTO "tasks_io" VALUES (3,'1
4
8
','4
');
INSERT INTO "tasks_io" VALUES (4,'ala
anna
kwakwa
wada','Yes
Yes
No
No
');
INSERT INTO "tasks_io" VALUES (5,'12
16
81
243','4
81
');
INSERT INTO "tasks_io" VALUES (6,'256
576
24
31','2304
744
');
INSERT INTO "tasks_io" VALUES (7,'1249.99
342.57','500
500
200
20
20
5
2
2
0.50
0.20
0.20
0.05
0.02
0.02
200
100
20
20
2
0.50
0.05
0.02');
INSERT INTO "tasks_io" VALUES (8,'3
5
7
10
15','2
5
13
55
610');
INSERT INTO "tasks_io" VALUES (9,'10
16
','4
8
');
INSERT INTO "tasks_io" VALUES (10,'10
20
30
','17
77
129');
INSERT INTO "tasks_io" VALUES (11,'5
96
35
23
-8
123','54');
INSERT INTO "tasks_task" VALUES (1,'Count prime numbers','Write a program to count number of prime numbers between 2 and n.
Input (must be an integer at least 2):
n
Output:
result','2019-11-04T20:30:08.207004Z',1,'21
34
325','8
11
66');
INSERT INTO "tasks_task" VALUES (2,'Pascal triangle','Write a program to write first n levels of Pascal triangle.
Remember about a space between two numbers and enter at the end
of the line!
Input (must be integer over 0):
n
Output:
result','2019-11-04T20:30:08.207004Z',1,'10
8','1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1 
1 8 28 56 70 56 28 8 1 
1 9 36 84 126 126 84 36 9 1 
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1 
');
INSERT INTO "tasks_task" VALUES (3,'Quadratic equation','Write a program to calculate value of x in quadratic equation
a*x^2+b*x+c=0.
Input (all 3 parameters are float):
a
b
c
Output:
Result
one or two results of the equation.
Important information:
Return the results to the nearest six decimal places!','2019-11-04T20:30:08.207004Z',1,'1
4
8','4');
INSERT INTO "tasks_task" VALUES (4,'Palindrome','Write a program to check, if the word is a palindrome.
Input:
word
Output:
Yes/No','2019-11-05T20:30:08.207004Z',1,'ala
anna
kwakwa
wada','Yes
Yes
No
No');
INSERT INTO "tasks_task" VALUES (5,'GCD','Write a program to calculate the Greatest Common Divisor of two integers.
Input:
a b - two integers
Output:
result','2019-11-05T20:30:08.207004Z',1,'12
16
81
243','4
81');
INSERT INTO "tasks_task" VALUES (6,'LCM','Write a program to calculate the Lowest Common Multiple of two integers.
Input:
a b - two integers
Output:
result','2019-11-05T20:30:08.207004Z',1,'256
576
24
31','2304
744');
INSERT INTO "tasks_task" VALUES (7,'Cash mashine','Write a program to change amount in EURO and EUROCENTS for at least possible number of banknotes and coins.
Possible banknotes: 500, 200, 100, 50, 20, 10, 5
Possible coins: 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01
Input (amount is a float with two decimal digits):
amount
Output:
result','2019-11-05T20:30:08.207004Z',1,'1249.99
342.57','500
500
200
20
20
5
2
2
0.50
0.20
0.20
0.05
0.02
0.02
200
100
20
20
2
0.50
0.05
0.02');
INSERT INTO "tasks_task" VALUES (8,'Fibonacci numbers','Write a program to calculate the n - th element of Fibonacci sequence.
n is an integer over 0.
Input:
n
Output:
result','2019-11-05T20:30:08.207004Z',1,'3
5
7
10
15','2
5
13
55
610');
INSERT INTO "tasks_task" VALUES (9,'Triangle of stars','Write a program to draw a triangle from stars.
n
Output:
result','2019-11-05T20:30:08.207004Z',1,'10
16','4
8');
INSERT INTO "tasks_task" VALUES (10,'Addition prime numbers','Write a program to calculate an addition of prime numbers between 2 and n.
Input (must be an integer at least 2):
n
Output:
result','2019-11-05T20:30:08.207004Z',1,'10
20
30','17
77
129');
INSERT INTO "tasks_task" VALUES (11,'Average','Write a program to calculate an average of n float numbers.
Result must be an integer round to the nearest number.

Input (must be an integer at least 1):
n (first parameter is an INT number of float parameters)
now write n FLOAT  parameters
Output:
result','2019-11-18T12:12:08.207004Z',1,'5
96
35
23
-8
123','54');
INSERT INTO "tasks_task" VALUES (12,'Binary search','Implement binary search algorithm.
Input:
min max x
min - minimum number INT
max - maximum number INT
x - found INT
Output:
middle counter
middle - index of x-element in table from min to max
counter - numer of recursions
','2019-11-18T14:17:08.207004Z',2,'1 100 49
1 100 1
-4 35 -7
53 25 25
352 354 353
','48 7
0 6
The element not exists in table!
Uncorrect number of parameters!
1 1
');
INSERT INTO "tasks_task" VALUES (13,'Body Mass Index','Calculate body mass index and return information about his mass.
Input:
growth mass
growth is Float in cm, mass is Float in kg
Output:
underweight (if BMI < 18.5)
healthy mass (if 18.5 <= BMI < 25.0)
overweight (if 25.0 <= BMI < 30.0)
obesity (if 30 <= BMI)


','2019-11-18T14:42:08.207004Z',1,'170 36
188 96
160 94
188 83

','underweight
overweight
obesity
healthy mass
');
INSERT INTO "tasks_task" VALUES (14,'Bubble sort','Implement bubble sort of INT numbers. Return number of swaps.
Input:
n - first parameter INT number of swaps
n INT numbers to sort
Output:
number of swaps between numbers INT','2019-11-18T14:59:08.207004Z',2,'6
1
5
4
3
2
6','6
');
INSERT INTO "tasks_task" VALUES (15,'Count coprime numbers','Count coprime numbers with n between 2 and n-1.
Input:
n (INT number 2 or more)
Output:
result (INT number)','2019-11-18T15:33:08.207004Z',1,'-5
10
17
20
30
53
40','-5
10
17
20
30
53
40');
INSERT INTO "tasks_task" VALUES (16,'Investment','Calculate investment money from the capital.
Conditions:
1. the investment period is one year
2. interest is capitalized after the deposit period ends
3. the tax from interest is 19%, example:
interest gross: 7.49 PLN
tax base: 7 PLN (the tip below 0.50 is skipped)
tax: 1 PLN (theoretically 1.33 PLN, but the tip below 0.50 is skipped)
insterest net: 6.49 PLN
Warning: interest net from 7.50 PLN gross is 5.50 PLN

Parameter:
capital(Float) percentage(Float)
Return:
interest_net(Float)','2019-11-18T15:52:08.207004Z',2,'100 2.5
100 2.49
1000 2.5
10000 2.49
10000 1.2
5500 1.7','1.50
2.49
20.00
202.00
97.00
75.50
');
INSERT INTO "tasks_task" VALUES (17,'Prime factors','Write all prime factors from 2 to n for n.
Parameters:
n (INT number)
Return:
all parameter number

Example result for n=20
2
2
5
','2019-11-18T16:52:08.207004Z',2,'10
20
53
24
12
','2
5
2
2
5
53
2
2
2
3
2
2
3
');
INSERT INTO "tasks_task" VALUES (18,'Star triangle','Write a program to draw a triangle from the stars.
Use one space minimum at the begin of the new line.
Input:
n - number of levels (INT, 1 or more)
Output:
triangle

Example for n = 3
   * 
  * * 
 * * * ','2019-11-18T17:04:08.207004Z',1,'10
5
7
3
','          * 
         * * 
        * * * 
       * * * * 
      * * * * * 
     * * * * * * 
    * * * * * * * 
   * * * * * * * * 
  * * * * * * * * * 
 * * * * * * * * * * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
   * 
  * * 
 * * * 
');
INSERT INTO "tasks_task" VALUES (19,'Match pattern','Write a program to count a number of pattern is the word.
Input:
word[TEXT] pattern[TEXT]
output:
count[INTEGER]

Example:
Input:
alalalalaaalaala ala
Output:
6','2019-11-23T18:25:08.207004Z',2,'mamamaaama mama
ababbabababa abba
cat cat
mat meteusz','2
4
1
0');
INSERT INTO "tasks_task" VALUES (20,'Polish notation','Write a simple calculator in Polish notation.
We use only +, -, * and Integer numbers.
Example:
Input:
mathematical operation like * 5 + 6 4
Output:
50
(because it is de facto 5 * ( 6 + 4 ) = 50)','2019-11-23T18:39:08.207004Z',2,'* - 6 5 7
- * 35 + 4 5 3 4
2 2 +','7
941
4');
INSERT INTO "tasks_task" VALUES (21,'e-mail','Write a function to check if e-mail address is valid.
Input:
example_email
Output:
True/False','2019-11-23T18:39:08.207004Z',2,'rafal...ml@@o..2.pl
rafal.mlod@zsi..pg9...pl
rafal.ml@o2.pl','False
False
True');
INSERT INTO "tasks_task" VALUES (22,'Palindromes 0-1','Copyright: Eryk Trzeciakiewicz
Read n and list all palindromes of the length between 1 and n consisting of digits 0 and 1.
Input:
n (INTEGER)
Output:
all palindromes
Note:
The order is important:
0
1
00
11
000
010
101
111 etc.','2019-11-23T18:34:08.207004Z',2,'4','0
1
00
11
000
010
101
111
0000
0110
1001
1111
');
INSERT INTO "tasks_task" VALUES (23,'Loan and credit','Calculate all loan installments with decreasing installments.
We round off fractions when calculating the loan and interest installments. Example:
loan installment = 1333.3333333333 -> 1333.33
interest installment = 144.44444444 -> 144.44
Installment = 1333.33 + 144.44 = 1477.77
Input:
amount number_of_months percentage_per_year
Output:
number_of_month installment

Example:
48000 24 12
Note:

1 2480.00
2 2460.00
3 2440.00
4 2420.00
...
47 2040.00
48 - 2020.00

','2019-11-23T20:18:08.207004Z',3,'96000 24 12
','1 4960
2 4920
3 4880
4 4840
5 4800
6 4760
7 4720
8 4680
9 4640
10 4600
11 4560
12 4520
13 4480
14 4440
15 4400
16 4360
17 4320
18 4280
19 4240
20 4200
21 4160
22 4120
23 4080
24 4040');
INSERT INTO "tasks_task" VALUES (24,'School notes','Calculate weight average of school notes in Poland (from 1 to 6, without pluses and minuses).
Input:
all pairs
note weight
Output:
weight average (round to 2 digit numbers)','2019-11-23T21:24:08.207004Z',1,'5 8
4 6
6 6
4 6
5 5
4 5
6 5
4 5
5 4
6 4
1 2
4 2
6 2
','4.75');
INSERT INTO "tasks_task" VALUES (25,'Convert binary to decimal','Convert Integer number from binary to decimal.
If input number is not a binary number, return output ERROR.
Input:
binary
Output:
decimal

Example:
input:
101
output:
5','2019-11-23T22:13:08.207004Z',1,'100
101
1101
agr2
111100
110110
1101010
2425
1010010101','4
5
13
ERROR
60
62
106
ERROR
661
');
INSERT INTO "tasks_task" VALUES (26,'Convert decimal to binary','Convert Integer number from decimal to binary.
If input number is not a decimal number, return output ERROR.
Input:
decimal
Output:
binary

Example:
input:
5
output:
101','2019-11-23T22:48:08.207004Z',1,'4
5
13
abbf
60
62
106
a8gs
661
','100
101
1101
ERROR
111100
110110
1101010
ERROR
1010010101');
INSERT INTO "tasks_task" VALUES (27,'Post code','Write a function to check, if an example post-number is correct.
Input:
example_post_number
Output:
True/False','2019-11-23T23:08:08.207004Z',2,'58-316
Ferdek
51-522
a3-53s
53wizy
','True
False
True
False
False');
INSERT INTO "authtoken_token" VALUES ('d17b20651386f19dbda5bf40f1e4f36f21688677','2019-10-30 00:51:22.262918',1);
INSERT INTO "authtoken_token" VALUES ('8e0e2219c9f3c674640a56e7c4952fa35928a284','2019-10-31 21:27:01.008862',3);
INSERT INTO "authtoken_token" VALUES ('b97030b906f9df6676b7a0147ee5f60209873594','2019-11-02 06:01:19.929207',4);
INSERT INTO "authtoken_token" VALUES ('48cc4cbbcca94ef1136ef24137a7ecb127659a02','2019-11-02 06:43:27.045702',7);
INSERT INTO "authtoken_token" VALUES ('56e4d862d7d27321a3b800c63af8d98d3ae01fea','2019-11-02 08:36:34.786426',8);
INSERT INTO "authtoken_token" VALUES ('2c78c06575aea2e3f9a90f94df38e9f7fed100d2','2019-11-02 08:40:18.664206',9);
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$150000$MWE9wqKDTzje$Z2KdnwH7jduofJOmyr9xuM4/2Rz0aTo1zbHr6MjdnH0=',NULL,0,'rafal','Rafal','some@email.com',0,1,'2019-10-30 00:45:19.706560','');
INSERT INTO "auth_user" VALUES (2,'pbkdf2_sha256$150000$kyyPCpiTLUVp$eC6nt98WUNbVxc2A0H4ckOUXnd/mvkM2xAV2sKHxQF8=',NULL,0,'aaarafal','AAARafal','aaasome@email.com',0,1,'2019-10-31 20:58:09.045651','');
INSERT INTO "auth_user" VALUES (3,'pbkdf2_sha256$150000$O42enbsBXWOI$tC32iNWc8wM0IldehZYfz1TvB/8sBVN4iVxuycbq9eU=',NULL,0,'pikus','Pikus','pikus@ooo.pl',0,1,'2019-10-31 21:24:25.035937','');
INSERT INTO "auth_user" VALUES (4,'pbkdf2_sha256$150000$OOjQtBt93ELN$YvWRljam8vS/rQAdLMhOK0tU4abNI17oyopAXtR9QgU=',NULL,0,'abcdef','Grazyna','abcdef@abc.pl',0,1,'2019-11-02 06:00:47.979338','');
INSERT INTO "auth_user" VALUES (5,'pbkdf2_sha256$150000$c9kYcyy6SSTq$DDyxpxxySJ6TiXiO1mmS78OUPAiPoyKjTLUDbMd/1Vk=',NULL,0,'marek','Marek','marek@xxxxxxx.pl',0,1,'2019-11-02 06:27:15.699968','');
INSERT INTO "auth_user" VALUES (6,'pbkdf2_sha256$150000$Ht13FE0U02qG$cuPv3nZYcM3hMc4CI2NuZCcEEtpSZCY4u9J1FCX7Lp8=',NULL,0,'mikolaj','Mikolaj','mikolaj@stop.pl',0,1,'2019-11-02 06:31:53.944980','');
INSERT INTO "auth_user" VALUES (7,'pbkdf2_sha256$150000$LxeqLPCVxmb7$EiRKsYBKzyowxH+aPFAgc5wDfyfoJ7rkZcJOQqFeiUc=',NULL,0,'micky','Micky','micky@ox.pl',0,1,'2019-11-02 06:42:42.166010','');
INSERT INTO "auth_user" VALUES (8,'pbkdf2_sha256$150000$777y1EyoSa51$Fgv1rRImZ9efQkFsO3XzgmARv5c4y9mGRXYOIEwRMuI=',NULL,0,'maxim','Maxim','maxim@vl.pl',0,1,'2019-11-02 08:35:25.336369','');
INSERT INTO "auth_user" VALUES (9,'pbkdf2_sha256$150000$9sjFUbFb4L4W$HLqMjjfNJRAkXmimeyR24t3qt886OOwWuxtN5RNarI4=',NULL,0,'lektor','Lektor','lektor@lso.pl',0,1,'2019-11-02 08:39:37.771439','');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_task','Can add task');
INSERT INTO "auth_permission" VALUES (26,7,'change_task','Can change task');
INSERT INTO "auth_permission" VALUES (27,7,'delete_task','Can delete task');
INSERT INTO "auth_permission" VALUES (28,7,'view_task','Can view task');
INSERT INTO "auth_permission" VALUES (29,8,'add_token','Can add Token');
INSERT INTO "auth_permission" VALUES (30,8,'change_token','Can change Token');
INSERT INTO "auth_permission" VALUES (31,8,'delete_token','Can delete Token');
INSERT INTO "auth_permission" VALUES (32,8,'view_token','Can view Token');
INSERT INTO "auth_permission" VALUES (33,9,'add_submission','Can add submission');
INSERT INTO "auth_permission" VALUES (34,9,'change_submission','Can change submission');
INSERT INTO "auth_permission" VALUES (35,9,'delete_submission','Can delete submission');
INSERT INTO "auth_permission" VALUES (36,9,'view_submission','Can view submission');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'tasks','task');
INSERT INTO "django_content_type" VALUES (8,'authtoken','token');
INSERT INTO "django_content_type" VALUES (9,'submissions','submission');
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2019-10-30 00:14:11.302159');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2019-10-30 00:14:11.333415');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2019-10-30 00:14:11.349041');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2019-10-30 00:14:11.402426');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2019-10-30 00:14:11.418059');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2019-10-30 00:14:11.480557');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2019-10-30 00:14:11.502686');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2019-10-30 00:14:11.533943');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2019-10-30 00:14:11.549570');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2019-10-30 00:14:11.580816');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2019-10-30 00:14:11.596440');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2019-10-30 00:14:11.634200');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2019-10-30 00:14:11.665452');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2019-10-30 00:14:11.703210');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2019-10-30 00:14:11.734468');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2019-10-30 00:14:11.765723');
INSERT INTO "django_migrations" VALUES (17,'sessions','0001_initial','2019-10-30 00:14:11.781343');
INSERT INTO "django_migrations" VALUES (18,'tasks','0001_initial','2019-10-30 00:14:11.803477');
INSERT INTO "django_migrations" VALUES (19,'authtoken','0001_initial','2019-10-30 00:42:32.543707');
INSERT INTO "django_migrations" VALUES (20,'authtoken','0002_auto_20160226_1747','2019-10-30 00:42:32.628576');
INSERT INTO "django_migrations" VALUES (21,'tasks','0002_auto_20191029_1004','2019-10-30 00:42:32.651986');
INSERT INTO "django_migrations" VALUES (22,'submissions','0001_initial','2019-10-30 00:42:32.681251');
CREATE INDEX IF NOT EXISTS "submissions_submission_user_id_f185a147" ON "submissions_submission" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "submissions_submission_task_id_6120ad48" ON "submissions_submission" (
	"task_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
