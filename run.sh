#!/usr/bin/env sh

set -e

pytest -sv --alluredir="logs"
allure serve --host 0.0.0.0 --port 9000 logs