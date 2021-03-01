-- Lists all records
ALTER DATABASE
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;
ALTER TABLE
    first_table
    CONVERT TO CHARACTER 
    SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
ALTER TABLE
    first_table
    CHANGE name
    VARCHAR(191)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;