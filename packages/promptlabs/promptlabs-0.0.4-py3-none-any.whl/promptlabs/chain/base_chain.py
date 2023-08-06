import warnings
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from abc import ABC, abstractmethod

from pydantic import BaseModel, Extra, Field, root_validator, validator
from promptlabs.scheme.template import ChainOutput, ChainLog

class Chain(BaseModel, ABC):
    """Base class for all chains."""
    config : Dict[str, Any]
    
    @property
    def input_keys(self) -> List[str]:
        return self.config["input_keys"]
    
    @property
    def output_keys(self) -> List[str]:
        return self.config["output_keys"]
    
    @property
    def _chain_type(self) -> str:
        raise NotImplementedError("Saving not supported for this chain type.")
    
    def _validate_inputs(self, inputs: Dict[str, Any]) -> None:
        """Check that all inputs are present."""
        missing_keys = set(self.input_keys).difference(inputs)
        if missing_keys:
            raise ValueError(f"Missing some input keys: {missing_keys}")

    def _validate_outputs(self, outputs: Dict[str, Any]) -> None:
        missing_keys = set(self.output_keys).difference(outputs)
        if missing_keys:
            raise ValueError(f"Missing some output keys: {missing_keys}")
        
    # @abstractmethod
    # def validate(
    #     self,
    #     inputs: Dict[str, Any],
    #     outputs: Dict[str, Any] = {}
    # ) -> Dict[str, Any]:
    #     """Validate the chain."""
    #     pass
    
    # @abstractmethod
    # def test(
    #     self,
    #     inputs: Dict[str, Any],
    #     outputs: Dict[str, Any] = {}
    # ) -> Dict[str, Any]:
    #     """Run the chain."""
    #     pass
    
    @abstractmethod
    def run(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any] = {}
    ) -> Tuple[ChainOutput, ChainLog]:
        """Run the chain."""
        pass