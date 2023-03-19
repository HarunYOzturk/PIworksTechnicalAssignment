
SELECT
    Device_Type,
    SUBSTRING(
        Stats_Access_Link, 
        CHARINDEX('://', Stats_Access_Link) + 3, 
        LEN(Stats_Access_Link) - CHARINDEX('://', Stats_Access_Link) - 8
    ) AS domain_name
FROM Device;


