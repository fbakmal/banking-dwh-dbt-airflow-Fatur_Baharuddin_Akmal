select
    account_id,
    customer_id,
    current_balance,
    close_date
from {{ source('raw_bank', 'account') }}
