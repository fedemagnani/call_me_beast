import logging
import argparse
import os

output_dir = os.environ['OUTPUT_DIR']

# # Make output directory
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# get a file logger
def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(f'{output_dir}/test.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger

def add(x, y):
    return x + y

if __name__ == '__main__':
    logger = get_logger()
    logger.info('test')
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=int, required=True)
    parser.add_argument('--y', type=int, required=True)
    args = parser.parse_args()

    print(add((args.x), args.y))
    logger.info('x: {}, y: {}'.format(args.x, args.y))

    result = add(args.x, args.y)
    logger.info('result: {}'.format(result))

    # Save the result to a file in /output
    with open(output_dir+'/result.txt', 'w+') as f:
        f.write(str(result))
