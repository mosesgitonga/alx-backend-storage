-- creating index

CREATE INDEX idx_name_first ON names SUBSTRING(name FROM 1 for 1);