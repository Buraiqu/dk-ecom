CREATE [OR REPLACE] PROCEDURE procedure_name 
(argument_mode(IN/OUT) Parameters datatype,......)
LANGUAGE 'plpgsql' --in case of pastgresql
AS
$$
BEGIN
    -- SQL statements to be executed
END;
$$;


CALL procedure_name(parameter_value);


CREATE OR REPLACE PROCEDURE update_emp(
    IN emp_id numeric,
    IN emp_salary numeric
) 
LANGUAGE 'plpgsql'                                                                                                                                                                            LANGUAGE 'plpgsql'
AS 
$$
BEGIN
    UPDATE employee
    SET salary = emp_salary
    WHERE id = emp_id;
END;
$$;


CALL update_emp(2);

CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

SELECT * FROM physics_failed;


CREATE VIEW physics_failed AS
SELECT student.student_name, student.class grade.grade
FROM student
INNER JOIN student_grade ON student.id = student_grade.student_id
WHERE grade.subject = 'physics' AND student_grade.grade = 'F';


CREATE INDEX index_name ON table_name (column_name);

CREATE INDEX employee_mail ON emmployee (mail);

SELECT id, name, department FROM employee WHERE mail = 'arun@gmail.com';