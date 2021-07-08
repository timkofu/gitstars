import os
import math
import asyncio
import logging
from typing import List, AsyncGenerator, Set, Tuple, Union, cast, Any

from github import Github


from ghs.model.infrastructure.repository.repository import Repository


class Update:
    """Fetch stars and store them in DB"""

    __slots__ = ("ghh", "dbh", "conn_creds")

    def __init__(
        self,
        conn_creds: dict[str, str],
        ghh: Github = Github(login_or_token=os.getenv("GH_AUTH_TOKEN")),
    ) -> None:
        self.ghh: Github = ghh
        self.conn_creds = conn_creds

    async def _set_dbh(self) -> None:
        self.dbh = cast(
            Repository, await Repository.get_database_handle(conn_creds=self.conn_creds)
        )

    async def _fetch_stars(self) -> AsyncGenerator[List[Any], None]:

        await self._set_dbh()

        user = await asyncio.get_running_loop().run_in_executor(
            None, self.ghh.get_user  # get the owner of the auth token
        )
        stars = await asyncio.get_running_loop().run_in_executor(None, user.get_starred)
        pages: int = math.ceil(stars.totalCount / 30)  # GitHub pagination count

        for page in range(pages):

            yield await asyncio.get_event_loop().run_in_executor(
                None, stars.get_page, page
            )

            # await asyncio.sleep(1)  # Give GH server a break
            # not needed apparently, GH can handle it

    async def stars(self) -> None:

        await self._set_dbh()

        logging.getLogger("uvicorn").info("GHS: Starting update ...")

        current_stars: Set[str] = set()  # For use in removing unstared projects

        async for projects in self._fetch_stars():

            for project in projects:

                # if not all((project.name, project.language)):
                #     logging.getLogger("uvicorn").warn(f"GHS: Could not save package {project.html_url}")
                #     break

                project_name = project.name.capitalize()
                current_stars.add(project_name)

                project_details = (
                    project_name,
                    str(
                        project.description
                    ),  # .replace("'", "''").replace('.', r'\.'),  # May be None, in which case 'None'
                    project.html_url,
                    project.stargazers_count,
                    project.forks_count,
                )

                query: str = """INSERT INTO project(
                        name, description, url, initial_stars,
                        current_stars, initial_fork_count,
                        current_fork_count
                    ) VALUES ($1, $2, $3, $4, $5, $6, $7) ON CONFLICT (name) DO UPDATE
                    SET description=$8, current_stars=$9, current_fork_count=$10
                    RETURNING project_id"""

                args: Tuple[Union[int, str], ...] = (
                    project_details[0],
                    project_details[1],
                    project_details[2],
                    project_details[3],
                    project_details[3],
                    project_details[4],
                    project_details[4],
                    project_details[1],
                    project_details[3],
                    project_details[4],
                )

                project_id: int = await self.dbh.upsert((query, *args))
                # Will implement batch inserts later

                # Save a project's main programming language
                language_id: int = await self.dbh.upsert(
                    (
                        """INSERT INTO pro_lang(name) values($1) ON CONFLICT (name) DO UPDATE
                    SET name = EXCLUDED.name
                    RETURNING language_id""",
                        project.language
                        or "Undetected",  # Need to set it (name) so RETURNING can work
                    )
                )

                # Create many-to-many relationship
                await self.dbh.upsert(
                    (
                        "INSERT INTO pr_pl values($1, $2) ON CONFLICT DO NOTHING",
                        *(language_id, project_id),
                    )
                )

        # Now we remove unstarred repos
        stored_stars: Set[str] = {
            p["name"] for p in await self.dbh.read("SELECT name FROM project")
        }
        fallen_stars: Set[str] = stored_stars - current_stars

        for star in fallen_stars:
            await self.dbh.delete(("DELETE FROM project WHERE name = $1", star))

        logging.getLogger("uvicorn").info("GHS: Update completed successfuly ✨")
