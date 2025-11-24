from abc import ABC, abstractmethod
import requests
import aiohttp
import asyncio


class Model(ABC):
    url = 'https://analitika.woysa.club/images/panel/json/download/niches.php'
    @abstractmethod
    def download(self, skip, category):
        pass

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    html = await fetch(Model.url)
    print(html[:500])

if __name__ == "__main__":
    asyncio.run(main())

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

loader = Loader()
data = loader.download(100, 1000)
print(data)



