import sys

print(sys.version)
print(sys.path)


import torch
import time
import logging
from torch.utils.tensorboard import SummaryWriter

logger = logging.getLogger(__name__)
# Writer will output to ./runs/ directory by default
writer = SummaryWriter()


def main():
	# logging.basicConfig(filename='test.log', level=logging.INFO)
	# https://stackoverflow.com/a/46098711/8612123
	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s [%(levelname)s] %(message)s",
		handlers=[
			logging.FileHandler("test.log"),
			logging.StreamHandler()
		]
	)

	logger.info('Started')
	a = torch.ones((2,2))
	a.cuda()
	logger.info(f"type of a:{type(a)}")
	for i in range(20):
		writer.add_scalar('y=2x', i * 2, i, time.time())
		time.sleep(1)
	# writer.add_image('images', grid, 0)
	# writer.add_graph(model, images)
	writer.close()

	logger.info('Finished')

if __name__ == '__main__':
	main()






