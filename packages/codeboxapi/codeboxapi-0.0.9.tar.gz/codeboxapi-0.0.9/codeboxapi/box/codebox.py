from typing import Any, Optional
from codeboxapi import settings
from codeboxapi.box import BaseBox
from ..utils import base_request, abase_request
from ..schema import (
    CodeBoxStatus, 
    CodeBoxOutput,
    CodeBoxFile
)
from aiohttp import ClientSession


class CodeBox(BaseBox):
    """ 
    Sandboxed Python Interpreter
    """
    
    def __new__(cls, *args, **kwargs):
        if settings.CODEBOX_API_KEY is None:
            from .localbox import LocalBox
            return LocalBox(*args, **kwargs)
        else:
            return super().__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.session: Optional[ClientSession] = None
    
    def codebox_request(
        self, 
        method, 
        endpoint, 
        *args, **kwargs
    ) -> dict[str, Any]:
        self._update()
        return base_request(
            method,
            f"/codebox/{self.id}" + endpoint,
            *args, **kwargs
        )
    
    async def acodebox_request(
        self,
        method,
        endpoint,
        *args, **kwargs
    ) -> dict[str, Any]:
        self._update()
        if self.session is None:
            raise RuntimeError("CodeBox session not started")
        return await abase_request(
            self.session,
            method,
            f"/codebox/{self.id}" + endpoint,
            *args, **kwargs
        )
    
    def start(self) -> CodeBoxStatus:
        self.id = base_request(
            method="GET",
            endpoint="/codebox/start",
        )["id"]
        return CodeBoxStatus(status="started")
    
    async def astart(self) -> CodeBoxStatus:
        self.session = ClientSession()
        self.id = (await abase_request(
            self.session,
            method="GET",
            endpoint="/codebox/start",
        ))["id"]
        return CodeBoxStatus(status="started")
    
    def status(self):
        return CodeBoxStatus(
            ** self.codebox_request(
                method="GET",
                endpoint="/",
            )
        )
    
    async def astatus(self):
        return CodeBoxStatus(
            ** await self.acodebox_request(
                method="GET",
                endpoint="/",
            )
        )
    
    def run(self, code: str):
        return CodeBoxOutput(
            ** self.codebox_request(
                method="POST",
                endpoint=f"/run",
                body={"code": code},
            )
        )
        
    async def arun(self, code: str):
        return CodeBoxOutput(
            ** await self.acodebox_request(
                method="POST",
                endpoint=f"/run",
                body={"code": code},
            )
        )

    def upload(
            self, 
            file_name: str, 
            content: bytes
        ) -> CodeBoxStatus:
        return CodeBoxStatus(
            ** self.codebox_request(
                method="POST",
                endpoint="/upload",
                files={"file": (file_name, content)},
                content_type=None
            ) 
        )
    
    async def aupload(
            self, 
            file_name: str, 
            content: bytes
        ) -> CodeBoxStatus:
        return CodeBoxStatus(
            ** await self.acodebox_request(
                method="POST",
                endpoint="/upload",
                files={"file": (file_name, content)},
                content_type=None
            ) 
        )
    
    def download(self, file_name: str) -> CodeBoxFile:
        return CodeBoxFile(
            ** self.codebox_request(
                method="GET",
                endpoint="/download",
                body={"file_name": file_name},
                content_type=None,
            )
        )
        
    async def adownload(self, file_name: str) -> CodeBoxFile:
        return CodeBoxFile(
            ** await self.acodebox_request(
                method="GET",
                endpoint="/download",
                body={"file_name": file_name},
                content_type=None,
            )
        )
        
    def install(self, package_name: str) -> CodeBoxStatus:
        return CodeBoxStatus(
            ** self.codebox_request(
                method="POST",
                endpoint="/install",
                body={
                    "package_name": package_name,
                },
            )
        )
    
    async def ainstall(self, package_name: str) -> CodeBoxStatus:
        return CodeBoxStatus(
            ** await self.acodebox_request(
                method="POST",
                endpoint="/install",
                body={
                    "package_name": package_name,
                },
            )
        )
    
    def list_files(self) -> list[CodeBoxFile]:
        return [
            CodeBoxFile(name=file_name, content=None) 
            for file_name in (
                self.codebox_request(
                    method="GET",
                    endpoint="/files",
                ))["files"]
            ]
        
    async def alist_files(self) -> list[CodeBoxFile]:
        return [
            CodeBoxFile(name=file_name, content=None) 
            for file_name in (
                await self.acodebox_request(
                    method="GET",
                    endpoint="/files",
                ))["files"]
            ]
    
    def stop(self) -> CodeBoxStatus:
        return CodeBoxStatus(
            ** self.codebox_request(
                method="POST",
                endpoint="/stop",
            )
        )

    async def astop(self) -> CodeBoxStatus:
        if self.session:
            await self.session.close()
            self.session = None
        
        return CodeBoxStatus(
            ** await self.acodebox_request(
                method="POST",
                endpoint="/stop",
            )
        )
    