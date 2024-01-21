-- safe divide

CREATE OR REPLACE FUNCTION safe_div(a INT, b INT)
RETURNS INT
AS $$
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;
$$ LANGUAGE plpgsql;