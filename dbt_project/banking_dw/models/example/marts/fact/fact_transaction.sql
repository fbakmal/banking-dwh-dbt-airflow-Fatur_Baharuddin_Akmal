select
    transaction_id as fact_transaction_key,
    account_id,
    transaction_date,
    amount,
    transaction_type
from {{ ref('stg_transaction') }}
