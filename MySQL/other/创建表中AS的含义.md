# [返回目录](MySQL.MD)
# 基本信息

项目：
主要内容：创建表中AS的含义
开始时间：2023 年 11 月 30 日
结束时间：

***
在 SQL 语句中，`AS` 关键字用于指定别名。别名是给查询结果中的列或者表指定一个新的名称，这样做可以使得列名更易读，或者当查询涉及到多个表时，使用别名可以避免列名或表名的冲突。
具体来说，`AS` 有以下几个用法：
1. **列别名**：在 `SELECT` 查询中，`AS` 用于给选中的列指定一个别名。例如，如果你有一个 `student` 表，里面有一个 `name` 字段，你想要在结果集中显示为“姓名”而不是“name”，那么你可以这样写：
   ```sql
   SELECT name AS 姓名 FROM student;
   ```
   这样，查询结果集中的 `name` 列就会显示为“姓名”。
2. **表别名**：在复杂的查询中，如果涉及到多个表，可以使用 `AS` 给表指定别名。例如：
   ```sql
   SELECT s.name AS 学生姓名， c.name AS 课程名称
   FROM student AS s
   JOIN course AS c ON s.course_id = c.id;
   ```
   在这个例子中，`student` 表被指定了一个别名 `s`，`course` 表被指定了一个别名 `c`，这样做使得查询语句更简洁，更容易理解。
3. **创建表时使用别名**：在 `CREATE TABLE` 语句中，`AS` 可以用于创建一个新表，并将另一个表中的所有数据复制到这个新表中。例如：
   ```sql
   CREATE TABLE new_table AS SELECT * FROM old_table;
   ```
   这条语句会创建一个名为 `new_table` 的新表，并将 `old_table` 表中的所有数据复制到 `new_table` 中。
4. **创建过程时使用别名**：在定义存储过程时，`AS` 用于定义过程中的变量或者参数。例如：
   ```sql
   CREATE PROCEDURE get_student_name AS
   BEGIN
       -- 过程体
   END;
   ```
   在这个例子中，`AS` 后面跟的是过程体，它定义了存储过程中的操作。
综上所述，`AS` 在 SQL 语句中是一个非常重要的关键字，它用于定义别名，使得数据库的操作更加灵活和方便。