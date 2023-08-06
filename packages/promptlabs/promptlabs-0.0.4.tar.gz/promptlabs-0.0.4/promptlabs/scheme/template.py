from __future__ import annotations

from typing import Any, Dict, List
from pydantic import BaseModel
from abc import ABC, abstractmethod

class BaseTemplate(BaseModel, ABC):
    def show(self):
        return self.dict()

    def __str__(self):
        return str(self.show())

class ChainOutput(BaseTemplate):
    chain_success: bool
    output_variables: Dict[str, Any] = {}

    
class ChainLog(BaseTemplate):
    logs: Dict[str, Any] = {}
    

class PipelineOutput(BaseTemplate):
    pipeline_success: bool
    output_variables: Dict[str, Any] = {}

    
class PipelineLog(BaseTemplate):
    chain_logs: List[ChainLog] = []
    chain_outputs: List[ChainOutput] = []
    logs: Dict[str, Any] = {}
    
    