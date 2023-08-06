import warnings
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from abc import ABC, abstractmethod
from datetime import datetime

from pydantic import Extra, Field, root_validator, validator

import promptlabs.chain as chain
from promptlabs.chain.base_chain import Chain
from promptlabs.scheme.template import ChainOutput, ChainLog, PipelineLog, PipelineOutput

def create_chain(chain_config) -> Chain:
    try:
        chain_class = getattr(chain, chain_config['type'])
        return chain_class(config=chain_config)
    except:
        raise ValueError(f"Invalid chain type: {chain_config['type']}")
class Pipeline:
    
    def __init__(self, config : Dict[str, Any]):
        self.config = config
        # add id to each chain_config from chain_id
        for chain_config in self.config["chain_configs"]:
            print(chain_config)
            chain_config['id'] = chain_config['chain_id']
        
        self.chains = [create_chain(chain_config) for chain_config in self.config["chain_configs"]]
    
    @property
    def input_keys(self) -> List[str]:
        return self.config["input_keys"]
    
    @property
    def output_keys(self) -> List[str]:
        
        return self.config["output_keys"]
                
                
    @root_validator(pre=True)
    def validate_chains(cls, values: Dict) -> Dict:
        config = values["config"]
        chain_configs = config["chain_configs"]
        pipe_input_keys = config["input_keys"]
        
        known_variables = pipe_input_keys
        for i, chain_config in enumerate(chain_configs):
            missing_vars = set(chain_config["input_keys"]).difference(known_variables)
            if missing_vars:
                raise ValueError(
                    f"Missing required input keys: {missing_vars} at chain {i}, "
                    f"chain config with error : {chain_config},"
                    f"only had {known_variables}"
                )
            known_variables |= set(chain_config["output_keys"])
        
        missing_vars = set(config["output_keys"]).difference(known_variables)
        if missing_vars:
            raise ValueError(
                    f"Expected output variables that were not found: {missing_vars}."
                )
        
        return values
        
    def _validate_inputs(self, inputs: Dict[str, Any]) -> None:
        """Check that all inputs are present."""
        missing_keys = set(self.input_keys).difference(inputs)
        if missing_keys:
            raise ValueError(f"Missing some input keys: {missing_keys}")
        
    def _validate_outputs(self, outputs: Dict[str, Any]) -> None:
        """Check that all outputs are present."""
        missing_keys = set(self.output_keys).difference(outputs)
        if missing_keys:
            raise ValueError(f"Missing some output keys: {missing_keys}")

    
    def run(self, inputs: Dict[str, Any]):
        
        # input validate
        try:
            self._validate_inputs(inputs)
        except Exception as e:
            return (
                PipelineOutput(pipeline_success=False),
                PipelineLog(logs={"error_log" : str(e)})
            )
            
        # pipeline log
        pipeline_log = PipelineLog()
        
        # run chains
        known_variables = inputs
        
        is_fail = False
        for i, chain_in_pipe in enumerate(self.chains):
            chain_inputs = {key: val for key, val in known_variables.items() if key in chain_in_pipe.input_keys}
            chain_outputs = {key: val for key, val in known_variables.items() if key in chain_in_pipe.output_keys}
            if chain_in_pipe is not None and not is_fail:
                if chain_in_pipe._chain_type == "FunctionChain" and chain_in_pipe._function is not None:
                    chain_output, chain_log = chain_in_pipe.run(chain_inputs)
                else:
                    chain_output, chain_log = chain_in_pipe.run(chain_inputs,chain_outputs)
                
                pipeline_log.chain_logs.append(chain_log)
                pipeline_log.chain_outputs.append(chain_output)
                
                if chain_output.chain_success == False:
                    is_fail = True
                    error_message = "{chain_type} Chain Step#{i} failed. Error log: {error_log}".format(
                        chain_type=type(chain_in_pipe),
                        i=i+1, 
                        error_log=chain_log.error_log)
                    pipeline_log.logs['error_log'] = error_message
                else:
                    outputs = chain_output.output_variables
                    known_variables.update(outputs)
            else:
                pipeline_log.chain_logs.append(
                    ChainLog(logs={"error_log" : "Error occurs before start this chain"})
                )
                pipeline_log.chain_outputs.append(
                    ChainOutput(chain_success=False)
                )
        
        if is_fail:

            return (
                PipelineOutput(pipeline_success=False),
                pipeline_log
            )
        
        output_variables = {key: val for key, val in known_variables.items() if key in self.output_keys}       

        return (
            PipelineOutput(pipeline_success=True, output_variables=output_variables),
            pipeline_log
        ) 
