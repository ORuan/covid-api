from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent


def commit_errors(erro, file_):
    print(f'ERROR in {file_}: {erro} -- {datetime.now().strftime("%H:%M:%S")}\n')
    try:
        with open(f'{BASE_DIR}/.bf4.log', 'a') as logging:
            logging.writelines(f'ERROR in {file_}: {erro} -- {datetime.now().strftime("%H:%M:%S")}\n')
    except Exception as err:
        print(err)