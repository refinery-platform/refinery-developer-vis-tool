import unittest
import subprocess
import requests
import sys
import re
import time


def get_port():
    # Looks up port number for container name given in argv
    port_mapping = subprocess.check_output(
        ['docker', 'port', sys.argv[1]]
    ).decode('utf-8').strip()
    return re.search(':(\d+)', port_mapping).group(1)

class ContainerTest(unittest.TestCase):

    def setUp(self):
        port = get_port()
        self.base = 'http://localhost:' + port

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

    def test_mounted_json(self):
        response = requests.get(self.base + '/data/input.json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Nils"', response.text)

    def test_envvar_value_json(self):
        response = requests.get(self.base + '/envvar_value.json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Chuck"', response.text)

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
