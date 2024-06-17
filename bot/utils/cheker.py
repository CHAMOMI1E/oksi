from db.SQL.requests.user import search_for_id, add_user


async def start_checker(id_tg: int):
    query = await search_for_id(id_tg)
    if query:
        return None
    else:
        await add_user(id_tg)
