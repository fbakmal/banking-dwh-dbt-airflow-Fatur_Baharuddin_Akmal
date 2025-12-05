select
    transaction_id,
    account_id,
    transaction_date,
    amount,
    transaction_type
from {{ ref('transactions') }}
