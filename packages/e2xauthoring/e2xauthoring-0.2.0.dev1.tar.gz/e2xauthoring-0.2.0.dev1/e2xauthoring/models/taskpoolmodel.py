import os
import shutil
import traceback as tb
from typing import Dict

from traitlets import Unicode

from ..utils.gitutils import create_repository, is_version_controlled
from .basemodel import BaseModel


class E2xTaskPoolModel(BaseModel):
    directory = Unicode("pools", help="The directory where the task pools go.")

    def new(self, **kwargs):
        name = kwargs["name"]
        if self.is_valid_name(name):
            path = os.path.join(self.base_path(), name)
            if os.path.exists(path):
                return {
                    "success": False,
                    "error": f"A pool with the name {name} already exists!",
                }
            else:
                os.makedirs(path, exist_ok=True)
                return {"success": True, "path": path}
        else:
            return {"success": False, "error": "Invalid name"}

    def remove(self, **kwargs):
        name = kwargs["name"]
        path = os.path.join(self.base_path(), name)
        shutil.rmtree(path)

    def get(self, **kwargs):
        name = kwargs["name"]
        tasks = self.__get_pool_info(name)
        return {
            "name": name,
            "tasks": tasks,
            "link": os.path.join("taskcreator", "pools", name),
        }

    def list(self, **kwargs):
        if not os.path.isdir(self.base_path()):
            os.makedirs(self.base_path(), exist_ok=True)
        poolfolders = os.listdir(self.base_path())
        pools = []
        for poolfolder in poolfolders:
            if poolfolder.startswith("."):
                continue
            tasks = self.__get_pool_info(poolfolder)
            pools.append(
                {
                    "name": poolfolder,
                    "tasks": tasks,
                    "link": os.path.join("taskcreator", "pools", poolfolder),
                }
            )

        return pools

    def __get_pool_info(self, name):
        return len(os.listdir(os.path.join(self.base_path(), name)))


class TaskPoolModel(E2xTaskPoolModel):
    def new(self, **kwargs) -> Dict[str, str]:
        """Create a new task pool

        Returns:
            Dict[str, str]: A status message
        """
        status = super().new(**kwargs)
        if not status["success"]:
            return status
        path = os.path.join(self.base_path(), kwargs["name"])
        if "create_repository" in kwargs and kwargs["create_repository"]:
            repo = create_repository(path, exists_ok=True)
            status["repository"] = repo is not None
        return status

    def turn_into_repository(self, pool):
        path = os.path.join(self.base_path(), pool)
        if not os.path.exists(path) or not os.path.isdir(path):
            return dict(
                status="error",
                error=f"The pool {pool} does not exist or is not a directory.",
            )
        repo = create_repository(path)
        return dict(success=repo is not None)

    def list(self, **kwargs):
        pools = super().list(**kwargs)
        for pool in pools:
            pool["is_repo"] = is_version_controlled(
                os.path.join(self.base_path(), pool["name"])
            )
            pool["tasks"] = self.__get_pool_info(pool["name"])
        return pools

    def get(self, pool):
        return dict(
            pool=pool,
            is_repo=is_version_controlled(os.path.join(self.base_path(), pool)),
            tasks=self.__get_pool_info(pool),
        )

    def remove(self, name):
        try:
            super().remove(name=name)
            return dict(status="success", message="")
        except Exception as e:
            return dict(
                status="error", message=tb.format_exception(None, e, e.__traceback__)
            )

    def __get_pool_info(self, name):
        return len(
            [
                d
                for d in os.listdir(os.path.join(self.base_path(), name))
                if not d.startswith(".")
            ]
        )
