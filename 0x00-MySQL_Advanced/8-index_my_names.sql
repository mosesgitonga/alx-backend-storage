-- creating index

CREATE INDEX idx_name_first ON names SUBSTRING(name(1));