import aiohttp
import asyncio
import os


async def download_image(session, url, filename):
    async with session.get(url) as response:
        if response.status == 200:
            with open(filename, "wb") as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {filename}")


async def download_all(num_images, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_images):
            url = "https://source.unsplash.com/random"
            filename = os.path.join(folder, f"image_{i}.jpg")
            tasks.append(download_image(session, url, filename))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    num_images = int(input("Enter number of images to download:"))
    folder = "artifacts"
    asyncio.run(download_all(num_images, folder))
