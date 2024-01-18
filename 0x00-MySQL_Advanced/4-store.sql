-- update item table when item is ordered

DELIMITER //

CREATE TRIGGER after_insert 
AFTER INSERT
ON orders
FOR EACH ROW
BEGIN
    -- DECREASE QUANTITY IN ITEM TABLE
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;

DELIMITER;