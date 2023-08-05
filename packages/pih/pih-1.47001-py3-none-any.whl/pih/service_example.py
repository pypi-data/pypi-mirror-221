import importlib.util
import sys

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih import A

#version 1.0
SR = A.CT_SR
SC = A.CT_SC

ROLE: SR = SR.DEVELOPER
if A.U.update_for_service(ROLE):

    from typing import Any
    from pih.tools import ParameterList

    def service_call_handler(sc: SC, parameter_list: ParameterList) -> Any:    
        return None
    
    def service_starts_handler() -> None:
        pass
       
    A.SRV_A.serve(ROLE, service_call_handler, service_starts_handler)
