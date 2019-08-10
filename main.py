from Story import Story
import time

def printer(contents):
    for content in contents:
        print(content)
        time.sleep(1)


def main():
	plot = Story()
	st = plot.get_start()
	while True:
		printer(st)
		if plot.checkpoint == plot.end:
			break
		st = plot.select_checkpoint()


if __name__ == "__main__":
    main()
    pass