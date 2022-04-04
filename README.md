# Hargreaves Lansdown Tech Task

* [Task 1 - XYZ Bank](#task_1)
* [Task 2 - XYZ Bank (SQL query)](#task_2)
* [Task 3 - XYZ Bank (SQL query to return customers with no accounts)](#task_3)
* [Task 4 - ABC ltd Data Warehouse model](#task_4)
* [Task 5 - Data stage process](#task_5)
* [Task 6 - IMDb Python task (link to code)](#task_6)


## Task_1


wWriting 

![XYZ Bank entity relationship diagram](xyz_bank_erd.png "XYZ Bank entity relationship diagram")


## Task_2 

XYZ Bank (SQL query to return multiple accounts)

```
SELECT a.customer_id, c.total_balance, COUNT(a.customer_id) AS no_of_accounts
FROM accounts a
INNER JOIN customers c ON (s.customer_id = a.customer_id)
GROUP BY a.customer_id
HAVING COUNT(a.customer_id) > 1
ORDER BY no_of_accounts DESC;
```

## Task_3

XYZ Bank (SQL query to return customers with no accounts)

```
SELECT a.customer_id
FROM accounts a
WHERE a.customer_id NOT IN
    (SELECT c.customer_id 
     FROM customer c);
```

OR

```
SELECT a.customer_id
FROM accounts a 
WHERE NOT EXISTS 
    (SELECT * 
     FROM customer c
     WHERE c.customer_id = a.customer_id);
```


## Task_4

ABC ltd Data Warehouse model


## Task_5

A data stage process was previously taking 10 minutes to run.  Now it’s taking an hour to complete.  Detail the possible causes and how you would determine which was responsible


## Task_6

Link to Python code:

* [IMDb code](task_6_imdb_code/)

* [main.py file](task_6_imdb_code/main.py)

Pseudo code version
