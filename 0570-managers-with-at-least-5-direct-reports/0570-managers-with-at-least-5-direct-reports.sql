/* need a subquery where we get the number per manager 
/* then connect with personal id  */
WITH Managers AS (
    SELECT 
        managerId, 
        COUNT(*) AS reports
        FROM
            Employee
        GROUP BY managerId
        HAVING reports >= 5
)
    SELECT
        name
        FROM Employee 
        JOIN Managers
        ON Employee.id = Managers.managerId;
