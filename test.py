import unittest
import subprocess
import requests
import re
import time
import argparse


def get_port():
    # Looks up port number for container name given in argv
    port_mapping = subprocess.check_output(
        ['docker', 'port', get_args().container_name]
    ).decode('utf-8').strip()
    return re.search(':(\d+)', port_mapping).group(1)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--container_name', action='store')
    parser.add_argument('--skip_mounted', action='store_true')
    parser.add_argument('--skip_envvar_value', action='store_true')
    parser.add_argument('--skip_envvar_url', action='store_true')
    return parser.parse_args()

class ContainerTest(unittest.TestCase):

    def setUp(self):
        self.base = 'http://localhost:' + get_port()

        # TODO: This didn't work on Travis... should it?
        # session = requests.Session()
        # adapter = requests.adapters.HTTPAdapter(max_retries=10)  # default 0
        # session.mount('http://', adapter)

        for i in range(5):
            try:
                requests.get(self.base)
                break
            except:
                print('Still waiting for server...')
                time.sleep(1)
        else:
            self.fail('Server never came up')

    def test_home_page(self):
        response = requests.get(self.base)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tool Launch Data', response.text)

    @unittest.skipIf(get_args().skip_mounted, 'CLI param skip')
    def test_mounted_json(self):
        response = requests.get(self.base + '/data/input.json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Nils"', response.text)

    @unittest.skipIf(get_args().skip_envvar_value, 'CLI param skip')
    def test_envvar_value_json(self):
        response = requests.get(self.base + '/envvar_value.json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Chuck"', response.text)

    @unittest.skipIf(get_args().skip_envvar_url, 'CLI param skip')
    def test_envvar_url_json(self):
        response = requests.get(self.base + '/envvar_url.json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Scott"', response.text)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContainerTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print('''
browse:   http://localhost:{}/
clean up: docker ps -qa | xargs docker stop | xargs docker rm
    '''.format(get_port()))
    if result.wasSuccessful():
        print('PASS!')
    else:
        print('FAIL!')
        exit(1)
