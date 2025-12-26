import requests
import asyncio
import desktop_notifier

base_url = "https://api.mangadex.org"

async def main():
    interval = 180
    manga_id = "ea0e7020-2b2f-4f17-9251-fee3632dc135"
    manga_name = "Marika-chan no Koukando wa Bukkowarete iru"
    previous_len = chapter_data(manga_id)

    while True:
        await asyncio.sleep(interval)
        current_len = chapter_data(manga_id)
        if not current_len != previous_len:
            continue
        if current_len[0]["id"] != previous_len[0]['id']:
            latest_len = chapter_data(manga_id)[0]["id"]
            await desktop_notifier.DesktopNotifier().send(
                title= f"New chapter of {manga_name}",
                message= f"https://mangadex.org/chapter/{latest_len}"
            )
            previous_len = current_len



def chapter_data(manga_id):
    r = requests.get(f"{base_url}/manga/{manga_id}/feed", params={
        "translatedLanguage[]": ["en"],
        "order[chapter]": "desc",  # latest chapter first
        "limit": 1}
        )
    r.raise_for_status()
    data = r.json()["data"]
    return data


asyncio.run(main())
