select
    account_id,
    transaction_date,
    sum(amount) over (
        partition by account_id
        order by transaction_date
        rows between unbounded preceding and current row
    ) as running_balance
from {{ ref('stg_transaction') }}
