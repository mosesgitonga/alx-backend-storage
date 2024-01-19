-- email validation to sent

DELIMITER //

CREATE TRIGGER email_validation
AFTER UPDATE
ON users
FOR EACH Row
BEGIN
    UPDATE users
    SET email = NEW.email;
END;

DELIMITER;
