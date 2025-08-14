from db import create_table

create_table(
    """
		DROP TABLE IF EXISTS public.test_sokolov;
    CREATE TABLE public.test_sokolov(
        date DATE,
        id INTEGER,
        title VARCHAR(50),
				course_year INTEGER,
				liter INTEGER,
				site VARCHAR(50),
				trimester INTEGER,
				school_year VARCHAR(50),
				course_name VARCHAR(50),
				teacher VARCHAR(50),
        score INTEGER,
        weight INTEGER,
        lesson_comment VARCHAR(500),
        score_comment VARCHAR(500)
    )
    """
)