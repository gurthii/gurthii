from tengo import price_updater_app
from time import sleep

def main():
	counter = 1
	print(f"___Starting Loop {counter}___")
	while True:
		price_updater_app()	
		print(f"Loop {counter} complete. Waiting for next run...\n")
		sleep(120) # runs every 1 hour
		counter += 1
			
if __name__ == "__main__":
    main()	
