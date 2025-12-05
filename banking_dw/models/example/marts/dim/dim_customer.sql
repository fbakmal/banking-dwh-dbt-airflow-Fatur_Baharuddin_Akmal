select
    customer_id as dim_customer_key,
    first_name,
    last_name,
    postal_code,
    registration_date,
    last_updated
from {{ ref('stg_customer') }}
