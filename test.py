import logging

logging.basicConfig(
    filename='example.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)


def log_to_file():
    i = 0
    while i < 10:
        logging.info(i)
        i += 1


if __name__ == '__main__':
    log_to_file()