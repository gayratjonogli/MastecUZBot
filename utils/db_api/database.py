from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) " \
              "VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def is_user(self, telegram_id):
        sql = f"SELECT * FROM Users WHERE telegram_id = '{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def create_table_groups(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Groups (
        id SERIAL PRIMARY KEY, 
        group_name VARCHAR (255) NOT NULL UNIQUE, 
        group_id BIGINT NOT NULL UNIQUE,
        status INTEGER
        );
        """
        await self.execute(sql, execute=True)

    async def add_group(self, group_name, group_id, status=1):
        sql = """
        INSERT INTO Groups (group_name, group_id, status) VALUES ($1, $2, $3) returning *
        """
        return await self.execute(sql, group_name, group_id, status, fetchrow=True)

    async def show_groups_name(self):
        sql = """
        SELECT group_name FROM Groups
        """
        return await self.execute(sql, fetch=True)

    async def update_group_status(self, group_id):
        sql = f"""
        UPDATE Groups SET status='{0}' WHERE group_id='{group_id}'
        """
        return await self.execute(sql, execute=True)

    async def update_status(self):
        sql = f"""
        UPDATE Groups SET status='{1}'
        """
        return await self.execute(sql, execute=True)

    async def show_id_by_name(self, name):
        sql = f"""
        SELECT group_id FROM GROUPS WHERE group_name = '{name}'
        """
        return await self.execute(sql, fetchval=True)

    async def check_name(self, group_name):
        sql = f"""
        SELECT EXISTS (SELECT 1 FROM Groups WHERE group_name = '{group_name}');
        """
        return await self.execute(sql, fetchval=True)

    async def check_id(self, id):
        sql = f"""
        SELECT EXISTS (SELECT 1 FROM Groups WHERE group_id = '{id}');
        """
        return await self.execute(sql, fetchval=True)

    async def show_groups_id(self):
        sql = """
        SELECT group_id FROM Groups
        """
        return await self.execute(sql, fetch=True)

    async def show_all(self):
        sql = """
        SELECT * FROM Groups
        """
        return await self.execute(sql, fetch=True)

    async def show_both(self):
        sql = """
        SELECT group_name, group_id from Groups
        """
        return await self.execute(sql, fetch=True)

    async def show_bothStatus(self):
        sql = f"""
        SELECT group_name from Groups WHERE status = '{1}'
        """
        return await self.execute(sql, fetch=True)

    async def show_bothStatusID(self):
        sql = f"""
        SELECT group_id from Groups WHERE status = '{1}'
        """
        return await self.execute(sql, fetch=True)

    async def delete_group_by_name(self, group_name):
        await self.execute(f"DELETE FROM Groups WHERE group_name = '{group_name}'", execute=True)

    async def delete_table_groups(self):
        await self.execute("DROP TABLE Groups", execute=True)
#########################################
    async def create_tableSpecialGroups(self):
        sql = """
        CREATE TABLE IF NOT EXISTS SpeacialGroups (
        id SERIAL PRIMARY KEY, 
        group_name VARCHAR (255) NOT NULL UNIQUE, 
        group_id BIGINT NOT NULL UNIQUE,
        status INTEGER
        );
        """
        await self.execute(sql, execute=True)


    async def add_Sgroup(self, group_name, group_id, status=1):
        sql = """
        INSERT INTO SpeacialGroups (group_name, group_id, status) VALUES ($1, $2, $3) returning *
        """
        return await self.execute(sql, group_name, group_id, status, fetchrow=True)

    async def show_Sgroups_name(self):
        sql = """
        SELECT group_name FROM SpeacialGroups
        """
        return await self.execute(sql, fetch=True)

    async def update_Sgroup_status(self, group_id):
        sql = f"""
        UPDATE SpeacialGroups SET status='{0}' WHERE group_id='{group_id}'
        """
        return await self.execute(sql, execute=True)

    async def update_Sstatus(self):
        sql = f"""
        UPDATE SpeacialGroups SET status='{1}'
        """
        return await self.execute(sql, execute=True)

    async def show_id_by_Sname(self, name):
        sql = f"""
        SELECT group_id FROM SpeacialGroups WHERE group_name = '{name}'
        """
        return await self.execute(sql, fetchval=True)

    async def check_Sname(self, group_name):
        sql = f"""
        SELECT EXISTS (SELECT 1 FROM SpeacialGroups WHERE group_name = '{group_name}');
        """
        return await self.execute(sql, fetchval=True)

    async def check_Sid(self, id):
        sql = f"""
        SELECT EXISTS (SELECT 1 FROM SpeacialGroups WHERE group_id = '{id}');
        """
        return await self.execute(sql, fetchval=True)

    async def show_Sgroups_id(self):
        sql = """
        SELECT group_id FROM SpeacialGroups
        """
        return await self.execute(sql, fetch=True)

    async def show_Sall(self):
        sql = """
        SELECT * FROM SpeacialGroups
        """
        return await self.execute(sql, fetch=True)

    async def show_Sboth(self):
        sql = """
        SELECT group_name, group_id from SpeacialGroups
        """
        return await self.execute(sql, fetch=True)

    async def show_SbothStatus(self):
        sql = f"""
        SELECT group_name from SpeacialGroups WHERE status = '{1}'
        """
        return await self.execute(sql, fetch=True)

    async def show_SbothStatusID(self):
        sql = f"""
        SELECT group_id from SpeacialGroups WHERE status = '{1}'
        """
        return await self.execute(sql, fetch=True)

    async def delete_Sgroup_by_name(self, group_name):
        await self.execute(f"DELETE FROM SpeacialGroups WHERE group_name = '{group_name}'", execute=True)

    async def delete_Stable_groups(self):
        await self.execute("DROP TABLE SpeacialGroups", execute=True)
