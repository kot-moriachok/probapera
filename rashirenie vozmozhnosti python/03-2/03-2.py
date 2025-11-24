import asyncio
import aiohttp
from abc import ABC, abstractmethod

class Model(ABC):
	url = 'https://analitika.woysa.club/images/panel/json/download/niches.php'
	@abstractmethod
	def download(self, skip, category):
		pass

class Loader(Model):
	_instance = None

def __new__(cls, *args, **kwargs):
	if cls._instance is None:
		cls._instance = super().__new__(cls)
	return cls._instance

def download(self, skip, category):
    full_url = (
        f"{self.url}?skip={skip}&price_min=0&price_max=1060225"
        f"&up_vy_min=0&up_vy_max=108682515&up_vy_pr_min=0&up_vy_pr_max=2900"
        f"&sum_min=1000&sum_max=82432725&feedbacks_min=0&feedbacks_max=32767"
        f"&trend=false&sort=sum_sale&sort_dir=-1&id_cat={category}"
    )
    try:
        response = requests.get(full_url)
        if response.ok:
            return response.json()
        else:
            raise Exception(f"HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")

async def fetch_data(category):
	loader = Loader()
	for skip in range(0, 500, 100):
		data = loader.download(skip, category)
	if not data:
		break
	print(f"[{category}] Скачано {len(data)} записей с skip={skip}")

async def main():
	tasks = [fetch_data(cat) for cat in [1000, 1001, 1002]]
	await asyncio.gather(*tasks)

if __name__ == "__main__":
	asyncio.run(main())