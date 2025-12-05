select
    customer_id,
    first_name || ' ' || last_name as customer_name,
    registration_date
from {{ source('raw_bank', 'customer') }}
