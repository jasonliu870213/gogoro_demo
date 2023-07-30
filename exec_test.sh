source /Users/liuchenghsuan/PycharmProjects/gogoro_demo/venv/bin/activate
pip install -r requirements.txt
pytest --reruns 2 test_api/test_demo.py --alluredir=./allure-results
