-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH teacher_grades AS (
    -- Find the teacher who graded the most assignments
    SELECT teacher_id, COUNT(*) AS total_graded
    FROM assignments
    WHERE grade IS NOT NULL
    GROUP BY teacher_id
    ORDER BY total_graded DESC
    LIMIT 1
)
-- Count how many grade 'A' assignments were given by that teacher
SELECT COUNT(*) AS total_A_grades
FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM teacher_grades)
AND grade = 'A';
