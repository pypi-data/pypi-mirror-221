import warnings
import os
from datetime import datetime
import re

from typing import Any, Dict, List, Callable, Optional, Sequence, Tuple, Union
from abc import ABC, abstractmethod

from pydantic import Extra, Field, root_validator, validator

from promptlabs.chain.base_chain import Chain
from promptlabs.scheme.template import ChainOutput, ChainLog
from promptlabs.scheme.llm import ChatOpenAI, BaseLLM

class LLMChain(Chain):

    llm : BaseLLM
    
    @root_validator(pre=True)
    def set_llm(cls, values: Dict) -> Dict:
        if "llm_function" not in values['config']:
            chat_openai_config = {
                "model_name": values['config']['model_name'],
                "temperature": values['config'].get('temperature', 0.7),
                "max_tokens": values['config'].get('max_tokens')
            }
            if 'openai_api_key' in values['config']:
                chat_openai_config["openai_api_key"] = values['config']['openai_api_key']
            values['llm'] = ChatOpenAI(
                **chat_openai_config
            )
        else:
            values['llm'] = values['config']["llm_function"]
        return values
    
    @property
    def _chain_type(self) -> str:
        return self.config["type"]
    
    @property
    def model_name(self) -> str:
        return self.config["model_name"]
    
    @property
    def prompt(self) -> str:
        return self.config["prompt"]
    
    @property
    def system_prompt(self) -> str:
        default_system_prompt = "You are a helpful assistant."
        if 'system_prompt' not in self.config:  
            return default_system_prompt
        else:
            return self.config["system_prompt"]
    
    
    # def set_llm(self) -> BaseLLM:
    #     if "llm_function" not in self.config:
    #         if 'temperature' not in self.config:
    #             temperature = 0.7
    #         if 'max_tokens' not in self.config:
    #             max_tokens = None
    #         return ChatOpenAI(
    #             model_name=self.model_name,
    #             openai_api_key=self.config['openai_api_key'],
    #             temperature=temperature,
    #             max_tokens=max_tokens
    #         )
    #     else:
    #         return self.config["llm_function"]

    def _call_llm_submodule(
        self,
        inputs: Dict[str, Any]
    ) -> Dict[str, Any]:
        max_retry = 3
        retry_count = 0
        raw_output = None
        
        while retry_count < max_retry:
            openai_call_error = None
            parsing_error = None
            validation_error = None
            try:
                try:
                    messages = [
                        {"role": "system", "content" : self.system_prompt},
                        {"role": "user", "content" : self.prompt.format(**inputs)}
                    ]
                    is_success, response = self.llm.generate(
                        messages=messages
                    )
                    print(is_success, response)
                    if not is_success:
                        raise Exception("OpenAI call error : " + str(response))
                    raw_output = response["response"]['choices'][0]["message"]['content']
                except Exception as e:
                    openai_call_error = "OpenAI call error: " + str(e)
                    raise

                parsed_output = {
                    "text" : raw_output
                }

                try:
                    self._validate_outputs(parsed_output)
                except Exception as e:
                    validation_error = "Validation error: " + str(e)
                    raise

                return {
                    "status" : "success",
                    "parsed_output" : parsed_output,
                    "raw_output" : response,
                }
                
            except Exception as e:
                retry_count += 1
                print("retry count: " + str(retry_count))
                if retry_count == max_retry:
                    error_log = "\n".join(filter(None, [openai_call_error, parsing_error, validation_error]))

                    if raw_output:
                        return {
                            "status": "error", 
                            "error_log": error_log,
                            "raw_output": raw_output
                        }
                    else:
                        return {
                            "status": "error", 
                            "error_log": error_log
                        }
                continue
        
    
    def validate(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any] = {}
    ) -> Dict[str, Any]:
        """Validate the chain."""
        
        # input validate
        try:
            self._validate_inputs(inputs)
        except Exception as e:
            return {   
                "validated" : False,
                "error_log": str(e),
                "output_variables" : {}
            }
            
        # openai call validate    
        llm_result = self._call_llm_submodule(inputs)
        
        if llm_result['status'] == 'error':
            return {   
                "validated" : False,
                "error_log": llm_result['error_log']
            }
        else:
            return {
                "validated" : True,
                "output_variables" : llm_result['parsed_output']
            }

    
    def run(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any] = {}
    ) -> Tuple[ChainOutput, ChainLog]:
        
        # Validate inputs
        try:
            self._validate_inputs(inputs)
        except Exception as e:
            return ChainOutput(chain_success=False), ChainLog(logs={"error_log": str(e)})

        # openai call validate
        llm_result = self._call_llm_submodule(inputs=inputs)

        if llm_result['status'] == 'error':
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs={"error_log": llm_result['error_log']})
            )
        else:
            return (
                ChainOutput(chain_success=True, output_variables=llm_result['parsed_output']),
                ChainLog(logs={"raw_output": llm_result['raw_output']})
            )

class LLMRegexChain(LLMChain):
    def _call_llm_submodule(
        self,
        inputs: Dict[str, Any]
    ) -> Dict[str, Any]:
        max_retry = 3
        retry_count = 0
        raw_output = None
        
        while retry_count < max_retry:
            openai_call_error = None
            parsing_error = None
            validation_error = None
            try:
                try:
                    messages = [
                        {"role": "system", "content" : self.system_prompt},
                        {"role": "user", "content" : self.prompt.format(**inputs)}
                    ]
                    is_success, response = self.llm.generate(
                        messages=messages
                    )
                    print(is_success, response)
                    if not is_success:
                        raise Exception("OpenAI call error : " + str(response))
                    raw_output = response["response"]['choices'][0]["message"]['content']
                except Exception as e:
                    openai_call_error = "OpenAI call error: " + str(e)
                    raise

                parsed_output = {}

                try:
                    output_keys = self.output_keys
                    for key in output_keys:
                        # capitalize the first letter of the key
                        capitalized_key = key[0].upper() + key[1:]
                        # make the regular expression
                        pattern = r"\[{}(\s*\(.+\))?\sstart\](.*?)\[{}(\s*\(.+\))?\send\]".format(capitalized_key, capitalized_key)
                        results = re.findall(pattern, raw_output, re.DOTALL)
                        results = [result[1] for result in results]
                        if results:
                            if len(results) > 1: 
                                raise Exception("Multiple Matches")
                            parsed_output[key] = results[0].strip()
                except Exception as e:
                    parsing_error = "Parsing error: " + str(e)
                    raise

                try:
                    self._validate_outputs(parsed_output)
                except Exception as e:
                    validation_error = "Validation error: " + str(e)
                    raise

                return {
                    "status" : "success",
                    "parsed_output" : parsed_output,
                    "raw_output" : response,
                }
                
            except Exception as e:
                retry_count += 1
                print("retry count: " + str(retry_count))
                if retry_count == max_retry:
                    error_log = "\n".join(filter(None, [openai_call_error, parsing_error, validation_error]))

                    if raw_output:
                        return {
                            "status": "error", 
                            "error_log": error_log,
                            "raw_output": raw_output
                        }
                    else:
                        return {
                            "status": "error", 
                            "error_log": error_log
                        }
                continue
        