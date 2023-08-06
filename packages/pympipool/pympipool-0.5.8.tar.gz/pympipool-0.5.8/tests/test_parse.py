import unittest
from pympipool.shared.backend import parse_arguments
from pympipool.shared.taskexecutor import command_line_options


class TestParser(unittest.TestCase):
    def test_command_local(self):
        result_dict = {
            'host': 'localhost',
            'zmqport': '22',
        }
        command_lst = [
            'mpiexec', '--oversubscribe',
            '-n', '2',
            'python', '/',
            '--zmqport', result_dict['zmqport']
        ]
        self.assertEqual(command_lst, command_line_options(
            hostname=result_dict['host'],
            port_selected=result_dict['zmqport'],
            path="/",
            cores=2,
            oversubscribe=True,
            enable_flux_backend=False,
        ))
        self.assertEqual(result_dict, parse_arguments(command_lst))

    def test_command_flux(self):
        result_dict = {
            'host': "127.0.0.1",
            'zmqport': '22',
        }
        command_lst = [
            'flux', 'run', '-n', '2', 'python', '/',
            '--host', result_dict['host'],
            '--zmqport', result_dict['zmqport']
        ]
        self.assertEqual(command_lst, command_line_options(
            hostname=result_dict['host'],
            port_selected=result_dict['zmqport'],
            path="/",
            cores=2,
            oversubscribe=False,
            enable_flux_backend=True,
        ))
        self.assertEqual(result_dict, parse_arguments(command_lst))
