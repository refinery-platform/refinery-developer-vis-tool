import unittest
import os
import subprocess
import time
import requests
import sys


class ContainerTest(unittest.TestCase):

    def setUp(self):
        # self.suffix = os.environ['SUFFIX']
        # self.stamp = os.environ['STAMP']
        command = "docker port {NAME} | perl -pne 's/.*://'".format(
            **os.environ)
        os.environ['PORT'] = subprocess.check_output(
            command, shell=True).strip().decode('utf-8')
        url = 'http://localhost:{PORT}/'.format(**os.environ)
        for i in range(5):
            if 0 == subprocess.call('curl --fail --silent ' + url + ' > /dev/null', shell=True):
                return
            print('Still waiting for server...')
            time.sleep(1)
        self.fail('Server never came up')

    def test_home_page(self):
        response = requests.get('http://localhost:{PORT}'.format(**os.environ))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tool Launch Data', response.text)

    def test_mounted_json(self):
        response = requests.get(
            'http://localhost:{PORT}/data/input.json'.format(**os.environ)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Nils"', response.text)

    def test_envvar_value_json(self):
        response = requests.get(
            'http://localhost:{PORT}/envvar_value.json'.format(**os.environ)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Chuck"', response.text)

    def test_envvar_url_json(self):
        response = requests.get(
            'http://localhost:{PORT}/envvar_url.json'.format(**os.environ)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('"Scott"', response.text)

if __name__ == '__main__':
    os.environ['NAME'] = sys.argv[1]

    suite = unittest.TestLoader().loadTestsFromTestCase(ContainerTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print('''
browse:   http://localhost:{PORT}/
clean up: docker ps -qa | xargs docker stop | xargs docker rm
    '''.format(**os.environ))
    if result.wasSuccessful():
        print('PASS!')
    else:
        print('FAIL!')
        exit(1)
