from RestrictedPython import compile_restricted
from RestrictedPython.Eval import default_guarded_getiter
from RestrictedPython.Guards import safe_builtins
from RestrictedPython.PrintCollector import PrintCollector

def execute_code(text):
    byte_code = compile_restricted(text, filename='<inline>', mode='exec')

    exec_env = {
        '__builtins__': safe_builtins,
        '_getiter_': default_guarded_getiter,
        '_print_': PrintCollector,             
        'print': PrintCollector,              
    }

    exec(byte_code, exec_env)
    return exec_env['_print']()
