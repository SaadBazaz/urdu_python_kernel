from ipykernel.kernelbase import Kernel

from ipykernel.ipkernel import IPythonKernel

from urdupython import run_module, SCRIPTDIR

from io import StringIO
import sys

import os

class UrduPythonKernel(IPythonKernel):
    implementation = 'UrduPython'
    implementation_version = '1.1'
    # language_version = '0.1'
    language_info = {
        'name': 'python',
        'version': sys.version.split()[0],
        'mimetype': 'text/x-python',
        'file_extension': '.py',
    }
    banner = "UrduPython kernel"

    
    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        

        error_thrown = False

        try:
            compiled_code = run_module("lex", code, args = {
                            'translate': True,
                            'dictionary': os.path.join(SCRIPTDIR, '../', 'languages/ur/ur_native.lang.yaml'),
                            'reverse': False,
                            'keep': False,         
                            'keep_only': False,
                            'return': True,
                        })
        except Exception as e:
            error_thrown = True
            error_message = "Error: " + str(e)
            print (error_message)

        return super(UrduPythonKernel, self).do_execute(compiled_code, silent, store_history, user_expressions,
                   allow_stdin)


    def do_complete(self, code, cursor_pos):
        error_thrown = False

        # try:
        compiled_code = run_module("lex", code, args = {
        'translate': True,
        'dictionary': os.path.join(SCRIPTDIR, '../', 'languages/ur/ur_native.lang.yaml'),
        'reverse': False,
        'keep': False,         
        'keep_only': False,
        'return': True,
    })
            # except Exception as e:
            #     error_thrown = True
            #     error_message = "Error: " + str(e)
            #     print (error_message)

        return super(UrduPythonKernel, self).do_complete(compiled_code, cursor_pos)