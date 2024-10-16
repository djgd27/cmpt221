from sqlalchemy import delete

stmt = (
    delete(user_table).
    where(user_table.c.id == 5)
)